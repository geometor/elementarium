:navigation: header
:order: 95

=======
Modules
=======

``geometor.elementarium`` follows the GEOMETOR Mixin Architecture, separating optical tier physics, Mark I bench geometry, and Primer reticle export into composable modules:

- :mod:`geometor.elementarium` — Public package interface exporting :class:`~geometor.elementarium.elementarium.Elementarium`, :data:`~geometor.elementarium.tiers.TIERS`, :data:`~geometor.elementarium.bench.DEFAULT_MARK_I_BENCH`, :data:`~geometor.elementarium.plates.PRIMER_PLATES`, :func:`~geometor.elementarium.bench.build_keystone_plate_model`, and :func:`~geometor.elementarium.plates.export_plate_svg`.
- :mod:`geometor.elementarium.tiers` — :class:`~geometor.elementarium.tiers.OpticalTier` specifications, exact fused-silica Brewster spread (:func:`~geometor.elementarium.tiers.brewster_spread`), and :class:`~geometor.elementarium.tiers.TiersMixin`.
- :mod:`geometor.elementarium.bench` — :class:`~geometor.elementarium.bench.MarkIBenchSpec` golden-station rail geometry, exact float-free ``geometor.model`` Keystone builder (:func:`~geometor.elementarium.bench.build_keystone_plate_model`), and :class:`~geometor.elementarium.bench.BenchMixin`.
- :mod:`geometor.elementarium.plates` — :class:`~geometor.elementarium.plates.PrimerPlate` sequence (``P0``–``P5``), 1:1 ``50 mm × 50 mm`` SVG reticle serializer (:func:`~geometor.elementarium.plates.render_keystone_svg`), and :class:`~geometor.elementarium.plates.PlatesMixin`.
- :mod:`geometor.elementarium.cli` — Rich command-line interface (``status``, ``tiers``, ``plates``, ``export-masks``).