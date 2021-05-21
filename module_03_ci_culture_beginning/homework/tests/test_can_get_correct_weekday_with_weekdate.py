import unittest

import datetime

from module_02_linux.homework.hw_2_4_hello_world_with_day import app


class TestWeekDay(unittest.TestCase):
    def setUp(self) -> None:
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_week_day(self):
        username = "username"
        week = {0: "Хорошего понедельника", 1: "Хорошего вторника", 2: "Хорошей среды", 3: "Хорошего четверга",
                4: "Хорошей пятницы", 5: "Хорошей субботы", 6: "Хорошего воскресенья"}
        today = datetime.datetime.today().weekday()
        today_to_text = week[today]
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(today_to_text in response_text)
