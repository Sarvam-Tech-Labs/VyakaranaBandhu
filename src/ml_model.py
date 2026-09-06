"""
Machine Learning Classifier for Sanskrit Morphology
Trains, tunes, and predicts using an ensemble of linear and tree-based classifiers (with fallback when sklearn is not yet installed).
"""

import json
import os
from typing import List, Dict, Tuple, Any

try:
    import joblib
except ImportError:
    joblib = None

try:
    import numpy as np
except ImportError:
    np = None

try:
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

from .feature_extractor import SanskritFeatureExtractor
from .normalizer import clean_text

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "model.joblib")
DATASET_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "dataset.json")


class SanskritMLClassifier:
    """
    ML Classifier utilizing TF-IDF character n-grams and dense linguistic features.
    """
    def __init__(self):
        self.feature_extractor = SanskritFeatureExtractor(ngram_range=(2, 5), max_features=600)
        self.classes_ = ['Both', 'None', 'Samāsa Only', 'Sandhi Only']
        self.is_trained = False

        if SKLEARN_AVAILABLE:
            clf_lr = LogisticRegression(C=5.0, max_iter=1000, class_weight='balanced', random_state=42)
            clf_rf = RandomForestClassifier(n_estimators=100, max_depth=12, random_state=42)
            clf_gb = GradientBoostingClassifier(n_estimators=80, learning_rate=0.1, random_state=42)
            
            self.model = VotingClassifier(
                estimators=[('lr', clf_lr), ('rf', clf_rf), ('gb', clf_gb)],
                voting='soft'
            )
        else:
            self.model = None

    def load_dataset(self, path: str = DATASET_PATH) -> Tuple[List[str], List[str]]:
        """Load benchmark dataset."""
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        texts = [item["text"] for item in data]
        labels = [item["label"] for item in data]
        return texts, labels

    def train(self, texts: List[str] = None, labels: List[str] = None, save: bool = True):
        """Train the feature extractor and classifier."""
        if not SKLEARN_AVAILABLE:
            self.is_trained = True
            return self

        if texts is None or labels is None:
            texts, labels = self.load_dataset()

        X = self.feature_extractor.fit_transform(texts)
        y = np.array(labels)
        
        self.model.fit(X, y)
        self.classes_ = list(self.model.classes_)
        self.is_trained = True

        if save and joblib is not None:
            self.save(MODEL_PATH)
            
        return self

    def predict(self, texts: List[str]) -> List[str]:
        """Predict class labels for given texts."""
        probs = self.predict_proba(texts)
        return [max(p.items(), key=lambda x: x[1])[0] for p in probs]

    def predict_proba(self, texts: List[str]) -> List[Dict[str, float]]:
        """Predict class probabilities."""
        if SKLEARN_AVAILABLE and self.model is not None:
            if not self.is_trained:
                self.train()
            X = self.feature_extractor.transform(texts)
            probas = self.model.predict_proba(X)
            
            results = []
            for row in probas:
                prob_dict = {cls: float(row[i]) for i, cls in enumerate(self.classes_)}
                results.append(prob_dict)
            return results
        else:
            # Heuristic feature-weighted probability estimator fallback
            results = []
            for t in texts:
                feats = self.feature_extractor.extract_linguistic_features(t)
                scores = {'None': 0.25, 'Sandhi Only': 0.25, 'Samāsa Only': 0.25, 'Both': 0.25}
                
                if feats.get('stem_pada_sandhi', 0) > 0:
                    scores['Both'] += 0.8
                if feats.get('stem_pada_direct', 0) > 0:
                    scores['Samāsa Only'] += 0.8
                if feats.get('pada_pada_sandhi', 0) > 0 or feats.get('has_space', 0) > 0:
                    scores['Sandhi Only'] += 0.7
                if feats.get('ends_with_verb', 0) > 0 and feats.get('num_words', 1) == 1:
                    scores['None'] += 0.6
                if feats.get('starts_with_known_stem', 0) > 0 and feats.get('diphthong_count', 0) > 0:
                    scores['Both'] += 0.4
                    
                total = sum(scores.values())
                norm_scores = {k: v / total for k, v in scores.items()}
                results.append(norm_scores)
            return results

    def save(self, filepath: str = MODEL_PATH):
        """Persist model and feature extractor to disk."""
        if joblib is not None and SKLEARN_AVAILABLE:
            data = {
                'feature_extractor': self.feature_extractor,
                'model': self.model,
                'classes_': self.classes_
            }
            joblib.dump(data, filepath)

    def load(self, filepath: str = MODEL_PATH):
        """Load trained model from disk."""
        if joblib is not None and os.path.exists(filepath):
            data = joblib.load(filepath)
            self.feature_extractor = data['feature_extractor']
            self.model = data['model']
            self.classes_ = data['classes_']
            self.is_trained = True
            return True
        return False
