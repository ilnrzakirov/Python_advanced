"""
Ещё раз рассмотрим Flask endpoint, принимающий код на питоне и исполняющий его.
1. Напишите для него Flask error handler,
    который будет перехватывать OSError и писать в log файл exec.log
    соответствую ошибку с помощью logger.exception
2. Добавьте отдельный exception handler
3. Сделайте так, что в случае непустого stderr (в программе произошла ошибка)
    мы писали лог сообщение с помощью logger.error
4. Добавьте необходимые debug сообщения
5. Инициализируйте basicConfig для записи логов в stdout с указанием времени
"""
import logging
import shlex
import subprocess
from typing import Optional

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired

logger = logging.getLogger("exec")
app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(default=10)


def run_python_code_in_subprocess(code: str, timeout: int) -> str:
    command = f'python3 -c "{code}"'
    command = shlex.split(command)
    process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
    )
    logger.debug("run cdm")
    outs, errs = process.communicate(timeout=timeout)
    logger.debug(f"End {process.pid} , exit code {process.returncode}")

    if process.returncode > 0:
        logger.error(f"{errs.decode(encoding='utf-8')}")
    else:
        logger.debug(f"{outs.decode(encoding='utf-8')}")
    return outs.decode()


@app.route("/run_code", methods=["POST"])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        logger.debug("form is valid")
        code = form.code.data
        timeout = form.timeout.data
        stdout = run_python_code_in_subprocess(code=code, timeout=timeout)
        return f"Stdout: {stdout}"

    logger.debug("Form is not valid")
    return f"Bad request. Error = {form.errors}", 400

@app.errorhandler(OSError)
def handle_exception(e: OSError):
    original: Optional[Exception] = getattr(e, "original_exception", None)

    if isinstance(original, OSError):
        logger.exception(f"{e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="exec.log", format='%(asctime)s %(message)s')
    app.config["WTF_CSRF_ENABLED"] = False
    logger.debug("Start")
    app.run(debug=True)
