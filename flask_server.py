import flask
import concurrent.futures

from yolo import run_network

app = flask.Flask(__name__)

balls = []

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(run_network, balls)


@app.route('/balls')
def hello():
	return {'balls': balls}

app.run()