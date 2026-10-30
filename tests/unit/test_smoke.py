import importlib

import pytest

LIBS = [
    "numpy", "pandas", "scipy", "matplotlib", "astropy", "astroquery",
    "sklearn", "pyarrow", "pandera", "hypothesis", "joblib", "tomli",
    "streamlit",
]


@pytest.mark.parametrize("name", LIBS)
def test_library_imports(name):
    importlib.import_module(name)
