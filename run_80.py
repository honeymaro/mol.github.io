# -*- coding: utf-8 -*-
from flask import Flask, g, redirect, abort, make_response, jsonify, request
from flask_session import Session
from flask_cors import CORS
from gevent.wsgi import WSGIServer

app = Flask(__name__)
Session(app)

#: Flask-CORS
cors = CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": "true"}})

@app.before_request
def before_request():
    """
    모든 API 실행 전 실행하는 부분
    """
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

    if '/api' in request.environ['PATH_INFO']:
        is_ok = common.ddos_check_and_write_log()
        if is_ok is False:
            return make_response(jsonify(result_en='Blocked connection'
                                         , result_ko='접속이 차단되었습니다'
                                         , result=503), 503)

if __name__ == "__main__":
    # http = WSGIServer(('0.0.0.0', 5000), app)
    # http.serve_forever()
    https = WSGIServer(('0.0.0.0', 80), app)
    https.serve_forever()
