"""
Sanskrit Legal Brief & Quad-Tradition Sūtra Concordance Dossier Exporter
========================================================================
Exports courtroom-grade juridical briefs and 4-Pillar concordance reports into:
1. Formatted Markdown (.md)
2. Standalone Printable HTML (.html with modern styling & print CSS)
3. Structured JSON (.json)
"""

from typing import Dict, Any, List, Optional
import json
from .normalizer import devanagari_to_iast, iast_to_devanagari
from .subanta_engine import SubantaEngine
from .quad_concordance import QuadConcordanceEngine


class DossierExporter:
    """
    Exports comprehensive Sanskrit legal defense dossiers and 4-way concordance reports.
    """

    def __init__(self, subanta_engine: Optional[SubantaEngine] = None, quad_engine: Optional[QuadConcordanceEngine] = None):
        self.subanta_engine = subanta_engine or SubantaEngine()
        self.quad_engine = quad_engine or QuadConcordanceEngine(self.subanta_engine)

    def export_subanta_dossier(self, pada: str, export_format: str = "markdown") -> Dict[str, Any]:
        """
        Generates the full legal brief dossier for a target surface pada in the requested format.
        """
        analysis = self.quad_engine.analyze_quad_concordance(pada)
        p_clean = analysis["pada"]
        p_dev = iast_to_devanagari(p_clean)

        fmt = export_format.strip().lower()

        if fmt == "json":
            return {
                "pada": p_clean,
                "pada_devanagari": p_dev,
                "format": "json",
                "filename": f"dossier_{p_clean}.json",
                "content": json.dumps(analysis, ensure_ascii=False, indent=2)
            }

        if fmt == "html":
            html_content = self._generate_html_dossier(analysis, p_clean, p_dev)
            return {
                "pada": p_clean,
                "pada_devanagari": p_dev,
                "format": "html",
                "filename": f"dossier_{p_clean}.html",
                "content": html_content
            }

        # Default: Markdown
        md_content = self._generate_markdown_dossier(analysis, p_clean, p_dev)
        return {
            "pada": p_clean,
            "pada_devanagari": p_dev,
            "format": "markdown",
            "filename": f"dossier_{p_clean}.md",
            "content": md_content
        }

    def _generate_markdown_dossier(self, data: Dict[str, Any], p_clean: str, p_dev: str) -> str:
        """Generates structured Markdown courtroom brief."""
        lines = []
        lines.append(f"# ⚖️ PĀṆINIAN LEGAL DEFENSE & QUAD-TRADITION CONCORDANCE DOSSIER")
        lines.append(f"**Target Surface Pada:** `{p_dev}` (`{p_clean}`)\n")
        lines.append(f"**Jurisdiction:** Pāṇini Aṣṭādhyāyī • Mahābhāṣya • Bṛhat-Harināmāmṛta • Bāla-Toṣaṇī Ṭīkā\n")
        lines.append(f"**Total Legal Readings Substantiated:** {data['total_readings']}\n")
        lines.append("---\n")

        for idx, a in enumerate(data["analyses"], 1):
            ld = a.get("legal_defense", {})
            qc = a.get("quad_concordance", {})
            sg = ld.get("stem_grade", {})
            mb = ld.get("mahabhashya_dialectic", {})
            hnv = ld.get("hnv_lens", {})

            lines.append(f"## 🏛️ Reading {idx}/{data['total_readings']}: `{a['stem_devanagari']}` ({a['stem_iast']}) — {a['gender'].upper()}")
            lines.append(f"- **Grammatical Slot:** {a['vibhakti']} {a['vacana']}")
            lines.append(f"- **Stem Grade (Aṅga):** {sg.get('grade', 'Standard')}")
            lines.append(f"- **Kāraka Jurisdiction:** {ld.get('karaka_jurisdiction', 'N/A')}\n")

            lines.append(f"### 📜 Legal Plea (प्रतिज्ञा)")
            lines.append(f"> {ld.get('pratijna', '')}\n")

            lines.append(f"### 📖 Cited Pāṇinian Statutes & Precedents (पाणिनीय-सूत्र-प्रमाणम्)")
            lines.append("| Statute (सूत्रम्) | Type (प्रकारः) | Operational Function |")
            lines.append("| :--- | :--- | :--- |")
            for s in ld.get("statutes", []):
                lines.append(f"| **{s['sutra_dev']}**<br>*{s['sutra']}* | `{s['type']}` | {s['function']} |")
            lines.append("")

            if mb.get("purvapaksha"):
                lines.append(f"### 💬 Mahābhāṣya Dialectic (महाभाष्य-विचारः)")
                lines.append(f"- **Pūrvapakṣa (Objection):** {mb['purvapaksha']}")
                lines.append(f"- **Siddhānta (Patañjali's Verdict):** {mb['siddhanta']}\n")

            if hnv.get("narayana_base"):
                lines.append(f"### 🌸 Bṛhat-Harināmāmṛta & Bāla-Toṣaṇī Dimension (श्रीहरिनाममृत-दृष्टिः)")
                lines.append(f"- **Nārāyaṇa & Viṣṇubhakti:** {hnv['narayana_base']} + {hnv['visnubhakti']} ({hnv['bhakti_relationship']})")
                if hnv.get("bala_toshani_exegesis"):
                    lines.append(f"- **Bāla-Toṣaṇī Ṭīkā:** {hnv['bala_toshani_exegesis']}")
                lines.append(f"- **Smaraṇam:** *{hnv['philosophical_siddhanta']}*\n")

            lines.append(f"### 🔱 Quad-Tradition Sūtra Reconciliation Steps (चतुःशास्त्र-समन्वयः)")
            for st in qc.get("concordance_steps", []):
                lines.append(f"#### [Step {st['step']}] {st['stage']} ➔ `{st['intermediate_string']}`")
                lines.append(f"- **1. Pāṇini Aṣṭādhyāyī:** {st['p1_astadhyayi']['sutra']}")
                lines.append(f"- **2. Mahābhāṣya / Kaumudī:** {st['p2_mahabhashya']['jurisprudence']}")
                lines.append(f"- **3. Bṛhat-Harināmāmṛta:** {st['p3_harinamamrita']['sutra_principle']}")
                lines.append(f"- **4. Bāla-Toṣaṇī Ṭīkā:** {st['p4_bala_toshani']['exegesis']}")
                lines.append(f"- **⚖️ Samanvaya:** {st['reconciliation_verdict']}\n")

            lines.append(f"### ⚖️ Gender Jurisprudence (लिङ्ग-निर्णयः)")
            lines.append(f"{ld.get('gender_proof', '')}\n")

            lines.append(f"### ✅ Final Courtroom Verdict (निर्णयः)")
            lines.append(f"> **{ld.get('verdict', '')}**\n")
            lines.append("---\n")

        return "\n".join(lines)

    def _generate_html_dossier(self, data: Dict[str, Any], p_clean: str, p_dev: str) -> str:
        """Generates self-contained standalone printable HTML legal dossier."""
        md_text = self._generate_markdown_dossier(data, p_clean, p_dev)

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Legal Dossier — {p_dev} ({p_clean})</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800&family=Inter:wght@400;500;600;700&family=Yatra+One&display=swap');
    
    body {{
      font-family: 'Inter', system-ui, sans-serif;
      line-height: 1.6;
      color: #1e293b;
      background: #f8fafc;
      margin: 0;
      padding: 2rem;
    }}
    .dossier-container {{
      max-width: 860px;
      margin: 0 auto;
      background: #ffffff;
      padding: 3rem;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
      border: 1px solid #e2e8f0;
    }}
    h1, h2, h3, h4 {{
      color: #0f172a;
      font-family: 'Cinzel', serif;
    }}
    .devanagari {{
      font-family: 'Yatra One', serif;
      font-size: 1.25rem;
    }}
    .legal-seal {{
      text-align: center;
      margin-bottom: 2rem;
      padding-bottom: 1.5rem;
      border-bottom: 2px double #cbd5e1;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
      font-size: 0.9rem;
    }}
    th, td {{
      padding: 0.6rem 0.8rem;
      border: 1px solid #cbd5e1;
      text-align: left;
    }}
    th {{
      background: #f1f5f9;
      font-weight: 600;
    }}
    blockquote {{
      background: #f8fafc;
      border-left: 4px solid #3b82f6;
      margin: 1rem 0;
      padding: 0.8rem 1.2rem;
      color: #334155;
      font-style: italic;
    }}
    .verdict-box {{
      background: #ecfdf5;
      border: 2px solid #10b981;
      border-radius: 8px;
      padding: 1rem 1.2rem;
      font-weight: bold;
      color: #065f46;
      margin-top: 1.5rem;
    }}
    @media print {{
      body {{ background: #ffffff; padding: 0; }}
      .dossier-container {{ box-shadow: none; border: none; padding: 1.5cm; }}
      button {{ display: none; }}
    }}
  </style>
</head>
<body>
  <div class="dossier-container">
    <div class="legal-seal">
      <div style="font-size: 2.2rem;">⚖️ 🏛️ 🔱</div>
      <h1 style="margin: 0.5rem 0 0.2rem 0; font-size: 1.6rem;">PĀṆINIAN SANSKRIT JURISPRUDENCE COURT</h1>
      <p style="margin: 0; color: #64748b; font-size: 0.9rem;">High Council of Grammatical Jurisprudence & Quad-Tradition Concordance</p>
      <p style="margin: 0.4rem 0 0 0; font-weight: bold;">Formal Defense Dossier for Pada: <span class="devanagari">{p_dev}</span> ({p_clean})</p>
    </div>
    <div>
      <pre style="white-space: pre-wrap; font-family: inherit; font-size: 0.92rem; line-height: 1.65;">{md_text}</pre>
    </div>
    <div style="margin-top: 2rem; text-align: center;">
      <button onclick="window.print()" style="background: #2563eb; color: #ffffff; border: none; padding: 0.6rem 1.4rem; font-weight: bold; border-radius: 6px; cursor: pointer;">🖨️ Print / Save as PDF</button>
    </div>
  </div>
</body>
</html>"""
        return html
