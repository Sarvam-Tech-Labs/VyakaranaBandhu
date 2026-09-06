"""
Lightweight Web & API Server for Sanskrit Morphological Classifier & Pāṇinian Subanta Engine
Uses Python's standard http.server with JSON API support and static file serving.
"""

import os
import sys
import json
import urllib.parse
from typing import Any
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from src.classifier import SanskritClassifier
from src.subanta_engine import SubantaEngine
from src.quad_concordance import QuadConcordanceEngine
from src.krdanta_taddhita import KrdantaTaddhitaEngine
from src.verse_dependency import VerseDependencyEngine
from src.dossier_exporter import DossierExporter
from src.chandas import chandas_report

# The Aṣṭādhyāyī codification. Imported lazily inside the handlers rather
# than here: loading it reads the corpus off disk, and a server started to
# classify one word should not pay for that. `/api/tinanta/*` below is one
# of these: it is the sūtra-driven engine (src/astadhyayi/vyutpatti.py),
# not the hand-written src/tinanta_engine.py — see _tinanta_generate_payload
# and _tinanta_reverse_payload for why the old one was retired from the UI.

# Static UI root: ui/ holds the Bhakta Bandhu design-system front end.
WEB_DIR = os.path.join(os.path.dirname(__file__), "ui")
PORT = 8000

# Initialize engines
classifier = SanskritClassifier()
subanta_engine = SubantaEngine()
quad_engine = QuadConcordanceEngine(subanta_engine)
krdanta_engine = KrdantaTaddhitaEngine()
verse_dependency_engine = VerseDependencyEngine(classifier)
dossier_exporter = DossierExporter(subanta_engine, quad_engine)


#: प्रथम/मध्यम/उत्तम — display labels for the three puruṣas, matched to
#: the row order `src.astadhyayi.vibhakti.PERSONS` already fixes by
#: 1.4.101 तिङस्त्रीणि त्रीणि. Kept here rather than in the engine because
#: this is a UI label, not a grammatical fact.
_PURUSHA_LABELS = [
    ("Prathama Puruṣa (प्रथम पुरुषः / 3rd Person)", "3rd"),
    ("Madhyama Puruṣa (मध्यम पुरुषः / 2nd Person)", "2nd"),
    ("Uttama Puruṣa (उत्तम पुरुषः / 1st Person)", "1st"),
]
_VACANA_LABELS = [
    ("Ekavacana (एकवचनम् / Singular)", "sg"),
    ("Dvivacana (द्विवचनम् / Dual)", "du"),
    ("Bahuvacana (बहुवचनम् / Plural)", "pl"),
]
_GANA_NAMES = {
    1: "भ्वादि", 2: "अदादि", 3: "जुहोत्यादि", 4: "दिवादि", 5: "स्वादि",
    6: "तुदादि", 7: "रुधादि", 8: "तनादि", 9: "क्र्यादि", 10: "चुरादि",
}


def _tinanta_entry_payload(entry) -> dict:
    """
    One dhātupāṭha entry, conjugated in लट् (laṭ) with its full trace.

    Every cell either carries a form and the sūtras that made it, or is
    marked `withheld` — a slot the engine cannot yet finish (7.2.81 आतो
    ङितः, say) is reported as missing, never guessed at. That is the
    same honesty `vyutpatti.owed_for` gives the CLI, carried into JSON.
    """
    from src.astadhyayi.vyutpatti import paradigm, prakriya_payload
    from src.normalizer import iast_to_devanagari as dev

    gana_code = str(entry.gana).zfill(2)
    made = {(m.person, m.number): m for m in paradigm(entry.upadesa,
                                                      gana_code)}
    pada = next(iter(made.values())).pada if made else "parasmaipada"

    table = []
    for p_idx, (p_label, p_short) in enumerate(_PURUSHA_LABELS):
        row = []
        for v_idx, (v_label, v_short) in enumerate(_VACANA_LABELS):
            slot = made.get((p_idx, v_idx))
            if slot is None:
                row.append({
                    "purusha_short": p_short, "vacana_short": v_short,
                    "withheld": True,
                })
                continue
            row.append({
                "purusha_short": p_short, "vacana_short": v_short,
                "withheld": False,
                "devanagari": dev(slot.surface),
                "iast": slot.surface,
                "sutra": (slot.prakriya.steps[-1].sutra
                          if slot.prakriya.steps else ""),
                "derivation": prakriya_payload(slot.prakriya),
            })
        table.append({"purusha": p_label, "purusha_short": p_short,
                      "forms": row})

    return {
        "code": entry.code,
        "upadesa_iast": entry.upadesa,
        "upadesa_devanagari": dev(entry.upadesa),
        "root_iast": entry.dhatu,
        "root_devanagari": dev(entry.dhatu),
        "artha": entry.artha,
        "gana": entry.gana,
        "gana_name": _GANA_NAMES.get(entry.gana, ""),
        "pada_type": pada.capitalize(),
        "table": table,
    }


def _tinanta_generate_payload(root: str) -> dict:
    """
    `root` conjugated in लट् (laṭ) — every dhātupāṭha entry the name
    reaches, each with a full sūtra-by-sūtra trace per cell.

    Replaces the old hand-written `TinantaEngine`, which covered five
    hardcoded roots per lakāra and invented a generic ending for every
    other root regardless of its actual gaṇa — a confident wrong answer
    for anything outside its short list. This derives every form from
    the codified rules against the real ~2,229-root dhātupāṭha, and is
    silent (an empty `entries` list) rather than wrong where the root is
    not there or its gaṇa is not yet wired — see `vyutpatti.unreachable`.
    """
    from src.astadhyayi.vyutpatti import entries_of_name

    root = (root or "").strip()
    if not root:
        return {"error": "Enter a dhātu first."}
    entries = entries_of_name(root)
    if not entries:
        return {
            "error": (
                f"'{root}' is not a root the dhātupāṭha has, or its gaṇa "
                f"is not yet wired into the engine."
            ),
            "entries": [],
        }
    return {"root_query": root,
            "entries": [_tinanta_entry_payload(e) for e in entries]}


def _tinanta_reverse_payload(word: str) -> dict:
    """
    Every root the grammar could have made `word` from, in लट् (laṭ).

    The reverse direction: no rule of the Aṣṭādhyāyī runs backwards, so
    this makes every verb the engine can make from the ~2,229-root
    dhātupāṭha and matches. Two answers for one word is not an error —
    जयति (jayati) genuinely comes from two entries of जि (ji), one sense
    apiece — and the response says so rather than picking one.
    """
    from src.astadhyayi.vyutpatti import roots_of, prakriya_payload
    from src.normalizer import iast_to_devanagari as dev

    word = (word or "").strip()
    if not word:
        return {"error": "Enter a word first."}
    found = roots_of(word)
    if not found:
        return {
            "error": (
                f"No root in reach makes '{word}' — either it is not a "
                f"लट् (laṭ) parasmaipada/ātmanepada form, or a rule it "
                f"needs is codified but not yet wired into the engine."
            ),
            "matches": [],
        }
    matches = []
    for one in found:
        matches.append({
            "code": one.code,
            "upadesa_iast": one.upadesa,
            "upadesa_devanagari": dev(one.upadesa),
            "root_iast": one.dhatu,
            "root_devanagari": dev(one.dhatu),
            "artha": one.artha,
            "gana": one.gana,
            "gana_name": _GANA_NAMES.get(one.gana, ""),
            "pada_type": one.pada.capitalize(),
            "purusha": _PURUSHA_LABELS[one.person][0],
            "vacana": _VACANA_LABELS[one.number][0],
            "derivation": prakriya_payload(one.prakriya),
        })
    return {"word_query": word, "matches": matches}


class SanskritAPIHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def do_GET(self):
        try:
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)

            # 1. /api/classify?text=...
            if parsed.path == "/api/classify":
                text = params.get("text", [""])[0]
                result = classifier.classify(text)
                self._send_json(result)
                return

            # 2. /api/subanta/generate?stem=...&gender=...
            if parsed.path == "/api/subanta/generate":
                stem = params.get("stem", [""])[0]
                gender = params.get("gender", [None])[0]
                result = subanta_engine.generate_shabdarupa(stem, gender)
                self._send_json(result)
                return

            # 3. /api/subanta/analyze?pada=...
            if parsed.path == "/api/subanta/analyze":
                pada = params.get("pada", [""])[0]
                result = subanta_engine.analyze_subanta(pada)
                self._send_json({"pada": pada, "analyses": result})
                return

            # 4. /api/subanta/prakriya?stem=...&gender=...&vibhakti_idx=...&vacana_idx=...
            if parsed.path == "/api/subanta/prakriya":
                stem = params.get("stem", [""])[0]
                gender = params.get("gender", [None])[0]
                v_idx = int(params.get("vibhakti_idx", ["0"])[0])
                vac_idx = int(params.get("vacana_idx", ["0"])[0])
                result = subanta_engine.derive_prakriya(stem, gender, v_idx, vac_idx)
                self._send_json(result)
                return

            # 5. /api/subanta/concordance?stem=...&gender=...&vibhakti_idx=...&vacana_idx=...
            if parsed.path == "/api/subanta/concordance":
                stem = params.get("stem", [""])[0]
                gender = params.get("gender", [None])[0]
                v_idx = int(params.get("vibhakti_idx", ["0"])[0])
                vac_idx = int(params.get("vacana_idx", ["0"])[0])
                result = quad_engine.generate_quad_concordance(stem, gender, v_idx, vac_idx)
                self._send_json(result)
                return

            # 6. /api/tinanta/generate?root=...
            # लट् (laṭ) only, and the pada is derived, not chosen — see
            # _tinanta_generate_payload.
            if parsed.path == "/api/tinanta/generate":
                root = params.get("root", ["bhū"])[0]
                self._send_json(_tinanta_generate_payload(root))
                return

            # 6b. /api/tinanta/reverse?word=...
            if parsed.path == "/api/tinanta/reverse":
                word = params.get("word", [""])[0]
                self._send_json(_tinanta_reverse_payload(word))
                return

            # 7. /api/krdanta/generate?root=...&affix=...&upasarga=...
            if parsed.path == "/api/krdanta/generate":
                root = params.get("root", ["kṛ"])[0]
                affix = params.get("affix", ["ktva"])[0]
                upasarga = params.get("upasarga", [None])[0]
                result = krdanta_engine.derive_krdanta(root, affix, upasarga)
                self._send_json(result)
                return

            # 8. /api/taddhita/generate?stem=...&affix=...
            if parsed.path == "/api/taddhita/generate":
                stem = params.get("stem", ["dharma"])[0]
                affix = params.get("affix", ["thak"])[0]
                result = krdanta_engine.derive_taddhita(stem, affix)
                self._send_json(result)
                return

            # 9. /api/verse/dependency_tree?verse=...
            if parsed.path == "/api/verse/dependency_tree":
                verse = params.get("verse", ["dharmakṣetre kurukṣetre samavetā yuyutsavaḥ"])[0]
                result = verse_dependency_engine.build_dependency_tree(verse)
                self._send_json(result)
                return

            # 10. /api/dossier/export?pada=...&format=...
            if parsed.path == "/api/dossier/export":
                pada = params.get("pada", ["rāmaḥ"])[0]
                fmt = params.get("format", ["markdown"])[0]
                result = dossier_exporter.export_subanta_dossier(pada, fmt)
                if fmt == "html":
                    self._send_html(result["content"])
                    return
                self._send_json(result)
                return

            # 11. /api/chandas/analyze?text=...&script=...&boundary_mode=...&tradition=...
            if parsed.path == "/api/chandas/analyze":
                text = params.get("text", [""])[0]
                result = chandas_report(
                    text,
                    script=params.get("script", ["auto"])[0],
                    boundary_mode=params.get("boundary_mode", ["auto"])[0],
                    tradition=params.get("tradition", ["auto"])[0],
                )
                self._send_json(result)
                return

            # Aṣṭādhyāyī — the codification browser and playground.
            if parsed.path.startswith("/api/astadhyayi/"):
                from src.astadhyayi import api as astadhyayi_api

                leaf = parsed.path[len("/api/astadhyayi/"):]
                if leaf == "catalogue":
                    self._send_json(astadhyayi_api.catalogue())
                    return
                if leaf == "sutra":
                    sutra_id = params.get("id", [""])[0]
                    self._send_json(astadhyayi_api.detail(sutra_id))
                    return
                if leaf == "graph":
                    # `depth` used to be read here and is deliberately no
                    # longer accepted: the corpus is transitive, so the walk
                    # always runs to the top of the chain. An old link that
                    # still carries the parameter is answered, not refused.
                    sutra_id = params.get("id", [""])[0]
                    self._send_json(astadhyayi_api.graph(sutra_id))
                    return
                if leaf == "dependents":
                    sutra_id = params.get("id", [""])[0]
                    self._send_json(
                        {"id": sutra_id,
                         "dependents": astadhyayi_api.dependents(sutra_id)}
                    )
                    return

            # Default static file serving from the UI directory
            return super().do_GET()
        except Exception as err:
            self._send_json({"error": str(err)})

    def do_POST(self):
        try:
            parsed = urllib.parse.urlparse(self.path)
            content_len_header = self.headers.get("Content-Length")
            content_length = int(content_len_header) if content_len_header else 0
            if content_length > 0:
                post_data = self.rfile.read(content_length).decode("utf-8")
            else:
                post_data = ""
            
            try:
                data = json.loads(post_data) if post_data else {}
            except Exception:
                data = {"text": post_data}

            # Aṣṭādhyāyī — run one codified rule on values from the form.
            if parsed.path == "/api/astadhyayi/run":
                from src.astadhyayi import playground

                self._send_json(
                    playground.run(
                        data.get("id", ""), data.get("values", {}) or {}
                    )
                )
                return

            # 1. /api/classify
            if parsed.path == "/api/classify":
                text = data.get("text", "")
                result = classifier.classify(text)
                self._send_json(result)
                return

            # 2. /api/batch
            if parsed.path == "/api/batch":
                texts = data.get("texts", [])
                results = classifier.batch_classify(texts)
                self._send_json({"results": results})
                return

            # 3. /api/subanta/generate
            if parsed.path == "/api/subanta/generate":
                stem = data.get("stem", "")
                gender = data.get("gender", None)
                result = subanta_engine.generate_shabdarupa(stem, gender)
                self._send_json(result)
                return

            # 4. /api/subanta/analyze
            if parsed.path == "/api/subanta/analyze":
                pada = data.get("pada", "")
                result = subanta_engine.analyze_subanta(pada)
                self._send_json({"pada": pada, "analyses": result})
                return

            # 5. /api/subanta/prakriya
            if parsed.path == "/api/subanta/prakriya":
                stem = data.get("stem", "")
                gender = data.get("gender", None)
                v_idx = int(data.get("vibhakti_idx", 0))
                vac_idx = int(data.get("vacana_idx", 0))
                result = subanta_engine.derive_prakriya(stem, gender, v_idx, vac_idx)
                self._send_json(result)
                return

            # 6. /api/subanta/concordance
            if parsed.path == "/api/subanta/concordance":
                stem = data.get("stem", "")
                gender = data.get("gender", None)
                v_idx = int(data.get("vibhakti_idx", 0))
                vac_idx = int(data.get("vacana_idx", 0))
                result = quad_engine.generate_quad_concordance(stem, gender, v_idx, vac_idx)
                self._send_json(result)
                return

            # 7. /api/subanta/concordance_reverse
            if parsed.path == "/api/subanta/concordance_reverse":
                pada = data.get("pada", "")
                result = quad_engine.analyze_quad_concordance(pada)
                self._send_json(result)
                return

            # 8. /api/tinanta/generate — {root}. लट् only; see
            # _tinanta_generate_payload for why lakāra and pada are no
            # longer inputs.
            if parsed.path == "/api/tinanta/generate":
                root = data.get("root", "bhū")
                self._send_json(_tinanta_generate_payload(root))
                return

            # 8b. /api/tinanta/reverse — {word}. जयति → जि, and every
            # other root the दhātupāṭha's ~2,229 entries could make it
            # from.
            if parsed.path == "/api/tinanta/reverse":
                word = data.get("word", "")
                self._send_json(_tinanta_reverse_payload(word))
                return

            # 9. /api/tinanta/prakriya — {root, code?, purusha_idx,
            # vacana_idx}. One cell's full derivation on its own, for a
            # caller who already has the entry's dhātupāṭha `code` from
            # /api/tinanta/generate and does not want the whole table
            # again. `code` picks which entry where a name is ambiguous;
            # omitted, the first entry `entries_of_name` returns is used.
            if parsed.path == "/api/tinanta/prakriya":
                root = data.get("root", "bhū")
                code = data.get("code", "")
                p_idx = max(0, min(2, int(data.get("purusha_idx", 0))))
                v_idx = max(0, min(2, int(data.get("vacana_idx", 0))))
                result = _tinanta_generate_payload(root)
                entry = next(
                    (e for e in result.get("entries", [])
                     if not code or e["code"] == code), None)
                if entry is None:
                    self._send_json({"error": result.get(
                        "error", f"'{root}' is not a root the "
                        f"dhātupāṭha has.")})
                    return
                cell = entry["table"][p_idx]["forms"][v_idx]
                if cell.get("withheld"):
                    self._send_json({
                        "error": f"This slot is withheld — the engine "
                                 f"has no rule yet for it.",
                        "code": entry["code"],
                    })
                    return
                self._send_json({"code": entry["code"], **cell["derivation"]})
                return

            # 10. /api/krdanta/generate
            if parsed.path == "/api/krdanta/generate":
                root = data.get("root", "kṛ")
                affix = data.get("affix", "ktva")
                upasarga = data.get("upasarga", None)
                result = krdanta_engine.derive_krdanta(root, affix, upasarga)
                self._send_json(result)
                return

            # 11. /api/taddhita/generate
            if parsed.path == "/api/taddhita/generate":
                stem = data.get("stem", "dharma")
                affix = data.get("affix", "thak")
                result = krdanta_engine.derive_taddhita(stem, affix)
                self._send_json(result)
                return

            # 12. /api/verse/dependency_tree
            if parsed.path == "/api/verse/dependency_tree":
                verse = data.get("verse", "")
                result = verse_dependency_engine.build_dependency_tree(verse)
                self._send_json(result)
                return

            # 13. /api/dossier/export
            if parsed.path == "/api/dossier/export":
                pada = data.get("pada", "rāmaḥ")
                fmt = data.get("format", "markdown")
                result = dossier_exporter.export_subanta_dossier(pada, fmt)
                self._send_json(result)
                return

            # 14. /api/chandas/analyze
            if parsed.path == "/api/chandas/analyze":
                result = chandas_report(
                    data.get("text", ""),
                    script=data.get("script", "auto"),
                    boundary_mode=data.get("boundary_mode", "auto"),
                    tradition=data.get("tradition", "auto"),
                    include_near=bool(data.get("include_near", True)),
                )
                self._send_json(result)
                return

            self.send_response(404)
            self.end_headers()
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))

    def _send_html(self, html_str: str):
        payload = html_str.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(payload)
        self.wfile.flush()

    def _send_json(self, data: Any):
        payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(payload)
        self.wfile.flush()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


from socketserver import ThreadingMixIn

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
    # Python defaults this to 1, which sets SO_REUSEADDR. On Windows that flag
    # lets a SECOND process bind a port another process is already serving —
    # the bind succeeds silently, connections are split between the two, and
    # the port appears to hang. (On Unix SO_REUSEADDR only bypasses TIME_WAIT,
    # which is useful, so keep it there.) Turning it off on Windows makes a
    # duplicate launch fail loudly with WinError 10048 instead of wedging.
    allow_reuse_address = os.name != "nt"


def run_server(port=PORT):
    server_address = ("0.0.0.0", port)
    try:
        httpd = ThreadedHTTPServer(server_address, SanskritAPIHandler)
    except OSError as error:
        print(f"Could not bind port {port}: {error}")
        print("Another server.py is probably already running on this port.")
        print("List them with:  python server.py --who")
        raise SystemExit(1)
    print(f"============================================================")
    print(f"  Sanskrit Morphological & Subanta Server Running!")
    print(f"  Local Web App: http://127.0.0.1:{port}")
    print(f"  Classify API : http://127.0.0.1:{port}/api/classify?text=rāmaḥ")
    print(f"  Subanta API  : http://127.0.0.1:{port}/api/subanta/generate?stem=rāma")
    print(f"  Chandas API  : http://127.0.0.1:{port}/api/chandas/analyze?text=dharmakṣetre kurukṣetre")
    print(f"============================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")


def list_running_servers():
    """
    Lists every other running copy of this server. Windows lets a second
    process silently rebind a port that is already serving (see
    ThreadedHTTPServer.allow_reuse_address), so duplicates are easy to
    accumulate and hard to notice — this makes them visible.
    """
    import subprocess

    if os.name == "nt":
        query = (
            "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | "
            "Where-Object { $_.CommandLine -like '*server.py*' } | "
            "ForEach-Object { \"$($_.ProcessId)  $($_.CreationDate)\" }"
        )
        command = ["powershell", "-NoProfile", "-Command", query]
    else:
        command = ["pgrep", "-af", "server.py"]

    try:
        output = subprocess.run(
            command, capture_output=True, text=True, timeout=20
        ).stdout.strip()
    except Exception as error:
        print(f"Could not list processes: {error}")
        return

    rows = [line for line in output.splitlines() if line.strip()]
    if not rows:
        print("No server.py process is running.")
        return
    print(f"{len(rows)} server.py process(es) running:")
    for row in rows:
        print(f"  {row}")
    if len(rows) > 1:
        print("\nMore than one is running — that wedges the port. Keep exactly one.")


if __name__ == "__main__":
    if "--who" in sys.argv:
        list_running_servers()
    else:
        run_server()

