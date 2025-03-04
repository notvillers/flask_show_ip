#!/bin/bash
port=1338
script_dir=$(dirname "$0")
cd $script_dir
source .venv/bin/activate
mod_wsgi-express start-server wsgi.py --processes 2 --port $port
deactivate