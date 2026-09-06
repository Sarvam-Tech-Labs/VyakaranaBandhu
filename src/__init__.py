"""
Sanskrit Morphological Classifier & Subanta Engine Package
Categorizes Sanskrit input and executes Pāṇinian / Harināmāmṛta Subanta derivations.
"""

from .classifier import SanskritClassifier
from .subanta_engine import SubantaEngine
from .quad_concordance import QuadConcordanceEngine
from .krdanta_taddhita import KrdantaTaddhitaEngine
from .tinanta_engine import TinantaEngine
from .verse_dependency import VerseDependencyEngine
from .dossier_exporter import DossierExporter

__all__ = [
    "SanskritClassifier",
    "SubantaEngine",
    "QuadConcordanceEngine",
    "KrdantaTaddhitaEngine",
    "TinantaEngine",
    "VerseDependencyEngine",
    "DossierExporter"
]


