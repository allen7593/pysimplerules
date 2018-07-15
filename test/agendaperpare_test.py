import unittest
from unittest.mock import patch

from pysrules.agendagroup import RuleConfigs
from pysrules.agendprepare import get_obj_name, AgendaPreparer
from pysrules.exceptions import AgendaPrepareException


class TestClass: pass


class TestDecorator(unittest.TestCase):

    def test_get_obj_name_class(self):
        obj = TestClass()
        self.assertEqual("TestClass", get_obj_name(obj))

    m_test_list = [
        {
            "agenda_name": "test_agenda",
            "items_provided": [TestClass, int, str, list, dict, set, tuple, float]
        }
    ]

    @patch('pysrules.agendagroup.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_1(self, RuleConfigs):
        __import__("test.test_rules")
        preparer = AgendaPreparer()
        a1 = TestClass()
        ai = preparer.prepare_agenda("test_agenda", a1)
        self.assertEqual(a1, ai.TestClass)

    @patch('pysrules.agendagroup.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_int(self, RuleConfigs):
        __import__("test.test_rules")
        preparer = AgendaPreparer()
        a1 = 1

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")

    @patch('pysrules.agendagroup.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_str(self, RuleConfigs):
        __import__("test.test_rules")
        preparer = AgendaPreparer()
        a1 = "Test String"

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")

    @patch('pysrules.agendagroup.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_float(self, RuleConfigs):
        __import__("test.test_rules")
        preparer = AgendaPreparer()
        a1 = 2.3

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")

    @patch('pysrules.agendagroup.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_list(self, RuleConfigs):
        __import__("test.test_rules")
        preparer = AgendaPreparer()
        a1 = list()

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")

    @patch('pysrules.agendagroup.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_dict(self, RuleConfigs):
        __import__("test.test_rules")
        preparer = AgendaPreparer()
        a1 = dict()

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")

    @patch('pysrules.agendagroup.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_tuple(self, RuleConfigs):
        __import__("test.test_rules")
        preparer = AgendaPreparer()
        a1 = (1, 2)

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")

    @patch('pysrules.agendagroup.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_set(self, RuleConfigs):
        __import__("test.test_rules")
        preparer = AgendaPreparer()
        a1 = set([])

        with self.assertRaises(AgendaPrepareException) as cm:
            ai = preparer.prepare_agenda("test_agenda", a1)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Primitive types are not supported")

    @patch('pysrules.agendagroup.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_agenda_prepare_class_get(self, RuleConfigs):
        __import__("test.test_rules")
        preparer = AgendaPreparer()
        a1 = TestClass()
        ai = preparer.prepare_agenda("test_agenda", a1)
        self.assertEqual(a1, ai.get_TestClass())


if __name__ == '__main__':
    unittest.main()
