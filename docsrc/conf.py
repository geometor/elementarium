"""Sphinx configuration for GEOMETOR Elementarium."""

from __future__ import annotations

import os
from pathlib import Path
import sys

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.elementarium as module  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "elementarium"
repo_name = "elementarium"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

# Configure offline-safe local intersphinx inventories across the GEOMETOR workspace
for _remote_key in list(intersphinx_mapping.keys()):  # noqa: F405
    _entry = intersphinx_mapping[_remote_key]  # noqa: F405
    if _entry[1] is None:
        intersphinx_mapping.pop(_remote_key, None)  # noqa: F405

for _sister in (
    "euclid",
    "elements",
    "codes",
    "fundamentals",
    "wildberger",
):
    _inv = _WORKSPACE_ROOT / _sister / "docs" / "objects.inv"
    if _inv.is_file():
        intersphinx_mapping[_sister] = (  # noqa: F405
            f"https://geometor.github.io/{_sister}",
            (os.fspath(_inv), None),
        )

html_theme = "foundation"
html_static_path: list[str] = ["_static"]
autoapi_add_toctree_entry = False
if "intro.rst" not in exclude_patterns:  # noqa: F405
    exclude_patterns.append("intro.rst")  # noqa: F405
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]
