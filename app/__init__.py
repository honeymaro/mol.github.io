# -*- coding: utf-8 -*-
from flask import Flask, g, redirect, abort, make_response, jsonify, request
from flask_session import Session
import pymysql

# Define the WSGI application object
app = Flask(__name__, static_url_path='/static')

#: Configurations
import config
app.config.from_object(config)

#: Flask-Session
Session(app)

#################################### 모듈 연결시키기 ####################################

# API Version
versions = ['/api/v1']

from app.subscribe.urls import subscribe
app.register_blueprint(subscribe, url_prefix='/api/v1/subscribe')

#####################################################################################

@app.before_request
def before_request():
    """
    모든 API 실행 전 실행하는 부분
    """
    g.db = pymysql.connect(
             host=config.DB_HOST,
             user=config.DB_USER,
             password=config.DB_PASS,
             db=config.DB_DEFAULTSCHEMA,
             charset='utf8',
             cursorclass=pymysql.cursors.DictCursor
            ) 


@app.teardown_request
def teardown_request(exception):
    """
    모든 API 실행 후 실행하는 부분. 여기서는 DB 연결종료.
    """
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(result_ko='존재하지 않는 페이지입니다'
                                 , result_en='Not Found!'
                                 , result=404), 404)


@app.errorhandler(401)
def not_unauthorized(error):
    return make_response(jsonify(result_ko='인증되지 않음'
                                 , result_en='Unauthenticated'
                                 , result=401), 401)


@app.errorhandler(403)
def forbidden(error):
    # return abort(403)
    return make_response(jsonify(result_ko='접근 금지!'
                                 , result_en='Forbidden!'
                                 , result=403), 403)


@app.route('/')
def hello_world():
    return redirect('/static/index.html')

@app.route('/robot.txt')
def robot():
    return redirect('/static/robot.txt')
