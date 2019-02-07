#!/usr/bin/env python
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("cssdbpy.cssdbpy", ["cssdbpy/cssdbpy.pyx"]),]
cmdclass = {'build_ext': build_ext}

setup(
    name='cssdbpy',
    version='0.2.1.1',
    packages=['cssdbpy'],
    ext_modules=ext_modules,
    cmdclass=cmdclass,
    author='deslum',
    author_email='randomazer@gmail.com',
    url='https://github.com/cssdbpy',
    description='High performance SSDB client implemented with Cython'
)
