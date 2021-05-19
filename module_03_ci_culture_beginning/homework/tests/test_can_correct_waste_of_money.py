import unittest

import os

from module_02_linux.homework.hw_3_2 import app, storage, add


class TestWasteOfMoney(unittest.TestCase):
    def setUp(self) -> None:
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.base_url = "/add/"
        storage.update({"20210510": 1000, "20210310": 1500, "20201205": 100})

    def test_chek_add(self):
        add_date = "20000819"
        add_waste = "5000"
        response = self.app.get(self.base_url + add_date + os.sep + add_waste)
        self.assertTrue(storage[add_date], int(add_waste))

    def test_correct_calculate_year(self):
        calculate_year = "calculate/2021"
        response = self.app.get(calculate_year)
        response_text = response.data.decode()
        self.assertEqual(response_text, "2500")

    def test_correct_calculate_year_month(self):
        calculate_date = "calculate/2020/12"
        response = self.app.get(calculate_date)
        response_text = response.data.decode()
        self.assertEqual(response_text, "100")

    def test_chek_valid_date(self):
        add_date = "210508"
        add_waste = 5000
        with self.assertRaises(ValueError):
            add(add_date, add_waste)

    def test_calculate_when_empty(self):
        storage.clear()
        calculate_year = "calculate/2021"
        response = self.app.get(calculate_year)
        response_text = response.data.decode()
        self.assertEqual(response_text, "0")



