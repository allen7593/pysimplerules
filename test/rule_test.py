import unittest

from pysrules.decorator import RuleDeck


class TestDecorator(unittest.TestCase):
    def test_second(self):
        __import__("test.test_rule_1")
        rule_deck = RuleDeck()
        for func in rule_deck:
            if func["agenda"]:
                func["func"]()


if __name__ == '__main__':
    unittest.main()
