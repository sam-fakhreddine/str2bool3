import os
from setuptools import setup

# Read version from environment variable, with fallback to default version
version = os.environ.get('PACKAGE_VERSION', '1.0.0')

setup(
    name='str2bool3',
    packages=['str2bool3'],
    version=version,
    description='Convert string to boolean (Forked from SymonSoft/str2bool)',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/sam-fakhreddine/str2bool3',
    download_url=f'https://github.com/sam-fakhreddine/str2bool3/archive/refs/tags/{version}.tar.gz',
    keywords=['str2bool', 'bool', 'boolean', 'convert', 'yes', 'no', 'true', 'false'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Utilities'
    ],
)
