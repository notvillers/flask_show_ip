#!/bin/bash
script_dir=$(dirname "$0")
cd $script_dir
source .venv/bin/activate
python wsgi.py
deactivate