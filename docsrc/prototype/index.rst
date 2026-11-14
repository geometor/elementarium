:navigation: header
:order: 20

========================
Mark I Desktop Prototype
========================

The immediate engineering objective of ``geometor.elementarium`` is the **Mark I Desktop Optical Prototype**: a benchtop, completely unpowered passive optical instrument built around ``50 mm × 50 mm`` fused-silica plates on a golden-proportioned kinematic rail.

Benchtop Geometry & Station Detents
-----------------------------------

All axial station positions derive from a single physical unit chord :math:`u = |AB| = 20\text{ mm}` established directly on ``Plate 0``:

- **Entrance Aperture (`Station 0`)**: :math:`0\text{ mm}` — ``Plate 0`` (*Vesica Keystone*) receiving external sunlight, LED point illumination, or heliostat input.
- **Collimator Stage (`Station 1`)**: :math:`u \cdot \phi = 10(1 + \sqrt{5})\text{ mm} \approx 32.361\text{ mm}` — Secondary pinhole slit / fused-silica planoconvex singlet (:math:`f \approx 32.4\text{ mm}`).
- **Reticle Stage (`Station 2`)**: :math:`u \cdot \phi^2 = 10(3 + \sqrt{5})\text{ mm} \approx 52.361\text{ mm}` — ``50 mm × 50 mm`` chrome-on-quartz and birefringent waveplate carrier.
- **Brewster Analyzer Stage (`Station 3`)**: :math:`u \cdot \phi^3 = 20(2 + \sqrt{5})\text{ mm} \approx 84.721\text{ mm}` — Removable / rotatable fused-silica flat inclined at :math:`\theta_B = \arctan(1.4585) \approx 55.564^\circ`.

Notice the additive self-verification built into the rail:

.. math::

   u + u\phi = u\phi^2, \qquad u\phi + u\phi^2 = u\phi^3

Any observer holding ``Plate 0`` can verify every axial spacing on the optical bench by direct compass transfer without a millimeter scale.

Candidate Benchtop Fabrication Paths
------------------------------------

1. **T0 Aperture Keystone**: Laser-cut brass / blackened stainless steel foil or etched silicon aperture mask mounted in a ``50 mm × 50 mm`` quartz frame.
2. **T1 Primer Reticles**: Photolithographic chrome-on-quartz reticles (``1-2 um`` minimum feature size) or UV-laser-ablated metallic thin-film masks on fused silica.
3. **T2 Birefringent Demonstrator**:
   - *Benchtop Iteration A*: Patterned multi-order quartz / polymer retarder sectors laminated between fused-silica flats, completely transparent in unpolarized ``T1`` projection and high-contrast between crossed :math:`55.56^\circ` glass Brewster plates.
   - *Benchtop Iteration B*: Femtosecond-laser-written form-birefringent nanogratings inside monolithic fused silica.
4. **T3 Combinatorial & Sensor Frame**: Dual counter-rotating Vernier quartz reticles paired with a high-density hexagonal fiduciary matrix encoding the minimal DAG evaluator.
