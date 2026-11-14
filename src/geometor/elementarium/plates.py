"""Mark I Primer plate catalog and 1:1 50mm reticle SVG mask exporter."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import sympy as sp
import sympy.geometry as spg

from .bench import DEFAULT_MARK_I_BENCH, build_keystone_plate_model


@dataclass(frozen=True)
class PrimerPlate:
    """Metadata for a single zero-context optical plate in the Mark I prototype."""

    plate_id: str
    tier_id: str
    title: str
    substrate: str
    optical_encoding: str
    bootstrap_concept: str


PRIMER_PLATES: tuple[PrimerPlate, ...] = (
    PrimerPlate(
        plate_id="P0",
        tier_id="T0",
        title="Vesica Keystone & Rail Proportion Gauge",
        substrate="50 mm x 50 mm fused silica / precision aperture mask",
        optical_encoding="Pinholes A, B, C, D, M, PhiInv, Phi + micro-slit locus",
        bootstrap_concept=(
            "Unit chord 1, equilateral spread 3/4, right angle spread 1, "
            "golden section phi, and two-stage beam collimation spacing."
        ),
    ),
    PrimerPlate(
        plate_id="P1",
        tier_id="T1",
        title="Collimation & Focal Lock",
        substrate="50 mm x 50 mm chrome-on-quartz reticle",
        optical_encoding="Concentric Vernier rings and paraxial ray convergence diagram",
        bootstrap_concept=(
            "Confirms sharp focus at station u * phi^2 and establishes "
            "equivalence (=), incidence, and parallel ray transport."
        ),
    ),
    PrimerPlate(
        plate_id="P2",
        tier_id="T1",
        title="Quadrance, Spread & Deductive Implication",
        substrate="50 mm x 50 mm chrome-on-quartz reticle",
        optical_encoding="Pythagorean / Rational Trigonometry area-quadrance decomposition",
        bootstrap_concept=(
            "Defines Given -> Construct -> Invariant visual syntax, natural integers, "
            "rational ratios, and orthogonal quadrance addition Q1 + Q2 = Q3."
        ),
    ),
    PrimerPlate(
        plate_id="P3",
        tier_id="T1",
        title="The Brewster Polarization Key",
        substrate="50 mm x 50 mm chrome-on-quartz reticle",
        optical_encoding="Refraction/reflection ray diagram at spread s_B = n^2 / (1 + n^2)",
        bootstrap_concept=(
            "Demonstrates reflection off two crossed fused-silica flats inclined at "
            "55.56 deg, extinguishing direct light until a birefringent plate intervenes."
        ),
    ),
    PrimerPlate(
        plate_id="P4",
        tier_id="T2",
        title="Birefringent Azimuth & Metrological Standard",
        substrate="50 mm x 50 mm patterned quartz / nanograting waveplate",
        optical_encoding="4-channel slow-axis azimuth sectors (0, 22.5, 45, 67.5 deg)",
        bootstrap_concept=(
            "Invisible in unpolarized light; calibrates analyzer rotation and anchors "
            "physical units to SiO2 lattice spacing and optical dispersion."
        ),
    ),
    PrimerPlate(
        plate_id="P5",
        tier_id="T3",
        title="Combinatorial Vernier & Symbolic DAG Seed",
        substrate="50 mm x 50 mm dual-layer Vernier reticle + fiduciary frame",
        optical_encoding="Hexagonal / concentric binary lattice + DAG incidence graph",
        bootstrap_concept=(
            "Self-describing state reduction rules enabling optical nomography or "
            "camera-driven cold-boot reconstruction of the G.1-G.601 canon."
        ),
    ),
)


def render_keystone_svg() -> str:
    """Render a 1:1 50 mm x 50 mm SVG reticle mask for Plate 0 (Vesica Keystone).

    Evaluates exact SymPy algebraic coordinates from :func:`build_keystone_plate_model`
    strictly at the SVG serialization boundary, mapping unit chord ``|AB| = 1``
    to ``unit_chord_mm = 20 mm`` centered on a ``50 mm x 50 mm`` quartz reticle.

    Returns:
        Complete SVG document string with physical ``mm`` dimensions and ``.euclid-graphic`` styling.
    """
    model = build_keystone_plate_model()
    spec = DEFAULT_MARK_I_BENCH
    size = float(spec.reticle_size_mm)
    scale = float(spec.unit_chord_mm)

    # Center midpoint M(1/2, 0) slightly left of plate center so Phi(1.618, 0) fits cleanly
    origin_x = 14.0
    origin_y = size / 2.0

    def to_mm(x_expr: sp.Expr, y_expr: sp.Expr) -> tuple[float, float]:
        px = origin_x + float(sp.sympify(x_expr).evalf()) * scale
        py = origin_y - float(sp.sympify(y_expr).evalf()) * scale
        return px, py

    lines_svg: list[str] = []
    circles_svg: list[str] = []
    points_svg: list[str] = []

    # Outer reticle boundary and fiducial corner crosses
    lines_svg.append(
        f'  <rect x="0.50" y="0.50" width="{size - 1.0:.2f}" height="{size - 1.0:.2f}" '
        'fill="#0b0e14" stroke="#8aa2c8" stroke-width="0.25" rx="1.0"/>'
    )
    lines_svg.append(
        f'  <line x1="2.50" y1="{origin_y:.4f}" x2="{size - 2.50:.2f}" y2="{origin_y:.4f}" '
        'stroke="#3b4b66" stroke-width="0.12" stroke-dasharray="0.8,0.6"/>'
    )

    for elem, info in model.items():
        if info.guide:
            continue
        el_id = info.ID or ""
        classes_str = " ".join(info.classes)

        if isinstance(elem, spg.Circle):
            cx, cy = to_mm(elem.center.x, elem.center.y)
            rad = float(sp.sympify(elem.radius).evalf()) * scale
            stroke = "#e5c07b" if "golden" in info.classes else "#61afef"
            dash = ' stroke-dasharray="0.9,0.5"' if "golden" in info.classes else ""
            circles_svg.append(
                f'  <circle cx="{cx:.4f}" cy="{cy:.4f}" r="{rad:.4f}" '
                f'fill="none" stroke="{stroke}" stroke-width="0.18"{dash} '
                f'data-id="{el_id}" class="{classes_str}"/>'
            )
        elif isinstance(elem, spg.Line):
            p1x, p1y = to_mm(elem.p1.x, elem.p1.y)
            p2x, p2y = to_mm(elem.p2.x, elem.p2.y)
            dx = p2x - p1x
            dy = p2y - p1y
            norm = (dx * dx + dy * dy) ** 0.5
            if norm > 0:
                ux, uy = dx / norm, dy / norm
                x1, y1 = p1x - ux * 20.0, p1y - uy * 20.0
                x2, y2 = p1x + ux * 36.0, p1y + uy * 36.0
                # Clip inside reticle margin
                x1 = max(3.0, min(size - 3.0, x1))
                x2 = max(3.0, min(size - 3.0, x2))
                y1 = max(3.0, min(size - 3.0, y1))
                y2 = max(3.0, min(size - 3.0, y2))
                lines_svg.append(
                    f'  <line x1="{x1:.4f}" y1="{y1:.4f}" x2="{x2:.4f}" y2="{y2:.4f}" '
                    f'stroke="#5c7089" stroke-width="0.14" data-id="{el_id}" class="{classes_str}"/>'
                )
        elif isinstance(elem, spg.Polygon):
            pts_attr = " ".join(
                f"{to_mm(v.x, v.y)[0]:.4f},{to_mm(v.x, v.y)[1]:.4f}" for v in elem.vertices
            )
            lines_svg.append(
                f'  <polygon points="{pts_attr}" fill="#61afef" fill-opacity="0.08" '
                f'stroke="#98c379" stroke-width="0.22" data-id="{el_id}" class="{classes_str}"/>'
            )
        elif isinstance(elem, spg.Point2D):
            px, py = to_mm(elem.x, elem.y)
            is_aperture = "aperture" in info.classes or "golden_stop" in info.classes
            r_pin = 0.55 if is_aperture else 0.38
            fill = "#ffffff" if is_aperture else "#e5c07b"
            points_svg.append(
                f'  <circle cx="{px:.4f}" cy="{py:.4f}" r="{r_pin:.2f}" '
                f'fill="{fill}" stroke="#0b0e14" stroke-width="0.12" '
                f'data-id="{el_id}" class="{classes_str}"/>'
            )

    body = "\n".join([*lines_svg, *circles_svg, *points_svg])
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{size:.0f}mm" height="{size:.0f}mm" '
        f'viewBox="0 0 {size:.2f} {size:.2f}" '
        'class="euclid-graphic elementarium-reticle" data-plate="P0">\n'
        f"{body}\n"
        "</svg>\n"
    )


def export_plate_svg(output_path: Path) -> Path:
    """Write the 1:1 50 mm x 50 mm Plate 0 SVG reticle mask to disk.

    Args:
        output_path: Destination file path for the generated SVG.

    Returns:
        Resolved path to the written SVG file.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_keystone_svg(), encoding="utf-8")
    return output_path.resolve()


class PlatesMixin:
    """Mixin for Elementarium class providing Primer plate lookup and SVG export."""

    @property
    def plates(self) -> tuple[PrimerPlate, ...]:
        """Return the ordered Mark I Primer plate catalog."""
        return PRIMER_PLATES

    def get_plate(self, plate_id: str) -> PrimerPlate:
        """Look up a Primer plate by identifier (e.g., ``'P0'``).

        Args:
            plate_id: Case-insensitive plate identifier ``P0``..``P5``.

        Returns:
            Matching :class:`PrimerPlate`.

        Raises:
            KeyError: If ``plate_id`` is not present in :data:`PRIMER_PLATES`.
        """
        key = plate_id.strip().upper()
        for plate in PRIMER_PLATES:
            if plate.plate_id == key:
                return plate
        msg = f"Unknown Primer plate: {plate_id!r}"
        raise KeyError(msg)

    def export_keystone_svg(self, output_path: Path) -> Path:
        """Export Plate 0 (Vesica Keystone) 1:1 SVG reticle mask to ``output_path``."""
        return export_plate_svg(output_path)
