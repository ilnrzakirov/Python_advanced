"""
Ещё раз повторите вызовы через Postman к endpoint, которые мы разбирали на уроках.
"""
import json

import wtforms.fields

from urllib.parse import unquote_plus

from flask import Flask, request

from flask_wtf.form import FlaskForm

from wtforms.validators import InputRequired, Email, NumberRange

app = Flask(__name__)


@app.route("/sum", methods=["POST"])
def sum1():
    array1 = request.form.getlist("array1", type=int)
    array2 = request.form.getlist("array2", type=int)

    result = ",".join(str(a1 + a2) for (a1, a2) in zip(array1, array2))

    return f"Array of sums is [{result}]"


@app.route("/sum2", methods=["POST"])
def sum2():
    form_data = request.get_data(as_text=True)
    request_data = unquote_plus(form_data)

    arrays = {}

    for encoded in request_data.split("&"):
        key, value = encoded.split("=")

        arrays[key] = [int(item) for item in value.split(",")]

    result = ",".join(str(a1 + a2) for a1, a2 in zip(arrays["array1"], arrays["array2"]))

    return result


@app.route("/sum3", methods=["POST"])
def sum3():
    form_data = request.get_data(as_text=True)

    data_object = json.loads(form_data)

    result = ",".join(str(a1 + a2) for a1, a2 in zip(data_object["array1"], data_object["array2"]))

    return result


class RegistrationForm(FlaskForm):
    email = wtforms.StringField(validators=[InputRequired(), Email()])
    phone = wtforms.IntegerField(validators=[InputRequired(), NumberRange(min=1000000000, max=9999999999)])
    name = wtforms.StringField(validators=[InputRequired()])
    address = wtforms.StringField(validators=[InputRequired()])
    index = wtforms.IntegerField()
    comment = wtforms.StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successful registered user {email} with phone +7{phone}"

    return f"Invalid input {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
