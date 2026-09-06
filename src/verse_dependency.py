"""
Sanskrit Verse Syntactic Dependency Tree & Visual Anvaya Graph Engine
====================================================================
Transforms continuous Sanskrit verses into:
1. Padaccheda & Morphological Token Stream
2. Kāraka Syntactic Dependency Graph (Nodes & Directed Edges)
3. Responsive SVG Diagram Renderer with sleek dark-mode glassmorphic aesthetics.
"""

from typing import Dict, Any, List, Optional, Tuple
import re
from .normalizer import devanagari_to_iast, iast_to_devanagari
from .anvaya import generate_anvaya
from .classifier import SanskritClassifier


class VerseDependencyEngine:
    """
    Constructs Kāraka dependency graphs and renders SVG trees from Sanskrit verses.
    """

    def __init__(self, classifier: Optional[SanskritClassifier] = None):
        self.classifier = classifier or SanskritClassifier()

    def build_dependency_tree(self, verse_text: str) -> Dict[str, Any]:
        """
        Decomposes verse and builds full Kāraka dependency tree data structure.
        """
        classified = self.classifier.classify(verse_text)
        token_results = classified.get("token_results", classified.get("tokens", []))
        raw_v = classified.get("input_text", verse_text)
        meter = classified.get("meter", "Anuṣṭubh (8-syllable quarter)")

        # Padaccheda & Token Extraction
        padas = []
        node_id_counter = 1

        nodes = []
        edges = []

        root_verb_id = None
        root_verb_text = None

        # Extract all constituent padas
        for tok in token_results:
            raw_w = tok.get("input_text", "").strip()
            padacheda_str = tok.get("padacheda", "")
            pred_cls = tok.get("predicted_class", "")

            if pred_cls in ("Sandhi Only", "Both") and " + " in padacheda_str:
                parts = [p.strip() for p in padacheda_str.split("(")[0].split("+") if p.strip()]
            else:
                parts = [tok.get("devanagari", raw_w)]

            for p_str in parts:
                p_clean = p_str.strip()
                if not p_clean:
                    continue
                p_iast = devanagari_to_iast(p_clean).lower().replace(":", "ḥ")

                # Determine syntactic category
                role, karaka_label, color = self._classify_pada_role(p_clean, p_iast)

                node_obj = {
                    "id": f"node_{node_id_counter}",
                    "text_devanagari": p_clean,
                    "text_iast": p_iast,
                    "role": role,
                    "karaka_label": karaka_label,
                    "color": color,
                    "is_verb": (role == "Kriyāpada (क्रियापदम् / Verb)")
                }
                nodes.append(node_obj)

                if node_obj["is_verb"] and not root_verb_id:
                    root_verb_id = node_obj["id"]
                    root_verb_text = p_clean

                node_id_counter += 1

        # Fallback implicit copula (asti) if no finite verb found
        if not root_verb_id:
            root_verb_id = f"node_{node_id_counter}"
            root_verb_text = "अस्ति (asti / implied)"
            nodes.append({
                "id": root_verb_id,
                "text_devanagari": "अस्ति [अध्याहृत]",
                "text_iast": "asti (implicit copula)",
                "role": "Kriyāpada (क्रियापदम् / Verb)",
                "karaka_label": "Adhyāhṛta Kriyā (2.3.46)",
                "color": "#ec4899",
                "is_verb": True
            })

        # Construct Edges linking to root verb or substantive
        subject_id = None
        for n in nodes:
            if n["id"] == root_verb_id:
                continue

            nid = n["id"]
            role = n["role"]

            if "Kartṛ" in role or "Subject" in role:
                subject_id = nid
                edges.append({
                    "from": root_verb_id,
                    "to": nid,
                    "relation": "Kartā (कर्ता / Subject)",
                    "sutra": "svatantraḥ kartā (1.4.54)",
                    "color": "#38bdf8"
                })
            elif "Karman" in role or "Object" in role:
                edges.append({
                    "from": root_verb_id,
                    "to": nid,
                    "relation": "Karma (कर्म / Object)",
                    "sutra": "karturīpsitatamaṃ karma (1.4.49)",
                    "color": "#fbbf24"
                })
            elif "Adhikaraṇa" in role or "Locus" in role or "Locative" in role:
                edges.append({
                    "from": root_verb_id,
                    "to": nid,
                    "relation": "Adhikaraṇa (अधिकरणम् / Locus)",
                    "sutra": "ādhāro'dhikaraṇam (1.4.45)",
                    "color": "#a78bfa"
                })
            elif "Karaṇa" in role or "Instrument" in role:
                edges.append({
                    "from": root_verb_id,
                    "to": nid,
                    "relation": "Karaṇa (करणम् / Instrument)",
                    "sutra": "sādhakatamaṃ karaṇam (1.4.42)",
                    "color": "#34d399"
                })
            elif "Pūrvakāla" in role or "Participle" in role:
                edges.append({
                    "from": root_verb_id,
                    "to": nid,
                    "relation": "Pūrvakāla-Kriyā (पूर्वकाल-क्रिया)",
                    "sutra": "samānakartṛkayoḥ pūrvakāle (3.4.21)",
                    "color": "#f472b6"
                })
            elif "Viśeṣaṇa" in role or "Modifier" in role:
                target = subject_id if subject_id else root_verb_id
                edges.append({
                    "from": target,
                    "to": nid,
                    "relation": "Viśeṣaṇa (विशेषणम् / Concord)",
                    "sutra": "viśeṣaṇaṃ viśeṣyanighnam",
                    "color": "#6ee7b7"
                })
            else:
                edges.append({
                    "from": root_verb_id,
                    "to": nid,
                    "relation": "Sambandha (सम्बन्ध / Relation)",
                    "sutra": "ṣaṣṭhī śeṣe (2.3.50)",
                    "color": "#94a3b8"
                })

        # Generate SVG visualization
        svg_code = self._generate_svg_tree(nodes, edges, raw_v, root_verb_id)

        # Anvaya prose sequence
        anvaya_res = generate_anvaya(token_results, raw_v)

        return {
            "verse_text": raw_v,
            "meter": meter,
            "root_verb": root_verb_text,
            "nodes": nodes,
            "edges": edges,
            "anvaya_prose": anvaya_res.get("anvaya_devanagari", ""),
            "anvaya_english": anvaya_res.get("translation_summary", ""),
            "svg_graph": svg_code
        }

    def _classify_pada_role(self, dev: str, iast: str) -> Tuple[str, str, str]:
        """Deduces Kāraka role and UI node color."""
        # 1. Finite Verbs
        if iast in ('uvāca', 'bravīti', 'akarot', 'akurvata', 'kurvanti', 'paśyati', 'tiṣṭhati', 'bhavati', 'santi', 'yotsye', 'avocata', 'yudhyasva', 'vande', 'abravīt', 'paśya', 'smara', 'nama', 'jahi', 'dehi', 'viduḥ', 'bhaviṣyati', 'abhavat', 'karoti', 'kuru', 'bhavatu') or dev in ('वन्दे', 'अकुर्वत', 'उवाच', 'अब्रवीत्', 'पश्य', 'कुरु', 'भवति', 'अस्ति', 'सन्ति'):
            return "Kriyāpada (क्रियापदम् / Verb)", "Pradhāna-Kriyā (Main Action)", "#ec4899"

        # 2. Prior participles (Ktvā / Lyap)
        if iast.endswith(('tvā', 'ya', 'tya')) and iast not in ('rāmāya', 'kṛṣṇāya'):
            return "Pūrvakāla-Kriyā (पूर्वकाल-क्रिया)", "Participle (3.4.21)", "#f472b6"

        # 3. Locatives / Place-Time
        if iast.endswith(('e', 'ṣu', 'su', 'i', 'yām', 'au')) and iast in ('dharmakṣetre', 'kurukṣetre', 'raṇe', 'saṅgrāme', 'yuddhe', 'kṣetre', 'dine'):
            return "Adhikaraṇa (अधिकरणम् / Locus)", "Ādhāra (1.4.45)", "#a78bfa"

        # 4. Subjects & Plural agents
        if iast.endswith(('aḥ', 'āḥ', 'vān', 'mān', 'ārau', 'āraḥ', 'inau', 'inaḥ')) or iast in ('māmakāḥ', 'pāṇḍavāḥ', 'sañjaya', 'dhṛtarāṣṭraḥ', 'yuyutsavaḥ', 'arjunaḥ', 'kṛṣṇaḥ'):
            if iast in ('samavetāḥ', 'samavetā', 'yuyutsavaḥ'):
                return "Kartṛ-Viśeṣaṇa (विशेषणम् / Subject Modifier)", "Concord (विशेष्यनिघ्न)", "#38bdf8"
            return "Kartṛ (कर्ता / Agent-Subject)", "Svatantra (1.4.54)", "#60a5fa"

        # 5. Objects (2nd case)
        if iast.endswith(('am', 'ān', 'īm', 'ūn', 'am')):
            return "Karman (कर्म / Direct Object)", "Īpsitatama (1.4.49)", "#fbbf24"

        # 6. Instruments (3rd case)
        if iast.endswith(('ena', 'eṇa', 'ayā', 'inā', 'iṇā', 'aiḥ', 'ābhiḥ', 'ebhiḥ')):
            return "Karaṇa (करणम् / Instrument)", "Sādhakatama (1.4.42)", "#34d399"

        # 7. Genitives (6th case)
        if iast.endswith(('asya', 'ayoḥ', 'ānām', 'āṇām', 'eḥ', 'oḥ', 'uḥ', 'tava', 'mama', 'me', 'te')):
            return "Sambandha (सम्बन्ध / Genitive Possessor)", "Śeṣe Ṣaṣṭhī (2.3.50)", "#94a3b8"

        return "Padam (पदम् / Syntactic Constituent)", "Subanta / Avyaya", "#cbd5e1"

    def _generate_svg_tree(self, nodes: List[Dict[str, Any]], edges: List[Dict[str, Any]], verse: str, root_id: str) -> str:
        """Generates clean, responsive SVG syntax tree diagram."""
        width = 850
        height = 420

        # Calculate node positions
        # Root verb at top center
        root_x = width // 2
        root_y = 65

        pos = {}
        pos[root_id] = (root_x, root_y)

        child_nodes = [n for n in nodes if n["id"] != root_id]
        n_count = len(child_nodes)

        # Distribute child nodes in an arc or grid below root
        if n_count > 0:
            step_x = (width - 120) / max(1, (n_count - 1)) if n_count > 1 else width // 2
            for idx, cn in enumerate(child_nodes):
                cx = 60 + idx * step_x if n_count > 1 else width // 2
                cy = 240 if idx % 2 == 0 else 320
                pos[cn["id"]] = (cx, cy)

        # Draw SVG elements
        svg_lines = []
        svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" class="anvaya-svg-canvas" style="width: 100%; height: auto; background: radial-gradient(circle at 50% 20%, rgba(30, 27, 75, 0.95), rgba(15, 23, 42, 0.98)); border-radius: 12px; border: 1px solid rgba(139, 92, 246, 0.25);">')
        
        # Defs: Arrow markers & filters
        svg_lines.append('''
        <defs>
          <linearGradient id="edgeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.8"/>
            <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.8"/>
          </linearGradient>
          <marker id="arrow" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/>
          </marker>
          <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="3" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
          </filter>
        </defs>
        ''')

        # Title header
        svg_lines.append(f'<text x="25" y="32" fill="#c4b5fd" font-size="13" font-family="system-ui, sans-serif" font-weight="600">🌳 PĀṆINIAN KĀRAKA SYNTACTIC DEPENDENCY TREE (अन्वय-कारक-वृक्षः)</text>')

        # Draw Edges (Bezier curves)
        for e in edges:
            u_id = e["from"]
            v_id = e["to"]
            if u_id in pos and v_id in pos:
                x1, y1 = pos[u_id]
                x2, y2 = pos[v_id]
                ctrl_y = (y1 + y2) / 2
                svg_lines.append(f'<path d="M {x1} {y1} C {x1} {ctrl_y}, {x2} {ctrl_y}, {x2} {y2}" stroke="{e.get("color", "#8b5cf6")}" stroke-width="2" fill="none" marker-end="url(#arrow)" opacity="0.85"/>')
                
                # Edge Label
                mid_x = (x1 + x2) / 2
                mid_y = (y1 + y2) / 2 - 6
                svg_lines.append(f'<rect x="{mid_x - 45}" y="{mid_y - 10}" width="90" height="18" rx="4" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(139, 92, 246, 0.3)" stroke-width="0.8"/>')
                svg_lines.append(f'<text x="{mid_x}" y="{mid_y + 3}" fill="{e.get("color", "#c4b5fd")}" font-size="9" font-family="system-ui" text-anchor="middle" font-weight="bold">{e["relation"].split()[0]}</text>')

        # Draw Nodes (Glassmorphic Cards)
        for n in nodes:
            nid = n["id"]
            if nid in pos:
                nx, ny = pos[nid]
                bg_col = n.get("color", "#8b5cf6")
                is_root = n.get("is_verb", False)
                w_box = 135 if is_root else 115
                h_box = 56 if is_root else 48
                rx_box = nx - w_box / 2
                ry_box = ny - h_box / 2

                # Card Rectangle
                border_glow = 'filter="url(#glow)" stroke="#f472b6"' if is_root else f'stroke="{bg_col}"'
                svg_lines.append(f'<rect x="{rx_box}" y="{ry_box}" width="{w_box}" height="{h_box}" rx="8" fill="rgba(30, 41, 59, 0.9)" {border_glow} stroke-width="1.8"/>')
                
                # Text: Devanagari Word
                svg_lines.append(f'<text x="{nx}" y="{ry_box + 20}" fill="#ffffff" font-size="{14 if is_root else 12}" font-family="system-ui, sans-serif" font-weight="bold" text-anchor="middle">{n["text_devanagari"]}</text>')
                # Text: Kāraka Role
                svg_lines.append(f'<text x="{nx}" y="{ry_box + 36}" fill="{bg_col}" font-size="9.5" font-family="system-ui" font-weight="600" text-anchor="middle">{n["karaka_label"]}</text>')

        svg_lines.append('</svg>')
        return '\n'.join(svg_lines)
