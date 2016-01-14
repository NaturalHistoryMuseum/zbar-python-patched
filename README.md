ZBar
====
ZBar is an open source software suite for reading bar codes from various sources, such as video streams, image files and raw intensity sensors. It supports many popular symbologies (types of bar codes) including EAN-13/UPC-A, UPC-E, EAN-8, Code 128, Code 39, Interleaved 2 of 5 and QR Code.

The purpose of this repository
==============================
This repository is forked from the [ZBar python wrapper download at PyPI](https://pypi.python.org/pypi/zbar/0.10), and only contains the python wrapper for the C library. For the full C library source, installation directions, etc., check out the [ZBar homepage](http://zbar.sourceforge.net).

The Natural History Museum's fork adds a wheel build for Windows 32-bit.

Fixes implemented
===================
[Patches `imagescanner.c`](https://github.com/npinchot/zbar/commit/d3c1611ad2411fbdc3e79eb96ca704a63d30ae69) to fix crashing (segmentation fault 11) issues with `import zbar` on OS X.

Patch taken from [http://launchpadlibrarian.net/134768014/zbar_0.10+doc-7build3_0.10+doc-8.diff.gz](http://launchpadlibrarian.net/134768014/zbar_0.10+doc-7build3_0.10+doc-8.diff.gz).

Installing on Mac OS X
======================
* Install `zbar` using homebrew:

    ```
    brew install zbar
    ```

* Install the extension module

    ```
    pip install https://github.com/NaturalHistoryMuseum/zbar-python-patched/archive/v0.10.tar.gz
    ```

Installing on Windows 32-bit
=============================
Install a release from this repo, e.g.:

```
pip install https://github.com/NaturalHistoryMuseum/zbar-python-patched/releases/download/v0.10/zbar-0.10-cp27-none-win_win32.whl
```

Building for Windows 32-bit
===========================

You should only need to build if you want to release a new version.

* Download and install
[Miniconda-latest-Windows-x86.exe](https://repo.continuum.io/miniconda/).

* Download
[MinGW](http://freefr.dl.sourceforge.net/project/mingw/Installer/mingw-get-setup.exe),
install to `C:\MinGW`, and run

    ```
    c:\MinGW\bin\mingw-get.exe install gcc
    ```

* Create `libpython27.a` from `python27.dll`, for the benefit of the MinGW linker

    Following [this advice](http://eli.thegreenplace.net/2008/06/28/compiling-python-extensions-with-distutils-and-mingw).

    ```
    c:\MinGW\bin\mingw-get install pexports
    FOR /F %a IN ('python -c "import sys; print(sys.exec_prefix)"') DO cd %a
    c:\MinGW\bin\pexports.exe python27.dll > python27.def
    c:\MinGW\bin\dlltool --dllname python27.dll --def python27.def --output-lib libs\libpython27.a
    ```

* Download
[zbar-0.10-setup.exe](http://sourceforge.net/projects/zbar/files/zbar/0.10/zbar-0.10-setup.exe/download)
and install to `c:\zbar`

* Build the `zbar` Python extension module and a wheel

    ```
    cd <where you cloned this repo>
    SET PATH=c:\MinGW\bin;%PATH%
    SET INCLUDE=C:\ZBar\include;%INCLUDE%
    SET LIB=C:\ZBar\lib;%LIB%
    SET LIBPATH=C:\ZBar\lib;%LIBPATH%
    SET PATH=c:\MinGW\bin;%PATH%
    build.bat
    ```

The `dist` directory will contain a wheel.
