import json
import logging

from flask import Flask, request

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def add_log():
    if request.method == 'POST':
        rd = request.form.to_dict()
        print(rd)
        rec = json.loads(rd['record'])
        record = logging.makeLogRecord(rec)
        return record


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
