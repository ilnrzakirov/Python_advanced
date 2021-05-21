import unittest

from module_03_ci_culture_beginning.homework.decrypt import decrypt


class TestDecrypt(unittest.TestCase):

    def test_1(self):
        value = "абра-кадабра"
        string = "абра-кадабра."
        response = decrypt(string)
        self.assertEqual(value, response)

    def test_2(self):
        value = "абра-кадабра"
        string = "абраа..-кадабра"
        response = decrypt(string)
        self.assertEqual(value, response)

    def test_3(self):
        value = "абра-кадабра"
        string = "абраа..-.кадабра"
        response = decrypt(string)
        self.assertEqual(value, response)

    def test_4(self):
        value = "абра-кадабра"
        string = "абра--..кадабра"
        response = decrypt(string)
        self.assertEqual(value, response)

    def test_5(self):
        value = "абра-кадабра"
        string = "абрау...-кадабра"
        response = decrypt(string)
        self.assertEqual(value, response)

    def test_6(self):
        value = ""
        string = "абра........"
        response = decrypt(string)
        self.assertEqual(value, response)

    def test_7(self):
        value = "абра-кадабра"
        string = "абрау...-кадабра"
        response = decrypt(string)
        self.assertEqual(value, response)

    def test_8(self):
        value = "а"
        string = "абр......а."
        response = decrypt(string)
        self.assertEqual(value, response)

    def test_9(self):
        value = "23"
        string = "1..2.3"
        response = decrypt(string)
        self.assertEqual(value, response)

    def test_10(self):
        value = ""
        string = "."
        response = decrypt(string)
        self.assertEqual(value, response)