from __future__ import annotations

import os
import pathlib


DEFAULT_DMAIN = """\
from __future__ import annotations

from .main import main


if __name__ == "__main__":
    raise SystemExit(main())
"""
DEFAULT_MAIN = """\
from __future__ import annotations


def main() -> int:
    return 0
"""


def create(module: str, runnin_main: bool = False) -> int:
    """create a blank module"""
    module_path = pathlib.Path(module)
    os.mkdir(module_path)

    _init_file = module_path / "__init__.py"
    with open(_init_file, "w"):
        pass

    if runnin_main:
        _dmain_file = module_path / "__main__.py"
        with open(_dmain_file, "w") as f:
            f.write(DEFAULT_DMAIN)
        _main_file = module_path / "main.py"
        with open(_main_file, "w") as f:
            f.write(DEFAULT_MAIN)

    return 0
