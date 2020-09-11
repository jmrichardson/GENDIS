#!/usr/bin/env python

from setuptools import setup
import numpy as np
from Cython.Build import cythonize

setup(name='GENDIS',
      version='1.0.13',
      description=' Contains an implementation (sklearn API) of the algorithm proposed in "GENDIS: GEnetic DIscovery of Shapelets" and code to reproduce all experiments.',
      author='Gilles Vandewiele',
      author_email='gilles.vandewiele@ugent.be',
      url='https://github.com/IBCNServices/GENDIS',
      packages=['gendis'],
      install_requires=[
          'deap',
          	  'numpy',
      	  'pandas',
      	  'pathos',
      	  'scipy',
      	  'sklearn',
      	  'tqdm',
      	  'tslearn',
          'nose2',
          'terminaltables'
      ],
      test_suite='nose2.collector.collector',
      ext_modules = cythonize(['gendis/pairwise_dist.pyx']),
      include_dirs=[np.get_include()]
     )
