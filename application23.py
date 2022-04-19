import simple_websocket
import flask
import platform
import time

app = flask.Flask(__name__)

@app.route('/')
def index():
    host = flask.request.host
    hostname = platform.platform()
    Time= time.strftime("%H:%M:%S")
    return Time+" Serving from "+host+" ("+hostname+")\n"

@app.route('/echo', websocket=True)
def echo():
    ws = simple_websocket.Server(flask.request.environ)
    try:
        while True:
            data = ws.receive()
            ws.send(data)
    except simple_websocket.ConnectionClosed:
        pass
    return ''


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8211,debug=True)