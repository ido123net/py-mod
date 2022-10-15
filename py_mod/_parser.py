from __future__ import annotations

import argparse
from typing import Sequence


def parse_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='py-mod')

    subparsers = parser.add_subparsers(dest='command')

    def _add_cmd(name: str, *, help: str) -> argparse.ArgumentParser:
        parser = subparsers.add_parser(name, help=help)
        return parser

    create_parser = _add_cmd('create', help='Create new python module')
    create_parser.add_argument('module', help='The module name to create.')

    return parser.parse_args(args)
