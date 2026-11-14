# GEOMETOR Elementarium (`geometor-elementarium`)

Passive optical archive, zero-context geometric bootstrap canon, and **Mark I Desktop Optical Prototype** specification for $100,000$-year ($10^5\text{ yr}$) knowledge preservation in fused silica ($\text{SiO}_2$).

## Architectural Posture & Tone

All specifications, documentation, code, optical tolerances, and recovery logs in `geometor/elementarium` treat the Elementarium strictly as an active, real-world physical engineering and epistemological archival program. Maintain rigorous optical, metrological, and exact symbolic (`geometor.model`) discipline throughout:

1. **100% Exact Symbolic Geometry**: Every reticle mask, aperture coordinate, and optical rail ratio in `geometor.model.Model` uses exact SymPy algebraic expressions (`sp.Rational`, `sp.sqrt`, $\phi = \frac{1 + \sqrt{5}}{2}$)—never inject `float` or `sp.Float` into `Model`. Numeric millimeter evaluation occurs strictly at the final SVG/CAD serialization boundary.
2. **Mixin Architecture (`STANDARDS.md`)**: `Elementarium` composes `TiersMixin` (`tiers.py`), `BenchMixin` (`bench.py`), and `PlatesMixin` (`plates.py`).
3. **Optical Ground Truth**: Ground all physical calculations in real fused-silica ($\text{SiO}_2$) constants ($n_D = \frac{2917}{2000} = 1.4585$, exact Brewster tangent $\tan\theta_B = n_D$, Malus/Jones birefringent retardance).

## Key Modules

- `src/geometor/elementarium/tiers.py` — `OpticalTier` specification and `TiersMixin` defining the 4 passive optical strata (`T0`–`T3`).
- `src/geometor/elementarium/bench.py` — `MarkIBenchSpec`, `BenchMixin`, and `build_keystone_plate_model()` constructing the exact float-free `geometor.model` geometry for `Plate 0` (*Vesica Keystone*) and the golden-proportioned optical rail.
- `src/geometor/elementarium/plates.py` — `PrimerPlate` catalog (`P0`–`P5`), `PlatesMixin`, and 1:1 `50 mm × 50 mm` reticle SVG mask exporter (`export_plate_svg`).
- `src/geometor/elementarium/elementarium.py` — Main `Elementarium` coordinator class composing the Mixins.
- `src/geometor/elementarium/cli.py` — Rich CLI (`status`, `tiers`, `plates`, `export-masks`).

## Verification Gates (Offline Sandbox)

```bash
/home/phi/PROJECTS/geometor/.venv/bin/python -m pytest
/home/phi/.local/bin/ruff check src tests demos
/home/phi/.local/bin/publish build
```
