"""
Для каждого поля и валидатора в endpoint /registration напишите по unit-тесту,
    который проверит, что валидатор и правда работает (т.е. мы должны проверить,
    что существует набор данных, которые проходят валидацию, и такие,
    которые валидацию не проходят)
"""
import unittest

from module_04_flask.hw.hw_1_2 import app


class TestForm(unittest.TestCase):
    def setUp(self) -> None:
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = "/registration"

    def test_bad_email(self):
        argum = {"email": "testtest.com", "phone": 9995554442, "name": "test", "address": "test", "index": 444}
        response = self.app.post(self.base_url, json=argum)
        self.assertTrue(response, 400)

    def test_email(self):
        argum = {"email": "test@test.com", "phone": 9995554442, "name": "test", "address": "test", "index": 444}
        response = self.app.post(self.base_url, json=argum)
        self.assertTrue(response, 200)

    def test_phone(self):
        argum = {"email": "test@test.com", "phone": 9995554442, "name": "test", "address": "test", "index": 444}
        response = self.app.post(self.base_url, json=argum)
        self.assertTrue(response, 200)

    def test_bad_phone(self):
        argum = {"email": "test@test.com", "phone": 99955544425, "name": "test", "address": "test", "index": 444}
        response = self.app.post(self.base_url, json=argum)
        self.assertTrue(response, 400)

    def test_bad2_phone(self):
        argum = {"email": "test@test.com", "phone": "9995554442f", "name": "test", "address": "test", "index": 444}
        response = self.app.post(self.base_url, json=argum)
        self.assertTrue(response, 400)

    def test_bad_name(self):
        argum = {"email": "test@test.com", "phone": 99955544425, "name": "", "address": "test", "index": 444}
        response = self.app.post(self.base_url, json=argum)
        self.assertTrue(response, 400)

    def test_bad_address(self):
        argum = {"email": "test@test.com", "phone": 99955544425, "name": "test", "address": "", "index": 444}
        response = self.app.post(self.base_url, json=argum)
        self.assertTrue(response, 400)

    def test_bad_index(self):
        argum = {"email": "test@test.com", "phone": 99955544425, "name": "test", "address": "test", "index": "fh"}
        response = self.app.post(self.base_url, json=argum)
        self.assertTrue(response, 400)

# Зачёт!
