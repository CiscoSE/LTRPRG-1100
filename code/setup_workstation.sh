#!/usr/bin/env bash

mkdir -p ~/lab/pythonenv
python -m venv ~/lab/pythonenv
source ~/lab/pythonenv/Scripts/activate
git clone https://github.com/curtissmith/LTRPRG-1100.git ~/lab/LTRPRG-1100
python -m pip install --upgrade pip==19.1.1
pip install -r ~/lab/LTRPRG-1100/requirements.txt
git clone https://github.com/YangModels/yang.git ~/lab/yang
pip install pyang==1.7.8
deactivate
exit