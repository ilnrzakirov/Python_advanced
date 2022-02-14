import codecs
import os
import flask
import subprocess
import shlex

from flask import current_app


app = flask.Flask(__name__)

def free_p():
    line = "lsof -i :5000 | grep Python | head -1 | awk '{print($2)}'"
    cmd = subprocess.run(['lsof', '-i', ':5000'], capture_output=True, encoding='utf-8')
    grep = subprocess.run(['grep', 'Python'], input=cmd.stdout, capture_output=True, encoding='utf-8')
    head = subprocess.run(['head', '-1'], input=grep.stdout, capture_output=True, encoding='utf-8')
    awk = subprocess.run(['awk', '{print($2)}'], input=head.stdout, capture_output=True, encoding='utf-8')
    if awk.stdout:
        os.kill(int(awk.stdout), 9)


@app.endpoint('test')
def test_endpoint():
    return 'Test endpoint was called!'


if __name__ == '__main__':
    free_p()
    app.run(debug=True)
