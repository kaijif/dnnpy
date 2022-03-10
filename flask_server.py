import flask
import threading

from yolo import run_network

app = flask.Flask(__name__)

balls = []

threading.Thread(run_network, (global_balls,))


@app.route('/balls')
def hello():
	return {'balls': balls}

app.run()