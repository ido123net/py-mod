from __future__ import annotations

import os
import pathlib


def create(module: str) -> int:
    module_path = pathlib.Path(module)
    os.mkdir(module_path)

    _init_file = module_path / '__init__.py'
    with open(_init_file, 'w'):
        pass

    return 0
