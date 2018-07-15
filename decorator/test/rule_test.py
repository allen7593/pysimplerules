import unittest

from decorator.dec import rule
import decorator.dec as dec


@rule("1==1")
def test_func_1():
    print("1")


@rule("2==2")
def test_func_2():
    print("2")


class TestDecorator(unittest.TestCase):
    def test_second(self):
        rule_deck = dec.RuleDeck()
        for func in rule_deck:
            if func["agenda"]:
                func["func"]()


if __name__ == '__main__':
    mod = __import__("decorator.test.rule_test")
    unittest.main()
