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

# Error response
def error_response(content: str,
                   status: int = 500) -> Response:
    '''
        Create an error response

        Args:
            content (str): Response content
            status (int): HTTP status code

        Returns:
            Response: Flask response
    '''
    return Response(content,
                    mimetype = "text/plain",
                    status = status)


# 404 error handler
@app.errorhandler(404)
def page_not_found(_: Exception) -> Response:
    '''
        Handle 404 errors

        Args:
            _: Exception (ignored)
    '''
    return error_response(content = "Page not found",
                          status = 404)


# 500 error handler
@app.errorhandler(Exception)
def handle_exception(_: Exception) -> Response:
    '''
        Handle exceptions

        Args:
            _: Exception (ignored)
    '''
    return error_response(content = "Unexpected error",
                          status = 500)


# Index route
@app.route('/')
def index():
    '''
        Index
    '''
    return Response(f"{request.remote_addr or ''}\n",
                    mimetype = "text/plain",
                    headers = {"X-Your-Ip": request.remote_addr or ''},
                    status = 200)


# For wsgi_mod
application = app
