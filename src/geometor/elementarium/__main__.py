"""Command-line entry point for ``python -m geometor.elementarium``."""

from __future__ import annotations

import sys

from .cli import run_cli


def main() -> None:
    """Invoke :func:`run_cli` and exit with its status code."""
    raise SystemExit(run_cli())


if __name__ == "__main__":
    sys.exit(run_cli())