from app import app
from gevent.wsgi import WSGIServer

http = WSGIServer(('0.0.0.0', 80), app)
http.serve_forever()
