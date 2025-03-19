#!/bin/bash
port=1338
script_dir=$(dirname "$0")
cd $script_dir
source .venv/bin/activate
mod_wsgi-express start-server flask_ip_wsgi.py --processes 1 --port $port
deactivate
