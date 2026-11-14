"""Demonstration script for the Mark I Desktop Optical Prototype specification."""

from __future__ import annotations

from geometor.elementarium import run_cli


def main() -> int:
    """Print the Mark I Desktop Prototype status table."""
    return run_cli(["status"])


if __name__ == "__main__":
    raise SystemExit(main())
