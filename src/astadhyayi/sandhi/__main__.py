# -*- coding: utf-8 -*-
"""python -m src.astadhyayi.sandhi "rāmas ca"  — print the derivation."""

import sys

from src.astadhyayi.sandhi import SandhiInputError, sandhi


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print(__doc__)
        return 2
    try:
        print(sandhi(" ".join(args)).trace())
    except SandhiInputError as error:
        print(f"cannot read that: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
