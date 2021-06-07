import pathlib
from typing import List

import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()

def read_requirements(filename: str) -> List[str]:
    return pathlib.Path('requires', filename).read_text().split('\n')

setuptools.setup(
    name='rbaas',
    version='0.0.1',
    author='Connor',
    author_email='noxor@noxor.io',
    description='Small project to practice and learn',
    long_description=long_description,
    install_requires=read_requirements('requirements.txt'),
    extras_require={'dev': read_requirements('development.txt')}
)
