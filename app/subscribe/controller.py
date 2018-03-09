from flask import request, make_response, json, jsonify
import app.subscribe.model as model
from app import app
import traceback

def addList():
    email = request.form['email']
    is_ok = model.addList(email)

    if is_ok == True:
        return make_response("OK", 200)

    else:
        return make_response("Fail", 410)
