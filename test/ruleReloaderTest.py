import unittest

from pysrules.decorator import RuleDeck
from pysrules.ruleReloader.rulereloader import RuleReloader


class TestClass: pass


class TestRuleReload(unittest.TestCase):
    import_list = [
        "test.test_rules"
    ]

    def test_rule_reload(self):
        reloader = RuleReloader(self.import_list)
        reloader.reload()
        deck = RuleDeck()
        print(deck.get_rule_deck())

        reloader = RuleReloader(self.import_list)
        reloader.reload()
        print(deck.get_rule_deck())


if __name__ == '__main__':
    unittest.main()
