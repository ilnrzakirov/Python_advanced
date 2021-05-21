import unittest

from module_03_ci_culture_beginning.homework.person import Person


class TestPerson(unittest.TestCase):
    def test_get_age(self):
        person = Person("User", 1990, "Kazan")
        age = person.get_age()
        self.assertEqual(age, 31)

    def test_get_age_for_raise(self):
        person = Person("User", -5, "Kazan")
        with self.assertRaises(ValueError):
            person.get_age()

    def test_get_age_for_type(self):
        person = Person("User", "Old", "Kazan")
        with self.assertRaises(TypeError):
            person.get_age()

    def test_gen_name(self):
        person = Person("User", "Old", "Kazan")
        self.assertEqual("User", person.get_name())

    def test_update_name(self):
        person = Person("User", "Old", "Kazan")
        person.set_name("User2")
        self.assertEqual("User2", person.name)

    def test_update_adress(self):
        person = Person("User", "Old", "Kazan")
        person.set_address("Moscow")
        self.assertEqual("Moscow", person.address)

    def test_get_adress(self):
        person = Person("User", "Old", "Kazan")
        self.assertEqual("Kazan", person.get_address())

    def test_homeless(self):
        person = Person("User", "Old")
        self.assertEqual(person.is_homeless(), True)
