
# THIS FILE WAS AUTOMATICALLY GENERATED BY deprecated_modules.py
import sys
# mypy error: Module X has no attribute y (typically for C extensions)
from . import _empirical_covariance  # type: ignore
from ..externals._pep562 import Pep562
from ..utils.deprecation import _raise_dep_warning_if_not_pytest

deprecated_path = 'GMMA.covariance.empirical_covariance_'
correct_import_path = 'GMMA.covariance'

_raise_dep_warning_if_not_pytest(deprecated_path, correct_import_path)

def __getattr__(name):
    return getattr(_empirical_covariance, name)

if not sys.version_info >= (3, 7):
    Pep562(__name__)
