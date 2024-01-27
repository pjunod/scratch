from flask import Flask, make_response
import datetime

app = Flask(__name__)


@app.route("/date/today")
def date_today():
    today = datetime.datetime.today()
    return make_response(f"Today's date is [{today}]", 200)