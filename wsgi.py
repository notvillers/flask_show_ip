'''
    Flask webapp
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

@app.errorhandler(404)
def page_not_found(_):
    '''
        Handle 404 errors

        Args:
            _: Exception (ignored)
    '''
    return Response("Page not found",
                    mimetype = "text/plain",
                    status = 404)


@app.errorhandler(Exception)
def handle_exception(_: Exception):
    '''
        Handle exceptions

        Args:
            _: Exception (ignored)
    '''
    return Response("Unexpected error",
                    mimetype = "text/plain",
                    status = 500)


# Index route
@app.route('/')
def index():
    '''
        Index
    '''
    return Response(f"{request.remote_addr or ''}\n",
                    mimetype = "text/plain",
                    headers = {"X-Your-Ip": request.remote_addr or ''})


# For wsgi_mod
application = app
