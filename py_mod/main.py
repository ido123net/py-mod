from __future__ import annotations

from typing import Sequence

from py_mod._parser import parse_args
from py_mod.create import create


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)

    if args.command == 'create':
        return create(module=args.module)

    return 0
