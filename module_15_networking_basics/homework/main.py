from flask import Flask, render_template

from module_15_networking_basics.homework.models import init_db

app: Flask = Flask(__name__)



if __name__ == '__main__':
    init_db()
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
