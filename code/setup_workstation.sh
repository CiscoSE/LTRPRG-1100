#!/usr/bin/env bash

mkdir ~/lab/pythonenv
python -m venv pythonenv
source ~/lab/pythonenv/Scripts/activate
git clone https://github.com/curtissmith/LTRPRG-1100.git
python -m pip install --upgrade pip==19.1.1
pip install -r ~/lab/LTRPRG-1100/requirements.txt
git clone https://github.com/YangModels/yang.git
pip install pyang==1.7.8
