'''
    WSGI module
'''

from waitress import serve # pylint: disable=import-error
from logger import Logger as L
from webapp import app
import config as cfg

def run(l: L) -> None:
    '''
        Runs the web application
    '''
    l.log("Server started")
    try:
        serve(app,
              port = cfg.PORT)
    except Exception as e: # pylint: disable=broad-exception-caught
        l.log(f"Error: {e}")
    l.log("Server stopped")


if __name__ == '__main__':
    run(L(cfg.wsgi_log_file))
