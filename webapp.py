'''
    Webapp.py is the main file that runs the web application.
'''

from flask import Flask, request, Response
from logger import Logger as L
import config as cfg

app: Flask = Flask(__name__)
l: L = L(cfg.flask_log_file)

@app.route('/')
def index():
    '''
        Index
    '''
    l.log(f"Request from {request.remote_addr}")
    return Response(f"{request.remote_addr or ''}\n",
                    mimetype = "text/plain",
                    headers={"X-Your-Ip": request.remote_addr})

if __name__ == '__main__':
    app.app_context().push()
    app.run(host = "0.0.0.0",
            debug = True,
            port = 9000)
