"""Unit tests for geometor.elementarium optical tiers, Mark I bench, and Plate 0."""

from __future__ import annotations

from pathlib import Path

import pytest
import sympy as sp
from geometor.model.algebra import zero_test

from geometor.elementarium import (
    FUSED_SILICA_ND,
    PHI,
    Elementarium,
    brewster_spread,
    build_keystone_plate_model,
    export_plate_svg,
    run_cli,
)


def test_brewster_spread_is_exact_rational() -> None:
    """Verify fused-silica Brewster spread s_B = n^2 / (1 + n^2) is strictly rational."""
    s_b = brewster_spread(FUSED_SILICA_ND)
    assert isinstance(s_b, sp.Rational)
    expected = sp.Rational(2917**2, 2000**2 + 2917**2)
    assert s_b == expected


def test_mark_i_bench_golden_stations() -> None:
    """Verify Fibonacci/golden recurrence u + u*phi == u*phi^2 on the optical rail."""
    elem = Elementarium()
    bench = elem.bench
    lhs = bench.unit_chord_mm + bench.collimator_station_mm
    rhs = bench.reticle_station_mm
    assert zero_test(lhs - rhs)
    assert 55.5 < bench.brewster_angle_deg < 55.7


def test_keystone_plate_model_is_float_free() -> None:
    """Ensure Plate 0 model contains zero sp.Float atoms and exact golden stops."""
    model = build_keystone_plate_model()
    for geom in model:
        assert not geom.atoms(sp.Float)

    by_id = {info.ID: geom for geom, info in model.items() if info.ID}
    assert zero_test(by_id["Phi"].x - PHI)
    assert zero_test(by_id["PhiInv"].x - (sp.Integer(1) / PHI))


def test_tier_and_plate_lookup() -> None:
    """Verify Mixin lookup methods and KeyError guards."""
    elem = Elementarium()
    assert len(elem.tiers) == 4
    assert elem.get_tier("t2").tier_id == "T2"
    assert elem.get_plate("p0").plate_id == "P0"

    with pytest.raises(KeyError):
        elem.get_tier("T9")
    with pytest.raises(KeyError):
        elem.get_plate("P99")


def test_export_plate_svg_and_cli(tmp_path: Path) -> None:
    """Verify 1:1 50mm SVG reticle export and CLI subcommands."""
    svg_file = tmp_path / "plate_0.svg"
    written = export_plate_svg(svg_file)
    assert written.is_file()
    content = written.read_text(encoding="utf-8")
    assert 'width="50mm"' in content
    assert 'data-plate="P0"' in content

    assert run_cli(["status"]) == 0
    assert run_cli(["tiers"]) == 0
    assert run_cli(["plates"]) == 0
    assert run_cli(["export-masks", "-o", str(tmp_path / "cli_p0.svg")]) == 0
