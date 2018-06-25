import unittest
from unittest.mock import patch

from agendagroup.config.RuleConfigs import RuleConfigs
from agendprepare.agendaprepare import get_obj_name, AgendaPreparer
from exceptions.agendaprepareException import AgendaPrepareException


class TestClass: pass


class TestDecorator(unittest.TestCase):

    def test_get_obj_name_primitive(self):
        a = 1
        b = "b"
        c = True
        d = {"test": "test"}
        e = ["test", "test1"]
        f = 2.3

        self.assertEqual("a", get_obj_name(a))
        self.assertEqual("b", get_obj_name(b))
        self.assertEqual("c", get_obj_name(c))
        self.assertEqual("d", get_obj_name(d))
        self.assertEqual("e", get_obj_name(e))
        self.assertEqual("f", get_obj_name(f))

    def test_get_obj_name_class(self):
        obj = TestClass()
        self.assertEqual("TestClass", get_obj_name(obj))

    m_test_list = [
        {
            "agenda_name": "test_agenda",
            "items_provided": [TestClass, int, str, list, dict, set, tuple]
        }
    ]

    @patch('agendagroup.config.RuleConfigs.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_1(self, RuleConfigs):
        __import__("agendprepare.test.test_rules")
        preparer = AgendaPreparer()
        a1 = TestClass()
        ai = preparer.prepare_agenda("test_agenda", a1)
        self.assertEqual(a1, ai.TestClass)

    @patch('agendagroup.config.RuleConfigs.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_int(self, RuleConfigs):
        __import__("agendprepare.test.test_rules")
        preparer = AgendaPreparer()
        a1 = 1

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")

    @patch('agendagroup.config.RuleConfigs.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_str(self, RuleConfigs):
        __import__("agendprepare.test.test_rules")
        preparer = AgendaPreparer()
        a1 = "Test String"

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")

    @patch('agendagroup.config.RuleConfigs.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_float(self, RuleConfigs):
        __import__("agendprepare.test.test_rules")
        preparer = AgendaPreparer()
        a1 = 2.3

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")

    @patch('agendagroup.config.RuleConfigs.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_list(self, RuleConfigs):
        __import__("agendprepare.test.test_rules")
        preparer = AgendaPreparer()
        a1 = list()

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")

    @patch('agendagroup.config.RuleConfigs.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_dict(self, RuleConfigs):
        __import__("agendprepare.test.test_rules")
        preparer = AgendaPreparer()
        a1 = dict()

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")

    @patch('agendagroup.config.RuleConfigs.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_tuple(self, RuleConfigs):
        __import__("agendprepare.test.test_rules")
        preparer = AgendaPreparer()
        a1 = (1, 2)

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")

    @patch('agendagroup.config.RuleConfigs.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_set(self, RuleConfigs):
        __import__("agendprepare.test.test_rules")
        preparer = AgendaPreparer()
        a1 = set([])

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")


if __name__ == '__main__':
    unittest.main()
