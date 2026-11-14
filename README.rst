=====================
GEOMETOR Elementarium
=====================

*Passive optical archive and zero-context geometric bootstrap architecture for 100,000-year knowledge preservation.*

Digital infrastructure has inverted the durability of human memory: contemporary civilization generates exabytes of symbolic data on media whose physical and semantic half-life is measured in years. Without active electrical power, supply chains, character tables, file-format specifications, and living linguistic context, modern storage collapses into indecipherable entropy within a single century.

**Elementarium** is an engineering and epistemological initiative within the **GEOMETOR** ecosystem to design, prototype, and verify a monolithic, unpowered optical archive in fused silica (:math:`\text{SiO}_2`) engineered for a :math:`10^5`-year horizon. All that is required to initiate recovery is **light**.

Design Axioms
-------------

1. **Zero-Power Optical Readout**: The archive contains no batteries, electronics, moving motors, or degradable polymers. Every stratum is recovered passively by passing light through engineered apertures, photomasks, birefringent retarder lattices, and interferometric waveguides.
2. **Self-Bootstrapping Instrument Ladder**: To defeat the *Dead-Reader Paradox* (requiring a high-technology reader just to decode Bit 0), each optical tier visually demonstrates how to align or construct the optical apparatus required to unlock the next tier.
3. **Zero-Context Geometric Primer**: Before introducing natural language, history, chemistry, or machine code, the archive establishes formal syntax, equivalence, deduction, number, and invariant proportion from pure constructive geometry (*Euclid I.1* Vesica Piscis, Rational Trigonometry quadrance/spread, and harmonic cross-ratio).
4. **Intrinsic Physical Standards**: Fused quartz (:math:`\text{SiO}_2`) serves simultaneously as substrate, lens, waveplate, and metrological standard—anchoring length, wavelength, refractive dispersion (:math:`n_D \approx 1.4585`, Brewster angle :math:`\theta_B = \arctan n_D \approx 55.57^\circ`), and piezoelectric resonance directly in the artifact.
5. **Dual-Observer Recovery (Biological & Machine)**: The Primer escalates seamlessly from naked-eye projected geometry to dense polarization-multiplexed symbolic DAGs and self-describing combinator virtual machines operable by optical sensors or autonomous machines.

Four-Tier Optical Stack
-----------------------

- **Tier 0 — Raw Light & Pinhole/Caustic Projection**: Uncollimated sunlight, starlight, or torchlight passing through precision macro-apertures casts the *Vesica Keystone* (`Plate 0`), establishing unit ratio and visual instructions for two-aperture beam collimation.
- **Tier 1 — Collimated Reticle & Diffractive Primer**: Collimated light projects micro-lithographic fused-silica plates encoding constructive geometry, visual deduction rules, arithmetic ratios, and the *Brewster Polarization Key* (:math:`\tan\theta_B = n`).
- **Tier 2 — Brewster-Angle Birefringent Library**: Crossed glass reflectors set at :math:`55.56^\circ` illuminate slow-axis azimuth and retardance voxels hidden invisibly inside transparent silica, unlocking high-density scientific, biological, and structural canons.
- **Tier 3 — Interferometric Logic & Cold-Boot Machine Layer**: Superimposed Vernier/Moiré optical masks and coherent waveguide frames provide passive combinatorial evaluation alongside a self-describing symbolic DAG engine (`G.1`–`G.601`).

Current Engineering Objective: Mark I Desktop Prototype
-------------------------------------------------------

Phase 1 focuses on constructing and testing the **Elementarium Mark I** benchtop optical prototype (`50 mm × 50 mm` fused-silica reticle standard on a proportioned passive optical rail) to validate end-to-end zero-text optical bootstrapping on the bench.

CLI Usage
---------

Managed with ``uv`` targeting Python 3.13:

.. code-block:: bash

   # Display Mark I Desktop Prototype & optical specification summary
   python -m geometor.elementarium status

   # Inspect the 4-tier optical bootstrap stack
   python -m geometor.elementarium tiers

   # List Mark I Primer plates (P0 - P5)
   python -m geometor.elementarium plates

   # Export 1:1 50mm x 50mm fabrication/projection SVG mask for Plate 0
   python -m geometor.elementarium export-masks

Documentation
-------------

Compile the Sphinx technical specification locally via ``photon-platform/publish``:

.. code-block:: bash

   publish build
