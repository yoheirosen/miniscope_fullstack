"""Compatibility package exposing existing miniscope_fullstack modules."""

from pathlib import Path

# Extend this package's module search path to include repository-root modules/packages.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in __path__:
    __path__.append(str(_REPO_ROOT))

__all__ = []
