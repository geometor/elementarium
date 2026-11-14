"""Passive optical archive and zero-context geometric bootstrap architecture.

Provides :class:`~geometor.elementarium.elementarium.Elementarium`, optical tier
specifications (:mod:`~geometor.elementarium.tiers`), Mark I desktop bench
geometry (:mod:`~geometor.elementarium.bench`), and Primer reticle exporters
(:mod:`~geometor.elementarium.plates`).
"""

from __future__ import annotations

from .bench import (
    DEFAULT_MARK_I_BENCH,
    PHI,
    BenchMixin,
    MarkIBenchSpec,
    build_keystone_plate_model,
)
from .cli import run_cli
from .elementarium import Elementarium
from .plates import (
    PRIMER_PLATES,
    PlatesMixin,
    PrimerPlate,
    export_plate_svg,
    render_keystone_svg,
)
from .tiers import (
    FUSED_SILICA_ND,
    TIERS,
    OpticalTier,
    TiersMixin,
    brewster_spread,
)

__version__ = "0.1.0"

__all__ = [
    "DEFAULT_MARK_I_BENCH",
    "FUSED_SILICA_ND",
    "PHI",
    "PRIMER_PLATES",
    "TIERS",
    "BenchMixin",
    "Elementarium",
    "MarkIBenchSpec",
    "OpticalTier",
    "PlatesMixin",
    "PrimerPlate",
    "TiersMixin",
    "__version__",
    "brewster_spread",
    "build_keystone_plate_model",
    "export_plate_svg",
    "render_keystone_svg",
    "run_cli",
]
