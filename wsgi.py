'''
    Webapp.py is the main file that runs the web application.
'''
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
    return Response(f"{request.remote_addr or ''}\n",
                    mimetype = "text/plain",
                    headers={"X-Your-Ip": request.remote_addr})

application = app
