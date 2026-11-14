"""Main Elementarium coordinator composing optical tier, bench, and plate mixins."""

from __future__ import annotations

from .bench import BenchMixin
from .plates import PlatesMixin
from .tiers import TiersMixin


class Elementarium(TiersMixin, BenchMixin, PlatesMixin):
    """Coordinator for the Elementarium optical specification and Mark I prototype."""

    def summary(self) -> dict[str, object]:
        """Return a structured engineering summary of the Mark I Desktop Prototype."""
        bench = self.bench
        return {
            "tiers": len(self.tiers),
            "plates": len(self.plates),
            "reticle_size_mm": int(bench.reticle_size_mm),
            "unit_chord_mm": int(bench.unit_chord_mm),
            "refractive_index": str(bench.refractive_index),
            "brewster_spread": str(bench.brewster_spread),
            "brewster_angle_deg": round(bench.brewster_angle_deg, 4),
        }