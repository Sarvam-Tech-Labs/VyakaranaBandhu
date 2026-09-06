"""
Benchmark Evaluation Suite for Sanskrit Morphological Classifier
Computes cross-validation metrics, full-corpus accuracy, per-class precision/recall/F1, and confusion matrix.
"""

import json
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import StratifiedKFold
from src.classifier import SanskritClassifier
from src.ml_model import SanskritMLClassifier


def evaluate_system():
    print("=" * 70)
    print("      SANSKRIT MORPHOLOGICAL CLASSIFIER: BENCHMARK EVALUATION")
    print("=" * 70)

    # 1. Load dataset
    with open("data/dataset.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = [item["text"] for item in data]
    labels = [item["label"] for item in data]
    categories = [item.get("category", "") for item in data]
    
    unique_labels = sorted(list(set(labels)))
    print(f"Total Benchmark Samples: {len(texts)}")
    print(f"Target Classes ({len(unique_labels)}): {', '.join(unique_labels)}")
    print("-" * 70)

    # 2. Cross-Validation of ML Model
    print(">>> Running 5-Fold Stratified Cross-Validation on ML Ensemble...")
    ml_clf = SanskritMLClassifier()
    X = ml_clf.feature_extractor.fit_transform(texts)
    y = np.array(labels)
    
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = []
    
    for fold, (train_idx, test_idx) in enumerate(skf.split(X, y), 1):
        X_tr, y_tr = X[train_idx], y[train_idx]
        X_te, y_te = X[test_idx], y[test_idx]
        
        ml_clf.model.fit(X_tr, y_tr)
        preds = ml_clf.model.predict(X_te)
        acc = accuracy_score(y_te, preds)
        cv_scores.append(acc)
        print(f"  Fold {fold} Accuracy: {acc*100:.2f}%")
        
    print(f"Mean CV Accuracy: {np.mean(cv_scores)*100:.2f}% (±{np.std(cv_scores)*100:.2f}%)")
    print("-" * 70)

    # 3. Hybrid Classifier Evaluation
    print(">>> Evaluating Complete Hybrid Pipeline (Pāṇinian Rules + ML)...")
    classifier = SanskritClassifier(load_pretrained_ml=False)
    # Train the ML component
    classifier.ml_classifier.train(texts, labels, save=True)
    
    hybrid_preds = []
    for t in texts:
        res = classifier.classify(t)
        hybrid_preds.append(res["predicted_class"])

    overall_acc = accuracy_score(labels, hybrid_preds)
    print(f"\nOverall Hybrid Accuracy: {overall_acc*100:.2f}%\n")

    # 4. Detailed Classification Report
    print("Classification Report:")
    print(classification_report(labels, hybrid_preds, digits=4))

    # 5. Confusion Matrix
    print("Confusion Matrix:")
    cm = confusion_matrix(labels, hybrid_preds, labels=unique_labels)
    
    header = f"{'True \\ Pred':<15}" + "".join([f"{l:<15}" for l in unique_labels])
    print(header)
    print("-" * len(header))
    for i, row_label in enumerate(unique_labels):
        row_str = f"{row_label:<15}" + "".join([f"{cm[i][j]:<15}" for j in range(len(unique_labels))])
        print(row_str)

    # 6. Canonical Test Suite
    print("\n" + "=" * 70)
    print("               CANONICAL RESEARCH PAPERS TEST SUITE")
    print("=" * 70)
    
    test_cases = [
        ("pacati", "None", "Simplex Verb"),
        ("kumāraḥ", "None", "Simplex Noun"),
        ("kṛpaṇaḥ", "None", "Internal Retroflexion Simplex"),
        ("rāmo gacchati", "Sandhi Only", "Visarga External Sandhi"),
        ("ityādi", "Sandhi Only", "Yaṇ External Sandhi"),
        ("sadaiva", "Sandhi Only", "Vṛddhi External Sandhi"),
        ("rājapuruṣaḥ", "Samāsa Only", "Tatpuruṣa Compound"),
        ("dharmakṣetram", "Samāsa Only", "Tatpuruṣa Compound"),
        ("yathāśakti", "Samāsa Only", "Avyayībhāva Compound"),
        ("devānāmpriyaḥ", "Samāsa Only", "Aluk Samāsa Exception"),
        ("nīlotpalam", "Both", "Karmadhāraya + Guṇa Sandhi"),
        ("mahātmā", "Both", "Bahuvrīhi + Dīrgha Sandhi"),
        ("mahotsavaḥ", "Both", "Karmadhāraya + Guṇa Sandhi"),
        ("devālayaḥ", "Both", "Tatpuruṣa + Dīrgha Sandhi"),
        # Devanagari Test Cases
        ("पचति", "None", "Devanagari Simplex Verb"),
        ("रामो गच्छति", "Sandhi Only", "Devanagari Visarga Sandhi"),
        ("राजपुरुषः", "Samāsa Only", "Devanagari Tatpuruṣa"),
        ("नीलोत्पलम्", "Both", "Devanagari Karmadhāraya + Guṇa")
    ]

    correct_count = 0
    for input_str, expected, desc in test_cases:
        res = classifier.classify(input_str)
        pred = res["predicted_class"]
        conf = res["confidence"]
        status = "✓ PASS" if pred == expected else "✗ FAIL"
        if pred == expected:
            correct_count += 1
            
        print(f"[{status}] {input_str:<18} ({desc})")
        print(f"        Expected: {expected:<12} | Predicted: {pred:<12} | Confidence: {conf*100:.1f}%")
        print(f"        Reason: {res['explanation']}")
        print()

    print(f"Canonical Test Suite Result: {correct_count}/{len(test_cases)} Passed ({(correct_count/len(test_cases))*100:.1f}%)")
    print("=" * 70)


if __name__ == "__main__":
    evaluate_system()
