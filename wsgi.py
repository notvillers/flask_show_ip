'''
    Flask webapp
'''
import os
from flask import Flask, request, Response, jsonify
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
    return Response(f"{request.remote_addr or ''}\n",
                    mimetype = "text/plain",
                    headers = {"X-Your-Ip": request.remote_addr})

@app.errorhandler(Exception)
def handle_exception(error):
    '''
        Handle exceptions
    '''
    return jsonify({"error": str(error)}), 500

# For wsgi_mod
application = app
