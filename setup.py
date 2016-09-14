import sys

if sys.hexversion < 0x2070000:
    raise NotImplementedError('Python < 2.7 not supported.')

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(name='hdf5storage',
      version='0.2',
      description='Utilities to read/write Python types to/from HDF5 files, including MATLAB v7.3 MAT files.',
      long_description=long_description,
      author='Freja Nordsiek',
      author_email='fnordsie at gmail dt com',
      url='https://github.com/frejanordsiek/hdf5storage',
      packages=['hdf5storage'],
      install_requires=['numpy', 'h5py>=2.1'],
      tests_require=['nose>=1.0'],
      test_suite='nose.collector',
      license='BSD',
      keywords='hdf5 matlab',
      zip_safe=True,
      classifiers=[
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          "Intended Audience :: Developers",
          "Intended Audience :: Information Technology",
          "Intended Audience :: Science/Research",
          "Topic :: Scientific/Engineering",
          "Topic :: Database",
          "Topic :: Software Development :: Libraries :: Python Modules"
          ]
      )
