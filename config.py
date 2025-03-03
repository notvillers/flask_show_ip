'''
    Config file for the project
'''
import os

PORT: int = 1338

log_path: str = os.path.join(os.path.dirname(__file__),
                             "log")

if not os.path.exists(log_path):
    os.mkdir(log_path)

flask_log_file: str = os.path.join(log_path,
                                   "flask.log")

wsgi_log_file: str = os.path.join(log_path,
                                  "wsgi.log")
