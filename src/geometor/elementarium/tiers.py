"""Optical tier specifications and fused-silica physical constants."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

FUSED_SILICA_ND: sp.Rational = sp.Rational(2917, 2000)
"""Nominal refractive index of fused silica (SiO2) at 589.3 nm (1.4585)."""


def brewster_spread(refractive_index: sp.Expr = FUSED_SILICA_ND) -> sp.Expr:
    """Compute exact Rational Trigonometry spread s_B = n^2 / (1 + n^2) for Brewster's angle.

    Because tan(theta_B) = n, sin^2(theta_B) = n^2 / (1 + n^2) is strictly rational
    whenever the refractive index is rational.

    Args:
        refractive_index: Exact symbolic refractive index n of the dielectric medium.

    Returns:
        Exact symbolic spread s_B in [0, 1].
    """
    n_expr = sp.sympify(refractive_index)
    return sp.simplify(n_expr**2 / (1 + n_expr**2))


@dataclass(frozen=True)
class OpticalTier:
    """Specification of a single passive readout stratum in the Elementarium stack."""

    tier_id: str
    index: int
    name: str
    illumination: str
    physical_mechanism: str
    unlock_prerequisite: str
    information_role: str


TIERS: tuple[OpticalTier, ...] = (
    OpticalTier(
        tier_id="T0",
        index=0,
        name="Raw Light & Aperture Projection",
        illumination="Uncollimated sunlight, starlight, or broadband point source",
        physical_mechanism="Precision macro-apertures and pinhole/caustic shadow geometry",
        unlock_prerequisite="Direct line-of-sight illumination onto any matte surface",
        information_role=(
            "Establishes unit chord, Vesica symmetry, golden proportion, and visual "
            "ray-alignment instructions for two-stage beam collimation."
        ),
    ),
    OpticalTier(
        tier_id="T1",
        index=1,
        name="Collimated Reticle & Diffractive Primer",
        illumination="Collimated broadband or monochromatic optical beam",
        physical_mechanism="Micro-lithographic fused-silica reticles and phase gratings",
        unlock_prerequisite="Two-aperture alignment and focal spacing taught in T0",
        information_role=(
            "Encodes glyph-free constructive geometry, visual deduction syntax, "
            "rational quadrance/spread invariants, and the Brewster polarization key."
        ),
    ),
    OpticalTier(
        tier_id="T2",
        index=2,
        name="Brewster-Angle Birefringent Library",
        illumination="Cross-polarized light via dual fused-silica Brewster reflectors",
        physical_mechanism="Form-birefringent slow-axis azimuth and retardance voxels in SiO2",
        unlock_prerequisite="Dual dielectric plates inclined at Brewster spread s_B taught in T1",
        information_role=(
            "Reveals high-density scientific, metrological, chemical, biological, "
            "and structural canons invisible under unpolarized illumination."
        ),
    ),
    OpticalTier(
        tier_id="T3",
        index=3,
        name="Interferometric Logic & Cold-Boot Machine Layer",
        illumination="Coherent / Vernier-aligned optical input or camera sensor array",
        physical_mechanism="Superimposed Moire/Vernier masks and self-describing fiduciary matrices",
        unlock_prerequisite="Bit-lattice grammar and combinator reduction rules taught in T2",
        information_role=(
            "Provides passive optical nomography alongside a self-bootstrapping "
            "symbolic DAG engine (G.1-G.601) operable by optical sensors or machines."
        ),
    ),
)


class TiersMixin:
    """Mixin for Elementarium class containing optical tier query methods."""

    @property
    def tiers(self) -> tuple[OpticalTier, ...]:
        """Return all four passive optical readout tiers."""
        return TIERS

    def get_tier(self, tier_id: str) -> OpticalTier:
        """Retrieve an optical tier by identifier (e.g., ``'T0'``).

        Args:
            tier_id: Case-insensitive tier identifier ``T0``..``T3``.

        Returns:
            Matching :class:`OpticalTier`.

        Raises:
            KeyError: If ``tier_id`` is not defined in :data:`TIERS`.
        """
        key = tier_id.strip().upper()
        for tier in TIERS:
            if tier.tier_id == key:
                return tier
        msg = f"Unknown optical tier: {tier_id!r}"
        raise KeyError(msg)

    def fused_silica_brewster_spread(self) -> sp.Expr:
        """Return exact Brewster spread s_B for fused silica (n_D = 2917/2000)."""
        return brewster_spread(FUSED_SILICA_ND)
