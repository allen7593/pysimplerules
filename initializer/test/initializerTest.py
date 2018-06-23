import unittest

from exceptions.initializeException import InitializeException
from exceptions.jsonValidationException import JsonValidationException
from initializer.initializer import Initializer


class TestDecorator(unittest.TestCase):

    def test_json_1(self):
        agenda_config = [
            {
                "items_provided": []
            },
        ]
        init = Initializer(agenda_config)
        with self.assertRaises(JsonValidationException) as cm:
            init.initialize()
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Missing 'agenda_name' in Config Json")

    def test_json_2(self):
        agenda_config = [
            {
                "agenda_name": "test_agenda",
            }
        ]
        init = Initializer(agenda_config)
        with self.assertRaises(JsonValidationException) as cm:
            init.initialize()
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Missing 'items_provided' in Config Json")

    def test_json_3(self):
        agenda_config = [
            {
                "agenda_name": "test_agenda",
                "items_provided": ""
            }
        ]
        init = Initializer(agenda_config)
        with self.assertRaises(JsonValidationException) as cm:
            init.initialize()
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "'items_provided' is not a list")

    def test_json_4(self):
        agenda_config = [
            {
                "agenda_name": "test_agenda",
                "items_provided": []
            }
        ]
        init = Initializer(agenda_config)
        with self.assertRaises(JsonValidationException) as cm:
            init.initialize()
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "'items_provided' cannot be empty")

    def test_json_5(self):
        init = Initializer(None)
        with self.assertRaises(InitializeException) as cm:
            init.initialize()
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Config List cannot be empty")

    def test_json_6(self):
        init = Initializer(" ")
        with self.assertRaises(InitializeException) as cm:
            init.initialize()
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Invalid type of Config List")


if __name__ == '__main__':
    unittest.main()
