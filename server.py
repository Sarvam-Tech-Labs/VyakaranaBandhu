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
from src.tinanta_engine import TinantaEngine
from src.verse_dependency import VerseDependencyEngine
from src.dossier_exporter import DossierExporter
from src.chandas import chandas_report

# The Aṣṭādhyāyī codification. Imported lazily inside the handlers rather
# than here: loading it reads the corpus off disk, and a server started to
# classify one word should not pay for that.

# Static UI root: ui/ holds the Bhakta Bandhu design-system front end.
WEB_DIR = os.path.join(os.path.dirname(__file__), "ui")
PORT = 8000

# Initialize engines
classifier = SanskritClassifier()
subanta_engine = SubantaEngine()
quad_engine = QuadConcordanceEngine(subanta_engine)
krdanta_engine = KrdantaTaddhitaEngine()
tinanta_engine = TinantaEngine()
verse_dependency_engine = VerseDependencyEngine(classifier)
dossier_exporter = DossierExporter(subanta_engine, quad_engine)


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

            # 6. /api/tinanta/generate?root=...&lakara=...&pada=...
            if parsed.path == "/api/tinanta/generate":
                root = params.get("root", ["bhū"])[0]
                lakara = params.get("lakara", ["lat"])[0]
                pada = params.get("pada", ["parasmaipada"])[0]
                result = tinanta_engine.generate_conjugation(root, lakara, pada)
                self._send_json(result)
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

            # 8. /api/tinanta/generate
            if parsed.path == "/api/tinanta/generate":
                root = data.get("root", "bhū")
                lakara = data.get("lakara", "lat")
                pada = data.get("pada", "parasmaipada")
                result = tinanta_engine.generate_conjugation(root, lakara, pada)
                self._send_json(result)
                return

            # 9. /api/tinanta/prakriya
            if parsed.path == "/api/tinanta/prakriya":
                root = data.get("root", "bhū")
                lakara = data.get("lakara", "lat")
                pada = data.get("pada", "parasmaipada")
                p_idx = int(data.get("purusha_idx", 0))
                v_idx = int(data.get("vacana_idx", 0))
                result = tinanta_engine.derive_prakriya(root, lakara, pada, p_idx, v_idx)
                self._send_json(result)
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

