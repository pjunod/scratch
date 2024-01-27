from flask import Flask, make_response
import datetime
app = Flask(__name__)


@app.route("/ts/")
def show_timestamp():
    return make_response(str(datetime.datetime.now()), 200)


@app.route("/date/future/days/<int:numdays>")
def show_future(numdays):
    future = str(datetime.datetime.now() + datetime.timedelta(days=numdays))
    return make_response(future, 200)
