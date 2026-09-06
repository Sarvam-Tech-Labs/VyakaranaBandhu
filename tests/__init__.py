import os
import sys

# Ensure project root is in python path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

def unwrapped(text: str) -> str:
    """
    A note with its line wrapping flattened, for matching quotations.

    Notes are stored wrapped at about seventy columns, so any quoted
    phrase longer than a few words may fall across a break and a plain
    `assertIn` will miss it. That has happened three times — at
    3.3.76, at 3.3.169, and once in the तच्छीलादि run — and each time
    the fix was to shorten the quotation, which weakens the test.

    Not a substitute for getting sandhi right: ततोऽन्यत्रापि contains
    no independent अ however it is wrapped, and no whitespace change
    will find one. This handles formatting only.
    """
    return " ".join(text.split())
