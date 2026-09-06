"""
Interactive Command Line Interface for Sanskrit Morphological Classifier & Pāṇinian Subanta Engine
Supports single words, compound terms, complete multi-word verses, and Śabdarūpa generation & analysis.
"""

import sys
import argparse
from typing import Dict, Any, List, Optional
from src.classifier import SanskritClassifier
from src.subanta_engine import SubantaEngine
from src.chandas import chandas_report


def format_classification_result(res: dict):
    # 1. Whole Verse Format
    if res.get('is_verse'):
        print("\n" + "=" * 80)
        print(f"  FULL SANSKRIT VERSE / SHLOKA ANALYSIS")
        if res.get('meter'):
            print(f"  Metre   : {res['meter']}")
        print("-" * 80)
        print(f"  Original Text : {res['input_text']}")
        print(f"  IAST Script   : {res['iast']}")
        print("-" * 80)
        
        if res.get('anvaya'):
            print(f"  Syntactic Order (Anvaya) : {res['anvaya']}")
            print(f"  Anvaya (IAST)            : {res.get('anvaya_iast', '')}")
            print("-" * 80)

        if res.get('full_padacheda'):
            print(f"  Full Padacheda Pipeline  : {res['full_padacheda']}")
            
        if res.get('prakriti_pratyaya_pipeline'):
            print(f"  Prakṛti-Pratyaya Vibhāga : {res['prakriti_pratyaya_pipeline']}")
            
        print("-" * 80)
        dist = res.get('class_summary') or res.get('class_distribution', {})
        print(f"  Class Summary ({res['token_count']} Words/Compounds): "
              f"Samāsa Only: {dist.get('Samāsa Only', 0)} | "
              f"Sandhi Only: {dist.get('Sandhi Only', 0)} | "
              f"Both: {dist.get('Both', 0)} | "
              f"None: {dist.get('None', 0)}")
        print("=" * 80)
        
        print("\n  WORD-BY-WORD MORPHOLOGICAL DECOMPOSITION:")
        for idx, tok_res in enumerate(res.get('token_results', []), 1):
            print(f"\n  [{idx}/{res['token_count']}] Word: {tok_res['input_text']} ({tok_res['iast']})")
            print(f"      Category : {tok_res['predicted_class']} (Confidence: {tok_res['confidence']*100:.1f}%)")
            print(f"      Subtype  : {tok_res.get('subtype', 'N/A')}")
            if tok_res.get('padacheda'):
                print(f"      Padacheda: {tok_res['padacheda']}")
            if tok_res.get('samasa') and tok_res.get('samasa') != 'N/A':
                print(f"      Samāsa   : {tok_res['samasa']}")
            if tok_res.get('prakriti_pratyaya') and tok_res['prakriti_pratyaya'].get('formula_dev'):
                print(f"      Prakṛti-Pratyaya : {tok_res['prakriti_pratyaya']['formula_dev']} ({tok_res['prakriti_pratyaya']['formula_iast']})")
            if tok_res.get('sandhi_steps'):
                for s in tok_res['sandhi_steps']:
                    print(f"      {s}")

        # Prosody. The classifier result carries only the one-line metre label
        # (src/verse_analyzer stores meter_summary, not the full apparatus, so
        # /api/classify stays lean) — so re-scan here for the per-akṣara grid.
        # ~14 ms, and only on the CLI path.
        format_chandas_report(chandas_report(res['input_text']), compact=True)
        print("=" * 80 + "\n")
        return

    # 2. Single Token / Compound Word Format
    print("\n" + "=" * 75)
    print(f"  Input Text   : {res['input_text']}")
    print(f"  IAST Script  : {res['iast']}")
    print(f"  Devanagari   : {res['devanagari']}")
    print("-" * 75)
    
    pred_class = res['predicted_class']
    conf = res['confidence'] * 100
    
    print(f"  CATEGORY     : {pred_class} (Confidence: {conf:.1f}%)")
    print(f"  SUBTYPE      : {res.get('subtype', 'N/A')}")
    print(f"  SŪTRA        : {res.get('sutra', 'N/A')}")
    
    # Structured Morphological Breakdown
    print("-" * 75)
    print("  STRUCTURED DERIVATION & PIPELINE:")
    if res.get('padacheda'):
        print(f"    Padacheda : {res['padacheda']}")
    if res.get('samasa'):
        print(f"    Samāsa    : {res['samasa']}")
    if res.get('sandhi_steps'):
        for step in res['sandhi_steps']:
            print(f"    {step}")
    if res.get('meaning'):
        print(f"    Meaning   : \"{res['meaning']}\"")
        
    print("-" * 75)
    print(f"  Explanation  : {res['explanation']}")
    if res.get('deep_commentary'):
        print(f"  Commentary   : {res['deep_commentary']}")
    
    if res.get('splits'):
        print("-" * 75)
        print("  Morphological Split (Vichchhed Candidates):")
        for s in res['splits']:
            print(f"    • {s['left_iast']} ({s['left_dev']}) + {s['right_iast']} ({s['right_dev']})")
            print(f"      [{s['description']}]")
            
    if res.get('ml_probabilities'):
        print("-" * 75)
        print("  ML Probability Distribution:")
        for cls, prob in sorted(res['ml_probabilities'].items(), key=lambda x: x[1], reverse=True):
            bar = "█" * int(prob * 25)
            print(f"    {cls:<14}: {prob*100:5.1f}%  {bar}")
            
    print("=" * 75 + "\n")


def format_shabdarupa_matrix(res: dict):
    """Formats and prints the 8x3 Śabdarūpa table."""
    print("\n" + "=" * 90)
    print(f"  PĀṆINIAN ŚABDARŪPA (SUBANTA) DECLENSION MATRIX")
    print(f"  Stem (Prātipadika) : {res['stem_devanagari']} ({res['stem_iast']})")
    print(f"  Gender (Liṅga)     : {res['gender'].capitalize()} | Paradigm: {res['paradigm']}")
    print("=" * 90)
    print(f"  {'Case (Vibhakti)':<30} | {'Singular (एकवचनम्)':<18} | {'Dual (द्विवचनम्)':<16} | {'Plural (बहुवचनम्)':<16}")
    print("-" * 90)
    for row in res["table"]:
        v_name = row["vibhakti"].split(" - ")[0].strip()
        cells = row["forms"]
        s_dev = f"{cells[0]['devanagari']} ({cells[0]['iast']})" if cells[0]['iast'] != '-' else '-'
        d_dev = f"{cells[1]['devanagari']} ({cells[1]['iast']})" if cells[1]['iast'] != '-' else '-'
        p_dev = f"{cells[2]['devanagari']} ({cells[2]['iast']})" if cells[2]['iast'] != '-' else '-'
        print(f"  {v_name:<30} | {s_dev:<18} | {d_dev:<16} | {p_dev:<16}")
    print("=" * 90 + "\n")


def format_subanta_analysis(pada: str, analyses: list):
    """Formats reverse Subanta morphological analysis results with Sanskrit legal defense."""
    print("\n" + "=" * 80)
    print(f"  PĀṆINIAN JURISPRUDENCE & REVERSE SUBANTA ANALYSIS (पाणिनीय-शास्त्रार्थ-प्रमाणम्)")
    print(f"  Target Surface Pada : {pada}")
    print("=" * 80)
    if not analyses:
        print(f"  No direct nominal subanta declensions found for '{pada}'.")
    else:
        for idx, a in enumerate(analyses, 1):
            ld = a.get('legal_defense', {})
            sg = ld.get('stem_grade', {})
            mb = ld.get('mahabhashya_dialectic', {})
            
            print(f"\n  ⚖️ [Reading {idx}/{len(analyses)}] LEGAL DEFENSE BRIEF:")
            print(f"      • Prātipadika (Base) : {a['stem_devanagari']} ({a['stem_iast']})")
            print(f"      • Gender (Liṅga)     : {a['gender'].capitalize()}")
            print(f"      • Grammatical Slot   : {a['vibhakti']} {a['vacana']}")
            if sg:
                print(f"      • Stem-Grade (Aṅga)  : {sg.get('grade', 'N/A')} [{sg.get('sutra', '')}]")
            print(f"      • Applied Sūtra      : {a.get('sutra', 'N/A')}")
            
            if ld:
                print(f"\n      📜 LEGAL PLEA (प्रतिज्ञा):")
                print(f"         {ld.get('pratijna', '')}")
                print(f"\n      🏛️ STATUTORY JURISDICTION (अधिकार एवं कारक-विधानम्):")
                print(f"         • Base Validity : {ld.get('base_authority', '')}")
                print(f"         • Kāraka Role   : {ld.get('karaka_jurisdiction', '')}")
                
                print(f"\n      📖 CITED STATUTES (पाणिनीय-सूत्र-प्रमाणम्):")
                for s in ld.get('statutes', []):
                    print(f"         § {s['sutra_dev']} | {s['sutra']}")
                    print(f"           - Type     : {s['type']}")
                    print(f"           - Function : {s['function']}")
                    
                if mb:
                    print(f"\n      💬 MAHĀBHĀṢYA DIALECTIC (महाभाष्य-विचारः):")
                    print(f"         • Pūrvapakṣa (Objection) : {mb.get('purvapaksha', '')}")
                    print(f"         • Siddhānta (Conclusion) : {mb.get('siddhanta', '')}")
                    
                hnv = ld.get('hnv_lens', {})
                if hnv:
                    print(f"\n      🌸 HARINĀMĀMṚTA-VYĀKARAṆA & BĀLA-TOṢAṆĪ VIEW (श्रीहरिनाममृत-बालतोषणी-दृष्टिः):")
                    print(f"         • Nārāyaṇa (Base)    : {hnv.get('narayana_base', '')} [{hnv.get('stem_classification', '')}]")
                    print(f"         • Viṣṇubhakti (Case) : {hnv.get('visnubhakti', '')} -> {hnv.get('bhakti_relationship', '')}")
                    print(f"         • Viṣṇupada (Word)   : {hnv.get('realized_visnupada', '')}")
                    if hnv.get('bala_toshani_exegesis'):
                        print(f"         • Bāla-Toṣaṇī Ṭīkā   : {hnv.get('bala_toshani_exegesis', '')}")
                    print(f"         • Smaraṇam / Meaning : {hnv.get('philosophical_siddhanta', '')}")

                print(f"\n      ⚖️ GENDER JURISPRUDENCE & DOCTRINE (लिङ्ग-निर्णयः):")
                print(f"         {ld.get('gender_proof', '')}")
                
                print(f"\n      ✅ FINAL VERDICT (निर्णयः):")
                print(f"         {ld.get('verdict', '')}")
            print("-" * 80)
    print("=" * 80 + "\n")


def format_prakriya_derivation(res: dict):
    sg = res.get('stem_grade', {})
    hnv = res.get('hnv_prakriya', {})
    print("\n" + "=" * 80)
    print(f"  PĀṆINIAN SUBANTA PRAKRIYĀ (DERIVATION TRACE)")
    print("=" * 80)
    print(f"  Surface Pada        : {res['final_pada_devanagari']} ({res['final_pada_iast']})")
    print(f"  Prātipadika (Base)  : {res['stem_devanagari']} ({res['stem_iast']}) [{res['gender'].capitalize()}]")
    print(f"  Grammatical Slot    : {res['vibhakti']} {res['vacana']}")
    if sg:
        print(f"  Stem Grade (Aṅga)   : {sg.get('grade', 'N/A')} [{sg.get('sutra', '')}]")
    print(f"  Raw SUP Affix       : {res['raw_sup_dev']} ({res['raw_sup']}) [Pāṇini 4.1.2]")
    print("-" * 80)
    print(f"  Syntactic Kāraka    : {res['karaka_info']['role']}")
    print(f"  Kāraka Sūtra        : {res['karaka_info']['sutra']}")
    print(f"  Semantic Meaning    : {res['karaka_info']['meaning']}")
    
    if hnv:
        print("-" * 80)
        print("  🌸 BṚHAT-HARINĀMĀMṚTA-VYĀKARAṆA & BĀLA-TOṢAṆĪ LENS (श्रीहरिनाममृत-बालतोषणी-प्रक्रिया):")
        print(f"    • Nārāyaṇa & Stem  : {hnv.get('narayana_base', '')} [{hnv.get('stem_nature', '')}]")
        print(f"    • Viṣṇubhakti      : {hnv.get('visnubhakti_affix', '')} [{hnv.get('visnubhakti_category', '')}]")
        print(f"    • Devotional Role  : {hnv.get('bhakti_relationship', '')}")
        print(f"    • Saṅketa / Lopa   : {hnv.get('sanketa_operation', '')}")
        print(f"    • Realized Pada    : {hnv.get('completed_visnupada', '')}")
        if hnv.get('bala_toshani_exegesis'):
            print(f"    • Bāla-Toṣaṇī Note : {hnv.get('bala_toshani_exegesis', '')}")
        
    print("-" * 80)
    print("  CHRONOLOGICAL SŪTRA DERIVATION STEPS:")
    for st in res.get('derivation_steps', []):
        print(f"\n  [Step {st['step']}] {st['stage']}")
        print(f"    • Operational Regime  : {st.get('regime', 'Sapādasaptādhyāyī')}")
        print(f"    • Intermediate String : {st['string']}")
        print(f"    • Applied Sūtra       : {st['sutra']} [{st['rule_type']}]")
        print(f"    • Rule Operation      : {st['explanation']}")
    print("\n" + "=" * 80 + "\n")


def format_quad_concordance(res: dict):
    print("\n" + "=" * 90)
    print("  🔱 EKAM SAT VIPRĀ BAHUDHĀ VADANTI — QUAD-TRADITION SŪTRA CONCORDANCE 🔱")
    print("  (चतुःशास्त्र-समन्वय-प्रणाली / Pāṇini • Mahābhāṣya • Harināmāmṛta • Bāla-Toṣaṇī)")
    print("=" * 90)
    print(f"  Surface Pada        : {res['final_pada_devanagari']} ({res['final_pada_iast']})")
    print(f"  Base Stem (Nārāyaṇa): {res['stem_devanagari']} ({res['stem_iast']}) [{res['gender'].capitalize()}]")
    print(f"  Grammatical Slot    : {res['vibhakti']} {res['vacana']}")
    print(f"  Raw Affix (Bhakti)  : {res['raw_sup']}")
    print(f"  Kāraka Jurisdiction : {res['karaka_role']}")
    print(f"  Bhakti Relationship : {res['bhakti_relationship']}")
    print("-" * 90)
    print("  STEP-BY-STEP 4-PILLAR RECONCILIATION:")

    for st in res.get("concordance_steps", []):
        print(f"\n  [Step {st['step']}] {st['stage']} ➔ Result: {st['intermediate_string']}")
        print(f"    ├─ 1. Pāṇini Aṣṭādhyāyī      : {st['p1_astadhyayi']['sutra']} [{st['p1_astadhyayi']['type']}]")
        print(f"    ├─ 2. Mahābhāṣya / Kaumudī   : {st['p2_mahabhashya']['jurisprudence']} ({st['p2_mahabhashya']['stem_grade']})")
        print(f"    ├─ 3. Bṛhat-Harināmāmṛta     : {st['p3_harinamamrita']['sutra_principle']}")
        print(f"    ├─ 4. Bāla-Toṣaṇī Ṭīkā       : {st['p4_bala_toshani']['exegesis']}")
        print(f"    └─ ⚖️ SAMANVAYA RECONCILIATION: {st['reconciliation_verdict']}")

    print("-" * 90)
    print(f"  📜 {res['grand_verdict']}")
    print("=" * 90 + "\n")


def format_tinanta_matrix(res: Dict[str, Any]):
    print("\n" + "=" * 80)
    print(f"  PĀṆINIAN TIṄANTA CONJUGATION MATRIX (तिङन्त-रूपाणि)")
    print("=" * 80)
    print(f"  Verbal Root (Dhātu) : {res['root_devanagari']} ({res['root_iast']}) — {res['root_meaning']} [{res['root_gana']}]")
    print(f"  Lakāra (Tense/Mood) : {res['lakara_name']}")
    print(f"  Voice / Pada        : {res['pada_type']}")
    print(f"  Pāṇini Statute      : {res['sutra_panini']}")
    print(f"  Harināmāmṛta Sūtra  : {res['sutra_hnv']}")
    print("-" * 80)
    print(f"  {'Puruṣa (Person)':<26} | {'Ekavacana (Sing.)':<16} | {'Dvivacana (Dual)':<16} | {'Bahuvacana (Plural)':<16}")
    print("-" * 80)
    for row in res["table"]:
        p_name = row["purusha_short"] + " Person"
        cells = [f"{c['devanagari']} ({c['iast']})" for c in row["forms"]]
        print(f"  {p_name:<26} | {cells[0]:<16} | {cells[1]:<16} | {cells[2]:<16}")
    print("=" * 80 + "\n")


def format_krdanta_derivation(res: Dict[str, Any]):
    print("\n" + "=" * 80)
    print(f"  KṚDANTA DERIVATION (कृदन्त-प्रक्रिया - PRIMARY VERBAL DERIVATIVE)")
    print("=" * 80)
    up_info = f" + Upasarga '{res['upasarga']}'" if res.get('upasarga') else ""
    print(f"  Base Dhātu    : {res['root_devanagari']} ({res['root_iast']}){up_info} [{res['root_gana']}]")
    print(f"  Kṛt Affix     : {res['affix_name']} ({res['affix_category']})")
    print(f"  Derived Word  : {res['derived_stem_devanagari']} ({res['derived_stem_iast']})")
    print(f"  Semantic Role : {res['semantic_meaning']}")
    print(f"  Pāṇini Sūtra  : {res['sutra_panini']}")
    print(f"  HNV / Ṭīkā    : {res['sutra_hnv']}")
    print(f"  Exegesis      : {res['tika_exegesis']}")
    print("-" * 80)
    print("  DERIVATION STEPS:")
    for st in res["derivation_steps"]:
        print(f"  [Step {st['step']}] {st['stage']} ➔ {st['form']}")
        print(f"    • Statute: {st['sutra']}")
        print(f"    • Detail : {st['desc']}")
    print("=" * 80 + "\n")


def format_taddhita_derivation(res: Dict[str, Any]):
    print("\n" + "=" * 80)
    print(f"  TADDHITĀNTA DERIVATION (तद्धितान्त-प्रक्रिया - SECONDARY NOMINAL DERIVATIVE)")
    print("=" * 80)
    print(f"  Prātipadika   : {res['base_stem_devanagari']} ({res['base_stem_iast']})")
    print(f"  Taddhita Affix: {res['affix_name']} ({res['affix_category']})")
    print(f"  Derived Stem  : {res['derived_stem_devanagari']} ({res['derived_stem_iast']})")
    print(f"  Semantic Role : {res['semantic_meaning']}")
    print(f"  Pāṇini Sūtra  : {res['sutra_panini']}")
    print(f"  HNV / Ṭīkā    : {res['sutra_hnv']}")
    print(f"  Exegesis      : {res['tika_exegesis']}")
    print("-" * 80)
    print("  DERIVATION STEPS:")
    for st in res["derivation_steps"]:
        print(f"  [Step {st['step']}] {st['stage']} ➔ {st['form']}")
        print(f"    • Statute: {st['sutra']}")
        print(f"    • Detail : {st['desc']}")
    print("=" * 80 + "\n")


def format_verse_dependency(res: Dict[str, Any]):
    print("\n" + "=" * 80)
    print(f"  🌳 PĀṆINIAN KĀRAKA SYNTACTIC DEPENDENCY GRAPH (अन्वय-कारक-सम्बन्धः)")
    print("=" * 80)
    print(f"  Target Verse      : {res['verse_text']}")
    print(f"  Root Finite Verb  : {res['root_verb']}")
    print(f"  Syntactic Anvaya  : {res['anvaya_prose']}")
    print(f"  English Meaning   : {res['anvaya_english']}")
    print("-" * 80)
    print("  KĀRAKA DIRECTED EDGES & RELATIONS:")
    for e in res["edges"]:
        print(f"  • {res['root_verb']} ──[{e['relation']}]──> Node ({e['to']}) | Statute: {e['sutra']}")
    print("=" * 80 + "\n")


def format_chandas_report(res: Dict[str, Any], compact: bool = False):
    """
    Prints the chandas apparatus. `compact` trims it to the metre line, the
    scansion grid, and the verification stamp — used when this is one section
    inside the already-long full-verse report, where the rule legend, authority
    pairs, and runner-up candidates would drown everything else. The
    --chandas flag prints the whole thing.
    """
    if compact:
        print("-" * 80)
        print("  CHANDAS — AKṢARA SCANSION (छन्दः)")
    else:
        print("\n" + "=" * 80)
        print(f"  CHANDAS — AKṢARA SCANSION & METRE IDENTIFICATION (छन्दः-शास्त्रम्)")
        print("=" * 80)

    if not res.get("ok"):
        print("  The text could not be scanned.")
        seen = set()
        for d in res.get("diagnostics", []):
            if not isinstance(d, dict) or d.get("severity") != "error":
                continue
            if d["message"] in seen:
                continue
            seen.add(d["message"])
            print(f"  • {d['message']}")
        print(("-" if compact else "=") * 80 + ("" if compact else "\n"))
        return

    meter = res.get("meter") or {}
    primary = meter.get("primary")
    totals = res.get("totals", {})

    print(f"  Metre            : {meter.get('label', 'unidentified')}")
    print(f"  Verdict Grade    : {meter.get('status')}  "
          f"(matched against {meter.get('catalog_size')} rules)")
    print(f"  Input Script     : {res.get('script')} | Pāda boundaries: {res.get('boundary_mode')}")
    pada_count = totals.get('padas', 0)
    print(f"  Totals           : {pada_count} pāda{'' if pada_count == 1 else 's'} | "
          f"{totals.get('syllables')} akṣaras | "
          f"{totals.get('guru')} guru + {totals.get('laghu')} laghu | {totals.get('matras')} mātrās")

    if primary and not compact:
        classification = primary.get("classification") or {}
        print("-" * 80)
        print(f"  System           : {classification.get('system_label', '')}")
        count_class = classification.get("count_class")
        if count_class:
            print(f"  Count Class      : {count_class.get('name')} — "
                  f"{count_class.get('syllables_per_pada')} akṣara per pāda")
        if classification.get("symmetry"):
            print(f"  Symmetry         : {classification['symmetry']}")
        if classification.get("gana_formula"):
            print(f"  Gaṇa Formula     : {classification['gana_formula']}")
        if classification.get("yati_statement"):
            print(f"  Yati             : {classification['yati_statement']}")
        if primary.get("template"):
            print(f"  Template         : {primary['template']}")
        source = primary.get("source") or {}
        if source:
            print(f"  Source           : {source.get('work')} — {source.get('locator')}")
        if primary.get("subtypes"):
            print(f"  Subtypes         : {' | '.join(primary['subtypes'])}")

    # Per-pāda scansion: one line of syllables, one of weights, aligned.
    print("-" * 80)
    print("  AKṢARA SCANSION (— = guru / heavy, ◡ = laghu / light, * = pāda-final anceps):")
    # Yati — the caesura the cited source prescribes. Only drawn from an
    # exactly-matching, independently verified candidate that records one;
    # absence means the tradition prescribes no break, not that it is unknown.
    yatis = []
    if (
        primary
        and primary.get("yati")
        and primary.get("match_type") == "exact"
        and meter.get("status") in ("identified", "provisional")
        and res.get("verification", {}).get("meter", {}).get("status") == "verified"
    ):
        yatis = sorted({y for y in primary["yati"] if isinstance(y, int) and y > 0})

    # Rows follow the metre's own pādas when its evidence tiles the verse, so
    # the yati lands in the same column on every row.
    rows = []
    flat = [s for pada in res.get("padas", []) for s in pada["syllables"]]
    if primary and primary.get("padas"):
        cursor = 0
        for evidence in sorted(primary["padas"], key=lambda e: e["pada_index"]):
            if evidence["syllable_start"] != cursor:
                rows = []
                break
            rows.append(flat[evidence["syllable_start"]:evidence["syllable_end"]])
            cursor = evidence["syllable_end"]
        if cursor != len(flat):
            rows = []
    metre_aligned = bool(rows)
    if not rows:
        rows = [pada["syllables"] for pada in res.get("padas", [])]
    label = "Pāda" if metre_aligned else "Unit"
    if metre_aligned and len(rows) != len(res.get("padas", [])):
        print(f"  (rows are the metre's {len(rows)} pādas, read inside the "
              f"{len(res.get('padas', []))} line(s) you supplied)")

    # One column width across every row, so beat N lines up down the column
    # and the yati falls in the same place on each line.
    width = max(
        (len(s["iast"]) + (1 if s["anceps"] else 0) for row in rows for s in row),
        default=1,
    )

    for index, syllables in enumerate(rows):
        cells = [s["iast"] + ("*" if s["anceps"] else "") for s in syllables]
        marks = ["—" if s["weight"] == "guru" else "◡" for s in syllables]
        pattern = "".join("G" if s["weight"] == "guru" else "L" for s in syllables)
        matras = sum(s["matras"] for s in syllables)

        def lay(items):
            out = []
            for position, item in enumerate(items):
                if position in yatis:
                    out.append("‖")
                out.append(f"{item:<{width}}")
            return " ".join(out)

        print(f"\n  {label} {index + 1}  [{pattern}]  "
              f"{len(syllables)} akṣara · {matras} mātrā")
        print("    " + lay(cells))
        print("    " + lay(marks))

    if yatis:
        positions = " and ".join(str(y) for y in yatis)
        print(f"\n  ‖ yati — the caesura the cited source prescribes, after syllable "
              f"{positions}. Word-boundary fit is not checked.")

    # Why each syllable scanned as it did — the rules actually used here.
    used = []
    for pada in res.get("padas", []):
        for s in pada["syllables"]:
            if s["rule"] not in used:
                used.append(s["rule"])
    rules = res.get("rules", {})
    if used and not compact:
        print("-" * 80)
        print("  DECIDING RULES USED:")
        for key in used:
            rule = rules.get(key, {})
            print(f"  • {key:<14} {rule.get('plain', '')}")
            print(f"    {'':<14} [{rule.get('sutra', '')}]")

    if primary and primary.get("notes") and not compact:
        print("-" * 80)
        for note in primary["notes"]:
            print(f"  Note: {note}")

    authority = (primary or {}).get("authority") or {}
    if authority.get("pairs") and not compact:
        print("-" * 80)
        print("  AUTHORITY (mūla + bhāṣya):")
        for pair in authority["pairs"]:
            root, bhasya = pair["root"], pair["bhasya"]
            print(f"  • {pair['label']} [{pair['tradition']}]")
            print(f"      Mūla   : {root['author']}, {root['work']} {root['locator']}")
            print(f"               \"{root['statement']}\"")
            print(f"      Bhāṣya : {bhasya['author']}, {bhasya['work']} {bhasya['locator']}")
            print(f"               \"{bhasya['statement']}\"")
    elif authority.get("note") and not compact:
        print("-" * 80)
        print(f"  Authority        : {authority.get('coverage')} — {authority['note']}")

    others = (meter.get("candidates") or [])[1:]
    if others and not compact:
        print("-" * 80)
        print("  OTHER CANDIDATES (diagnostics only — a near match is never a verdict):")
        for c in others[:6]:
            print(f"  • {c['name']:<28} {c['match_type']:<18} distance {c['distance']:<3} "
                  f"[{c['evidence']}]")

    for message in meter.get("diagnostics", []):
        print(f"\n  ! {message}")

    verification = res.get("verification", {})
    analysis_v = verification.get("analysis", {})
    meter_v = verification.get("meter", {})
    print("-" * 80)
    ok = analysis_v.get("status") == "verified" and meter_v.get("status") == "verified"
    print(f"  Verification     : scansion {analysis_v.get('status')} "
          f"({analysis_v.get('checks')} checks over {analysis_v.get('checked_syllables')} syllables) "
          f"| metre {meter_v.get('status')} ({meter_v.get('checks')} checks)"
          f"{'' if ok else '  <-- VERDICT SUPPRESSED'}")
    print(("-" if compact else "=") * 80 + ("" if compact else "\n"))


def interactive_mode(classifier: SanskritClassifier, subanta_engine: SubantaEngine, quad_engine: Any, krdanta_engine: Any, tinanta_engine: Any, verse_dep_engine: Any, dossier_exporter: Any):
    print("\n" + "=" * 75)
    print("      SANSKRIT GRAMMAR TOOLKIT (CLI)")
    print("      • Classify words / verses")
    print("      • Type ':shabda <stem> [gender]' for Śabdarūpa matrix")
    print("      • Type ':subanta <pada>' for reverse morphological lookup")
    print("      • Type ':tinanta <root> [lakara] [pada]' for verbal conjugation")
    print("      • Type ':krdanta <root> <affix> [upasarga]' for Kṛt derivatives")
    print("      • Type ':taddhita <stem> <affix>' for Taddhita derivatives")
    print("      • Type ':tree <verse>' for Kāraka dependency graph")
    print("      • Type ':chandas <verse>' for akṣara scansion and metre")
    print("      • Type ':export <pada> [markdown|html|json]' for legal dossier")
    print("      • Type ':concordance <stem> [gender] [v_idx] [vac_idx]' for 4-Way Concordance")
    print("      • Type 'exit' or 'quit' to quit")
    print("=" * 75)
    
    while True:
        try:
            user_input = input("\nEnter Sanskrit input > ").strip()
            if user_input.lower() in ('exit', 'quit', 'q'):
                print("Exiting. Namaste!")
                break
            if not user_input:
                continue

            if user_input.startswith(':chandas '):
                verse = user_input[9:].strip()
                format_chandas_report(chandas_report(verse))
            elif user_input.startswith(':tinanta ') or user_input.startswith(':t '):
                parts = user_input.split()
                root = parts[1]
                lak = parts[2] if len(parts) > 2 else "lat"
                pada = parts[3] if len(parts) > 3 else "parasmaipada"
                res = tinanta_engine.generate_conjugation(root, lak, pada)
                format_tinanta_matrix(res)
            elif user_input.startswith(':krdanta ') or user_input.startswith(':k '):
                parts = user_input.split()
                root = parts[1]
                aff = parts[2] if len(parts) > 2 else "ktva"
                up = parts[3] if len(parts) > 3 else None
                res = krdanta_engine.derive_krdanta(root, aff, up)
                format_krdanta_derivation(res)
            elif user_input.startswith(':taddhita ') or user_input.startswith(':td '):
                parts = user_input.split()
                stem = parts[1]
                aff = parts[2] if len(parts) > 2 else "thak"
                res = krdanta_engine.derive_taddhita(stem, aff)
                format_taddhita_derivation(res)
            elif user_input.startswith(':tree '):
                v_text = user_input[6:].strip()
                res = verse_dep_engine.build_dependency_tree(v_text)
                format_verse_dependency(res)
            elif user_input.startswith(':export '):
                parts = user_input.split()
                pada = parts[1]
                fmt = parts[2] if len(parts) > 2 else "markdown"
                res = dossier_exporter.export_subanta_dossier(pada, fmt)
                print(f"\n[Dossier Exported successfully: {res['filename']}]\n")
                if fmt != "html":
                    print(res["content"])
            elif user_input.startswith(':concordance ') or user_input.startswith(':c '):
                parts = user_input.split()
                stem = parts[1]
                gender = parts[2] if len(parts) > 2 and not parts[2].isdigit() else None
                v_idx = int(parts[3]) if len(parts) > 3 and parts[3].isdigit() else (int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 0)
                vac_idx = int(parts[4]) if len(parts) > 4 and parts[4].isdigit() else (int(parts[3]) if len(parts) > 3 and parts[3].isdigit() else 0)
                res = quad_engine.generate_quad_concordance(stem, gender, v_idx, vac_idx)
                format_quad_concordance(res)
            elif user_input.startswith(':shabda ') or user_input.startswith(':s '):
                parts = user_input.split()
                stem = parts[1]
                gender = parts[2] if len(parts) > 2 else None
                res = subanta_engine.generate_shabdarupa(stem, gender)
                format_shabdarupa_matrix(res)
            elif user_input.startswith(':subanta ') or user_input.startswith(':a '):
                parts = user_input.split()
                pada = parts[1]
                res = subanta_engine.analyze_subanta(pada)
                format_subanta_analysis(pada, res)
            elif user_input.startswith(':derive ') or user_input.startswith(':d '):
                parts = user_input.split()
                stem = parts[1]
                gender = parts[2] if len(parts) > 2 and not parts[2].isdigit() else None
                v_idx = int(parts[3]) if len(parts) > 3 and parts[3].isdigit() else (int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 0)
                vac_idx = int(parts[4]) if len(parts) > 4 and parts[4].isdigit() else (int(parts[3]) if len(parts) > 3 and parts[3].isdigit() else 0)
                res = subanta_engine.derive_prakriya(stem, gender, v_idx, vac_idx)
                format_prakriya_derivation(res)
            else:
                res = classifier.classify(user_input)
                format_classification_result(res)
            
        except (KeyboardInterrupt, EOFError):
            print("\nExiting. Namaste!")
            break


def main():
    from src.quad_concordance import QuadConcordanceEngine
    from src.krdanta_taddhita import KrdantaTaddhitaEngine
    from src.tinanta_engine import TinantaEngine
    from src.verse_dependency import VerseDependencyEngine
    from src.dossier_exporter import DossierExporter

    parser = argparse.ArgumentParser(description="Sanskrit Morphological Classifier & Pāṇinian Subanta/Tiṅanta/Kṛdanta Engine")
    parser.add_argument("text", nargs="?", type=str, help="Sanskrit text or full verse to classify")
    parser.add_argument("--batch", "-b", nargs="+", help="Classify multiple words")
    parser.add_argument("--shabda", "-s", type=str, help="Generate 8x3 Śabdarūpa table for a nominal stem (prātipadika)")
    parser.add_argument("--linga", "-l", type=str, default=None, help="Gender for Śabdarūpa (masculine/feminine/neuter)")
    parser.add_argument("--analyze-subanta", "-a", type=str, help="Reverse-analyze an inflected nominal pada")
    parser.add_argument("--derive", "-d", type=str, help="Derive step-by-step Pāṇinian Prakriyā for a nominal stem (e.g. 'rāma')")
    parser.add_argument("--concordance", "-q", type=str, help="Generate 4-Pillar Quad-Tradition Concordance for stem")
    parser.add_argument("--vibhakti-idx", "-v", type=int, default=0, help="Vibhakti index (0..7) for --derive / --concordance")
    parser.add_argument("--vacana-idx", "-c", type=int, default=0, help="Vacana index (0..2) for --derive / --concordance")
    parser.add_argument("--tinanta", "-t", type=str, help="Generate verbal conjugation matrix for a verbal root (dhātu, e.g. 'bhū', 'kṛ')")
    parser.add_argument("--lakara", "-k", type=str, default="lat", help="Lakāra for --tinanta (lat, lit, lut, lrt, lot, lan, vidhilin, etc.)")
    parser.add_argument("--pada-type", "-p", type=str, default="parasmaipada", help="Voice for --tinanta (parasmaipada / atmanepada)")
    parser.add_argument("--krdanta", type=str, help="Derive Kṛdanta primary verbal derivative (e.g. 'kṛ', 'gam')")
    parser.add_argument("--taddhita", type=str, help="Derive Taddhitānta secondary nominal derivative (e.g. 'dharma', 'vasudeva')")
    parser.add_argument("--affix", "-f", type=str, default="ktva", help="Affix key for --krdanta (ktva, lyap, tumun, kta, ktavatu, satr, sanac, tavya, aniya) or --taddhita (matup, inith, tva, tal, an, thak, mayat)")
    parser.add_argument("--upasarga", "-u", type=str, default=None, help="Upasarga prefix for --krdanta (e.g. 'sam', 'pra')")
    parser.add_argument("--anvaya-tree", type=str, help="Build Kāraka syntactic dependency tree for a continuous verse")
    parser.add_argument("--export-dossier", type=str, help="Export courtroom-grade legal dossier for a nominal pada")
    parser.add_argument("--export-format", type=str, default="markdown", help="Export format (markdown, html, json)")
    parser.add_argument("--chandas", type=str, help="Scan a verse into metrical akṣaras and identify its metre")
    parser.add_argument("--script", type=str, default="auto", help="Input script for --chandas (auto, devanagari, iast)")
    parser.add_argument("--boundary-mode", type=str, default="auto", help="Pāda boundaries for --chandas (auto, lines, dandas, single)")
    parser.add_argument("--tradition", type=str, default="auto", help="Metre tradition for --chandas (auto, classical, vedic)")
    parser.add_argument(
        "--astadhyayi",
        nargs="?",
        const="summary",
        metavar="SUTRA",
        help=(
            "Codification status of the Aṣṭādhyāyī. Bare for the summary, "
            "a sūtra id (1.1.9) for one entry in full, 'open' for the "
            "outstanding questions, 'full' for every entry."
        ),
    )
    args = parser.parse_args()

    if args.astadhyayi:
        # Imported here, not at module level: loading the registry reads
        # the corpus off disk, and no other subcommand needs it.
        from src.astadhyayi import report as astadhyayi_report

        choice = args.astadhyayi
        if choice == "summary":
            print(astadhyayi_report.summary())
        elif choice in ("open", "--open"):
            print(astadhyayi_report.open_questions())
        elif choice in ("full", "--full"):
            print(astadhyayi_report.full())
        else:
            try:
                print(astadhyayi_report.detail(choice))
            except KeyError as exc:
                print(f"  {exc}")
        return

    classifier = SanskritClassifier()
    subanta_engine = SubantaEngine()
    quad_engine = QuadConcordanceEngine(subanta_engine)
    krdanta_engine = KrdantaTaddhitaEngine()
    tinanta_engine = TinantaEngine()
    verse_dep_engine = VerseDependencyEngine(classifier)
    dossier_exporter = DossierExporter(subanta_engine, quad_engine)

    if args.chandas:
        res = chandas_report(
            args.chandas,
            script=args.script,
            boundary_mode=args.boundary_mode,
            tradition=args.tradition,
        )
        format_chandas_report(res)
    elif args.tinanta:
        res = tinanta_engine.generate_conjugation(args.tinanta, args.lakara, args.pada_type)
        format_tinanta_matrix(res)
    elif args.krdanta:
        res = krdanta_engine.derive_krdanta(args.krdanta, args.affix, args.upasarga)
        format_krdanta_derivation(res)
    elif args.taddhita:
        res = krdanta_engine.derive_taddhita(args.taddhita, args.affix)
        format_taddhita_derivation(res)
    elif args.anvaya_tree:
        res = verse_dep_engine.build_dependency_tree(args.anvaya_tree)
        format_verse_dependency(res)
    elif args.export_dossier:
        res = dossier_exporter.export_subanta_dossier(args.export_dossier, args.export_format)
        print(f"\n[Dossier Exported: {res['filename']}]\n")
        print(res["content"])
    elif args.concordance:
        res = quad_engine.generate_quad_concordance(args.concordance, args.linga, args.vibhakti_idx, args.vacana_idx)
        format_quad_concordance(res)
    elif args.derive:
        res = subanta_engine.derive_prakriya(args.derive, args.linga, args.vibhakti_idx, args.vacana_idx)
        format_prakriya_derivation(res)
    elif args.shabda:
        res = subanta_engine.generate_shabdarupa(args.shabda, args.linga)
        format_shabdarupa_matrix(res)
    elif args.analyze_subanta:
        res = subanta_engine.analyze_subanta(args.analyze_subanta)
        format_subanta_analysis(args.analyze_subanta, res)
    elif args.text:
        res = classifier.classify(args.text)
        format_classification_result(res)
    elif args.batch:
        for word in args.batch:
            res = classifier.classify(word)
            format_classification_result(res)
    else:
        interactive_mode(classifier, subanta_engine, quad_engine, krdanta_engine, tinanta_engine, verse_dep_engine, dossier_exporter)


if __name__ == "__main__":
    main()


