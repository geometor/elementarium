"""Mark I Desktop Optical Prototype geometry and exact Plate 0 construction."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
from geometor.model import Model, line_spread, quadrance, vertex_spread
from geometor.model.algebra import zero_test

from .tiers import FUSED_SILICA_ND, brewster_spread

PHI: sp.Expr = (sp.Integer(1) + sp.sqrt(5)) / sp.Integer(2)
"""Exact golden ratio (1 + sqrt(5)) / 2."""


def _assert_exact(actual: sp.Expr, expected: sp.Expr | int) -> None:
    """Verify exact symbolic equality via geometor.model.algebra.zero_test.

    Args:
        actual: Computed symbolic expression.
        expected: Expected symbolic expression or integer.

    Raises:
        AssertionError: If ``actual - expected`` is non-zero.
    """
    diff = sp.sympify(actual) - sp.sympify(expected)
    if not zero_test(diff):
        msg = f"Symbolic invariant mismatch: {actual} != {expected}"
        raise AssertionError(msg)


@dataclass(frozen=True)
class MarkIBenchSpec:
    """Physical and exact algebraic geometry for the Mark I Desktop Prototype."""

    reticle_size_mm: sp.Rational
    unit_chord_mm: sp.Rational
    refractive_index: sp.Rational

    @property
    def collimator_station_mm(self) -> sp.Expr:
        """Exact golden-section station distance u * phi in millimeters."""
        return self.unit_chord_mm * PHI

    @property
    def reticle_station_mm(self) -> sp.Expr:
        """Exact reticle stage distance u * phi^2 in millimeters."""
        return sp.expand(self.unit_chord_mm * PHI**2)

    @property
    def analyzer_station_mm(self) -> sp.Expr:
        """Exact Brewster analyzer stage distance u * phi^3 in millimeters."""
        return sp.expand(self.unit_chord_mm * PHI**3)

    @property
    def brewster_spread(self) -> sp.Expr:
        """Exact Brewster incidence spread s_B = n^2 / (1 + n^2)."""
        return brewster_spread(self.refractive_index)

    @property
    def brewster_angle_deg(self) -> float:
        """Numeric Brewster incidence angle in degrees for bench machining."""
        angle_rad = sp.atan(self.refractive_index)
        return float(sp.deg(angle_rad).evalf())


DEFAULT_MARK_I_BENCH = MarkIBenchSpec(
    reticle_size_mm=sp.Rational(50, 1),
    unit_chord_mm=sp.Rational(20, 1),
    refractive_index=FUSED_SILICA_ND,
)


def build_keystone_plate_model() -> Model:
    """Construct exact float-free geometor.model DAG for Plate 0 (Vesica Keystone).

    Starting solely from apertures ``A(0, 0)`` and ``B(1, 0)``, constructs:

    1. Vesica Piscis circles ``(A, B)`` and ``(B, A)`` meeting at ``C`` and ``D`` (spread ``3/4``).
    2. Perpendicular bisector ``[CD]`` meeting ``[AB]`` at midpoint ``M(1/2, 0)`` (spread ``1``).
    3. Perpendicular segment at ``B`` of half-unit length to ``P(1, 1/2)``, yielding hypotenuse ``|AP| = sqrt(5)/2``.
    4. Golden section locus ``PhiInv(1/phi, 0)`` and ``Phi(phi, 0)`` on axis ``[AB]``.

    Returns:
        Verified exact :class:`geometor.model.Model` instance.
    """
    m = Model("plate_0_keystone", auto_intersect=False, enable_logging=False)

    a = m.set_point(0, 0, classes=["given", "aperture"], ID="A")
    b = m.set_point(1, 0, classes=["given", "aperture"], ID="B")
    axis_ab = m.construct_line(a, b, classes=["axis"], ID="[ A B ]")

    c_a = m.construct_circle(a, b, classes=["vesica"], ID="( A B )")
    c_b = m.construct_circle(b, a, classes=["vesica"], ID="( B A )")

    c_top = m.intersect(c_a, c_b, side_of=(a, b, 1), classes=["keystone"], ID="C")
    d_bot = m.intersect(c_a, c_b, side_of=(a, b, -1), classes=["keystone"], ID="D")

    bisector = m.construct_line(c_top, d_bot, classes=["bisector"], ID="[ C D ]")
    mid = m.intersect(axis_ab, bisector, between=(a, b), classes=["midpoint"], ID="M")

    m.construct_polygon([a, b, c_top], classes=["equilateral"], ID="< A B C >")

    # Erect exact perpendicular at B using compass-and-straightedge subconstruction
    with m.subconstruction("perp_at_B") as scope:
        c_bm = m.construct_circle(b, mid, classes=["guide"], guide=True)
        e_ext = m.intersect(axis_ab, c_bm, other_than=mid, guide=True)
        c_me = m.construct_circle(mid, e_ext, classes=["guide"], guide=True)
        c_em = m.construct_circle(e_ext, mid, classes=["guide"], guide=True)
        k_top = m.intersect(c_me, c_em, side_of=(mid, e_ext, 1), guide=True)
        perp_b = m.construct_line(b, k_top, classes=["guide"], ID="perp_B", guide=True)
        p_half = m.intersect(
            perp_b,
            c_bm,
            side_of=(a, b, 1),
            classes=["golden_aux"],
            ID="P",
        )
        scope.keep(p_half)

    # Transfer golden ratio onto optical axis [AB]
    diag_ap = m.construct_line(a, p_half, classes=["guide"], ID="[ A P ]", guide=True)
    c_pb = m.construct_circle(p_half, b, classes=["guide"], ID="( P B )", guide=True)
    q_inner = m.intersect(diag_ap, c_pb, between=(a, p_half), classes=["guide"], guide=True)
    r_outer = m.intersect(diag_ap, c_pb, beyond=(a, p_half), classes=["guide"], guide=True)

    c_aq = m.construct_circle(a, q_inner, classes=["golden"], ID="( A phi_inv )")
    c_ar = m.construct_circle(a, r_outer, classes=["golden"], ID="( A phi )")

    g_inv = m.intersect(axis_ab, c_aq, between=(a, b), classes=["golden_stop"], ID="PhiInv")
    g_phi = m.intersect(axis_ab, c_ar, beyond=(a, b), classes=["golden_stop"], ID="Phi")

    # Verify exact algebraic and Rational Trigonometry invariants
    _assert_exact(quadrance(a, b), 1)
    _assert_exact(quadrance(a, c_top), 1)
    _assert_exact(vertex_spread(b, a, c_top), sp.Rational(3, 4))
    _assert_exact(line_spread(axis_ab, bisector), 1)
    _assert_exact(quadrance(a, mid), sp.Rational(1, 4))
    _assert_exact(quadrance(a, p_half), sp.Rational(5, 4))
    _assert_exact(g_inv.x, sp.Integer(1) / PHI)
    _assert_exact(g_phi.x, PHI)

    return m


class BenchMixin:
    """Mixin for Elementarium class providing Mark I desktop bench specifications."""

    @property
    def bench(self) -> MarkIBenchSpec:
        """Return default Mark I Desktop Optical Prototype specification."""
        return DEFAULT_MARK_I_BENCH

    def build_keystone_model(self) -> Model:
        """Construct and verify the exact Plate 0 Vesica Keystone model."""
        return build_keystone_plate_model()
