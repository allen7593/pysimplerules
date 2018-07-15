import unittest
from unittest.mock import patch

from pysrules.agendprepare import AgendaPreparer
from pysrules.ruleReloader import RuleReloader
from pysrules.ruleexecutor import RuleExecutor
from pysrules.agendagroup.ruleConfigs import RuleConfigs


class TestClass: pass


class TestDecorator(unittest.TestCase):
    m_test_list = [
        {
            "agenda_name": "test_agenda",
            "items_provided": [TestClass]
        }
    ]

    def setUp(self):
        import_list = ["test.test_rules"]
        reloader = RuleReloader(import_list)
        reloader.reload()

    @patch('pysrules.agendagroup.ruleConfigs.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_rule_executor_1(self, RuleConfigs):
        preparer = AgendaPreparer()
        test_obj_1 = TestClass()
        test_obj_1.a = 1
        ai = preparer.prepare_agenda("test_agenda", test_obj_1)
        executor = RuleExecutor()

        with self.assertRaises(Exception) as cm:
            executor.execute_all(ai)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "test_rule_1")

    @patch('pysrules.agendagroup.ruleConfigs.RuleConfigs', return_value=RuleConfigs(m_test_list))
    def test_rule_executor_2(self, RuleConfigs):
        preparer = AgendaPreparer()
        test_obj_2 = TestClass()
        test_obj_2.a = 2
        ai = preparer.prepare_agenda("test_agenda", test_obj_2)
        executor = RuleExecutor()

        with self.assertRaises(Exception) as cm:
            executor.execute_all(ai)
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "test_rule_2")


if __name__ == '__main__':
    unittest.main()
