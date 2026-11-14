"""Command-line interface for GEOMETOR Elementarium."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from rich.console import Console
from rich.table import Table

from .elementarium import Elementarium


def build_parser() -> argparse.ArgumentParser:
    """Build argument parser for the ``elementarium`` CLI."""
    parser = argparse.ArgumentParser(
        prog="elementarium",
        description=(
            "Elementarium optical specification, Mark I Desktop Prototype parameters, "
            "and 1:1 reticle SVG mask generator."
        ),
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("status", help="Display Mark I Desktop Prototype optical summary")
    sub.add_parser("tiers", help="Inspect the 4-tier passive optical bootstrap stack")
    sub.add_parser("plates", help="List the Mark I Primer plate sequence (P0-P5)")

    exp = sub.add_parser(
        "export-masks",
        help="Export 1:1 50mm x 50mm SVG reticle mask for Plate 0 (Vesica Keystone)",
    )
    exp.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("docsrc/_static/plates/plate_0_keystone.svg"),
        help="Output SVG file path (default: docsrc/_static/plates/plate_0_keystone.svg)",
    )
    return parser


def run_cli(argv: Sequence[str] | None = None) -> int:
    """Execute the ``elementarium`` CLI and return an exit status code.

    Args:
        argv: Optional command-line argument sequence; defaults to ``sys.argv[1:]``.

    Returns:
        Zero on clean execution.
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    cmd = args.command or "status"

    elem = Elementarium()
    console = Console()

    if cmd == "status":
        bench = elem.bench
        table = Table(title="Elementarium — Mark I Desktop Optical Prototype")
        table.add_column("Parameter", style="cyan")
        table.add_column("Exact / Symbolic", style="green")
        table.add_column("Bench Metric", style="yellow")
        table.add_row("Substrate", "SiO2 (Fused Silica)", f"n_D = {float(bench.refractive_index):.4f}")
        table.add_row(
            "Reticle Standard",
            f"{bench.reticle_size_mm} x {bench.reticle_size_mm}",
            f"{float(bench.reticle_size_mm):.1f} mm x {float(bench.reticle_size_mm):.1f} mm",
        )
        table.add_row("Unit Chord |AB|", str(bench.unit_chord_mm), f"{float(bench.unit_chord_mm):.3f} mm")
        table.add_row(
            "Collimator Station (u * phi)",
            str(bench.collimator_station_mm),
            f"{float(bench.collimator_station_mm.evalf()):.3f} mm",
        )
        table.add_row(
            "Reticle Station (u * phi^2)",
            str(bench.reticle_station_mm),
            f"{float(bench.reticle_station_mm.evalf()):.3f} mm",
        )
        table.add_row(
            "Analyzer Station (u * phi^3)",
            str(bench.analyzer_station_mm),
            f"{float(bench.analyzer_station_mm.evalf()):.3f} mm",
        )
        table.add_row(
            "Brewster Incidence",
            f"s_B = {bench.brewster_spread}",
            f"{bench.brewster_angle_deg:.3f} deg",
        )
        console.print(table)
        return 0

    if cmd == "tiers":
        table = Table(title="Four-Tier Passive Optical Bootstrap Stack")
        table.add_column("Tier", style="bold cyan")
        table.add_column("Name", style="white")
        table.add_column("Illumination", style="yellow")
        table.add_column("Role", style="green")
        for tier in elem.tiers:
            table.add_row(tier.tier_id, tier.name, tier.illumination, tier.information_role)
        console.print(table)
        return 0

    if cmd == "plates":
        table = Table(title="Mark I Desktop Prototype — Primer Plates")
        table.add_column("Plate", style="bold cyan")
        table.add_column("Tier", style="magenta")
        table.add_column("Title", style="white")
        table.add_column("Bootstrap Concept", style="green")
        for plate in elem.plates:
            table.add_row(plate.plate_id, plate.tier_id, plate.title, plate.bootstrap_concept)
        console.print(table)
        return 0

    if cmd == "export-masks":
        written = elem.export_keystone_svg(args.output)
        console.print(f"[green]Exported 1:1 reticle SVG:[/green] {written}")
        return 0

    return 0
