import os

from flask import Flask

import gevent
from gevent import monkey
from gevent.pywsgi import WSGIServer

gevent.monkey.patch_all()

app = Flask(__name__)

if __name__ == '__main__':

    @app.route('/')
    def root_access():
        return 'ERR'

    @app.route('/check', methods=["GET"])
    def get_check():
        return json.dumps({"status": "ok"})

    http_server = WSGIServer(
        ('', 10000),
        app,
        backlog=2048,
        environ={
            'wsgi.multithread': True,
            'SERVER_SOFTWARE': 'EveryChat 81 v2018.11.07'
        }
    )

    http_server.serve_forever()
