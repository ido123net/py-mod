from __future__ import annotations

import argparse
from typing import Sequence


def parse_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="py-mod")

    parser.add_argument("module", help="The module name to create.")
    parser.add_argument(
        "-r",
        "--running-main",
        action="store_true",
        help="Make it a running module (create a `__main__.py` and `main.py`)",
    )

    return parser.parse_args(args)
