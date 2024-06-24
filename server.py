import flask
import requests
from flask import request

app = flask.Flask(__name__)


@app.route('/', methods=['GET',"HEAD","POST","PUT","DELETE","CONNECT","OPTIONS","TRACE","PATCH"])
def index():
    url = request.args.get('q')
    print(url)
    headers = dict(request.headers)
    print(headers)
    data = request.data
    print(data)
    method = request.method
    print(method)

    r = requests.request(method=method, url=url, data=data)
    print(r)

    print(r.text)
    return r.text
