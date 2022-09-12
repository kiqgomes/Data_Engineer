from distutils.core import setup

from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['Sum.pyx'])
)

"""
Compile code:
    > python setup.py build_ext --inplace
"""