import time

from flask import Flask, jsonify

app = Flask(__name__)

def create_message(timestamp):
    return {
            "message": "Automate all the Things",
            "time": timestamp
            }

@app.route("/")
def get_message():
    now = int(time.time())
    msg = create_message(now)
    return jsonify(msg)
