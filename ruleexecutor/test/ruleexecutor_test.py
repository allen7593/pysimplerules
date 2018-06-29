import unittest
from unittest.mock import patch

from agendagroup.config.RuleConfigs import RuleConfigs
from agendprepare.agendaprepare import AgendaPreparer
from ruleexecutor.ruleexecutor import RuleExecutor


class TestClass: pass


class TestDecorator(unittest.TestCase):
    m_test_list = [
        {
            "agenda_name": "test_agenda",
            "items_provided": [TestClass, int, str, list, dict, set, tuple, float]
        }
    ]

    @patch('agendagroup.config.RuleConfigs.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_rule_executor_1(self, RuleConfigs):
        __import__("agendprepare.test.test_rules")
        preparer = AgendaPreparer()
        a1 = TestClass()
        a1.a = 1
        ai = preparer.prepare_agenda("test_agenda", a1)
        executor = RuleExecutor()

        with self.assertRaises(Exception) as cm:
            executor.execute_all(ai)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "test_rule_1")

    @patch('agendagroup.config.RuleConfigs.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_rule_executor_2(self, RuleConfigs):
        __import__("agendprepare.test.test_rules")
        preparer = AgendaPreparer()
        a1 = TestClass()
        a1.a = 2
        ai = preparer.prepare_agenda("test_agenda", a1)
        executor = RuleExecutor()

        with self.assertRaises(Exception) as cm:
            executor.execute_all(ai)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "test_rule_2")


if __name__ == '__main__':
    unittest.main()
