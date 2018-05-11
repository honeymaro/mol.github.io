from flask import request, make_response, json, jsonify
import app.subscribe.model as model
from app import app
import traceback

def addList():
    email = request.form['email']
    is_ok = model.addList(email)

    if is_ok == 0:
        return make_response("OK", 200)

    elif is_ok == 1:
        return make_response("DUP", 210)

    else:
        return make_response("Fail", 410)
