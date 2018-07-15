import sys
from importlib import reload

from decorator.dec import RuleDeck


class RuleReloader:
    def __init__(self, import_list: list):
        self.import_list = import_list
        self.fail_list = []

    def reload(self):
        rule_deck = RuleDeck()
        rule_deck.clear_rule_deck()
        for item in self.import_list:
            try:
                if item not in sys.modules:
                    __import__(item)
                else:
                    module = sys.modules[item]
                    reload(module)
            except Exception:
                self.fail_list.append(item)

    def get_fail_list(self):
        return self.fail_list
