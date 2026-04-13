import os
from setuptools import setup

# Single source of truth: PACKAGE_VERSION env var (set from git tag in CI),
# falling back to the default development version.
setup(version=os.environ.get('PACKAGE_VERSION', '1.4.0'))
