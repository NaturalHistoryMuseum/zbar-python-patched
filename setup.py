#!/usr/bin/env python
import os
import shutil
import sys

from setuptools import setup, Extension

from distutils.sysconfig import get_config_vars

setup_args = dict(
    name = 'zbar',
    version = '0.10',
    author = 'Jeff Brown',
    author_email = 'spadix@users.sourceforge.net',
    url = 'http://zbar.sourceforge.net',
    description = 'read barcodes from images or video',
    license = 'LGPL',
    long_description = open('README').read(),
    classifiers = [
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Environment :: X11 Applications',
        'Environment :: Win32 (MS Windows)',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Communications',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Software Development :: Libraries',
    ],
    ext_modules = [
        Extension('zbar', [
                'zbarmodule.c',
                'enum.c',
                'exception.c',
                'symbol.c',
                'symbolset.c',
                'symboliter.c',
                'image.c',
                'processor.c',
                'imagescanner.c',
                'decoder.c',
                'scanner.c',
                ],
            libraries = [ 'zbar' ],
        ),
    ],
)

if 'bdist' in sys.argv and 'win32' == sys.platform:
    # More work for binary distruction of windows build
    ZBAR = os.getenv('ZBAR') or 'C:\\ZBar'
    shutil.copy(os.path.join(ZBAR, 'bin', 'zlib1.dll'), '.')
    shutil.copy(os.path.join(ZBAR, 'bin', 'libzbar-0.dll'), '.')
    shutil.copy(os.path.join(ZBAR, 'bin', 'libiconv-2.dll'), '.')
    setup_args['ext_modules'][0].library_dirs = [os.path.join(ZBAR, 'lib')]
    setup_args['ext_modules'][0].include_dirs = get_config_vars('INCLUDEPY') + [os.path.join(ZBAR, 'include')]
    setup_args['data_files'] = [('', ['zlib1.dll', 'libzbar-0.dll', 'libiconv-2.dll'])]

setup(**setup_args)
