#!/bin/bash

clear
pip uninstall pythra -y
python setup.py sdist bdist_wheel
pip install dist/pythra-0.2.1.tar.gz
rm -r build dist

pythra -v
