echo Building win32 wheel of zbar
echo Clean
del /S *pyc
del /S *dll
rmdir /Q /S dist build

echo Build
python setup.py build --compiler mingw32 bdist bdist_wheel
