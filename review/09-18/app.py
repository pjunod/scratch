from flask import Flask, make_response
import requests

app = Flask(__name__)


@app.route("/foo/<string:url>")
def get_foo(url):
    if not url.startswith("https://"):
        url = "https://" + url
    req = requests.get(url)
    resp = make_response(req.text, 200)
    return resp