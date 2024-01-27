from flask import Flask, make_response

app = Flask(__name__)

@app.route("/times4/<int:num>")
def times4(num):
    resp = make_response(str(num * 4), 200)
    return resp