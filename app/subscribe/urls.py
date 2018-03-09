from flask import Blueprint
import app.subscribe.controller as ctrl

subscribe = Blueprint('subscribe', __name__)

subscribe.add_url_rule('/addList', view_func=ctrl.addList, methods=['POST'])
