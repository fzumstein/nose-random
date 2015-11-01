import os
import re
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'nose_random', '__init__.py')) as f:
    version = re.compile(r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

setup(
    name='nose-random',
    packages=find_packages(),
    version=version,
    description='Random scenario testing in Nose',
    author='Zoomer Analytics LLC',
    author_email='eric.reynolds@zoomeranalytics.com',
    url='https://github.com/ZoomerAnalytics/nose-random',
    keywords=['nose', 'tests', 'nosetests', 'test', 'unit', 'testing', 'random', 'stochastic',
              'entropy', 'randomized', 'scenario'],
    entry_points={
        'nose.plugins.0.10': [
            'nose_random = nose_random:NoseRandomPlugin'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
