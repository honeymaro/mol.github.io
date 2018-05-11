from app import app
from gevent.wsgi import WSGIServer

http = WSGIServer(('0.0.0.0', 443), app
        , keyfile='cert/langchain_io.key'
        , certfile='cert/langchain_io.crt'
        )
http.serve_forever()
