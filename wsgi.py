'''
    Flask webapp
'''
import os
from flask import Flask, request, Response
from werkzeug.middleware.proxy_fix import ProxyFix

# Flask app
app: Flask = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app,
                        x_for = 1,
                        x_proto = 1,
                        x_host = 1,
                        x_prefix = 1)


# Index route
@app.route('/')
def index():
    '''
        Index
    '''
    try:
        return Response(f"{request.remote_addr or ''}\n",
                        mimetype = "text/plain",
                        headers = {"X-Your-Ip": request.remote_addr})
    except Exception as e: # pylint: disable=broad-exception-caught
        return Response(f"{e}\n",
                        mimetype = "text/plain")

# For wsgi_mod
application = app
