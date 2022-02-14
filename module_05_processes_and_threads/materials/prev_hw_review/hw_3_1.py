import shlex
import string
import subprocess
import sys
import io
from typing import List

from flask import Flask, request

app = Flask(__name__)


class Redirect:
    def __init__(self, io):
        self.io = io
        self.stderr = sys.stderr
        self.stdout = sys.stdout

    def __enter__(self):
        sys.stderr = self.io
        sys.stdout = self.io

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stderr = self.stderr
        sys.stdout = self.stdout


@app.route("/ps", methods=["GET"])
def _ps():
    arguments: List[str] = request.args.getlist("arg")
    arguments_cleaned = [shlex.quote(s) for s in arguments]
    command_str = f"ps {' '.join(arguments_cleaned)}"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)

    if result.returncode != 0:
        return "Something went wrong", 500

    output = result.stdout.decode()
    return string.Template("<pre>${output}</pre>").substitute(output=output)


output = io.StringIO()
with Redirect(output) as f:
    print("hi hi hi")

print(output.getvalue())

# if __name__ == "__main__":
#    app.run(debug=True)
