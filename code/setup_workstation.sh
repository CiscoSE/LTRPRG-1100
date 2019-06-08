#!/usr/bin/env bash

## Download with 'curl https://raw.githubusercontent.com/CiscoSE/LTRPRG-1100/master/code/setup_workstation.sh > setup_workstation.sh'
## and run with 'source setup_workstation.sh'

mkdir -p ~/lab/pythonenv
git clone https://github.com/CiscoSE/LTRPRG-1100.git ~/lab/LTRPRG-1100
python -m venv ~/lab/pythonenv
source ~/lab/pythonenv/Scripts/activate
python -m pip install --upgrade pip==19.1.1
pip install -r ~/lab/LTRPRG-1100/requirements.txt
pip install pyang==1.7.8
git clone https://github.com/YangModels/yang.git ~/lab/yang
deactivate
