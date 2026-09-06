# -*- coding: utf-8 -*-
"""
The codified sūtras, one module per pāda.

Importing this package loads every rule module and so populates the registry.
Discovery is automatic: a new `adhyaya_N_pada_M.py` is picked up by being
there, with nothing to add here. Registration happens as a side effect of
import — each module calls `sources.register` at module level — so a consumer
that imports one module by hand gets that pāda only, while importing the
package gets all of them. Anything that reports on coverage wants the package.
"""

from __future__ import annotations

import importlib
import pkgutil
from typing import Tuple


def _load_all() -> Tuple[str, ...]:
    loaded = []
    for module in pkgutil.iter_modules(__path__):
        if module.name.startswith("_"):
            continue
        importlib.import_module(f"{__name__}.{module.name}")
        loaded.append(module.name)
    return tuple(sorted(loaded))


#: The pāda modules found and imported, in name order.
PADAS: Tuple[str, ...] = _load_all()

__all__ = ["PADAS"]
