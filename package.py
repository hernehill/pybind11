name = "pybind11"

version = "2.13.1.hh.1.0.0"

authors = [
    "PyBind",
]

description = (
    """Lightweight header-only library that exposes C++ types in Python and vice-versa"""
)

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = []

private_build_requires = []

variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.10"],
    ["python-3.11"],
    ["python-3.12"],
]


def commands():
    env.REZ_PYBIND11_ROOT = "{root}"
    env.PYBIND11_ROOT_DIR = "{root}"
    env.PYBIND11_ROOT = "{root}"
    env.pybind11_ROOT = "{root}"
    env.pybind11_DIR = "{root}/share/cmake/pybind11"


uuid = "repository.pybind11"
