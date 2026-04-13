import os
from setuptools import setup

# Allow CI to override version via PACKAGE_VERSION env var (set from git tag)
version = os.environ.get('PACKAGE_VERSION')
if version:
    setup(version=version)
else:
    setup()
