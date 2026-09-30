# -*- coding: utf-8 -*-
"""
The rules of the sandhi engine, one module per family.

Each module defines its rules with `@rule(...)` and lists them in a module
level `RULES` tuple; `rulebook.py` collects them. A family module owns its file
outright, so families can be written and tested independently of one another.
"""
