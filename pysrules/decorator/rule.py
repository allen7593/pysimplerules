from pysrules.const import AGENDA, EXEC_ORDER, FUNC, CONDITIONS
from pysrules.decorator import Singleton


@Singleton
class RuleDeck:
    rule_deck: list
    i: int

    def __init__(self):
        self.i = 0
        self.rule_deck = list()

    def get_rule_deck(self):
        return self.rule_deck

    def clear_rule_deck(self):
        self.rule_deck = list()

    def add_new(self, item: dict):
        self.rule_deck.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.rule_deck):
            i = self.i
            self.i += 1
            return self.rule_deck[i]
        self.i = 0
        raise StopIteration()


def rule(agenda: str, exec_order: int = 0, conditions: str = "True"):
    def rule_dec(func):
        rule_deck = RuleDeck()
        rule_dict = dict()
        rule_dict[AGENDA] = agenda
        rule_dict[EXEC_ORDER] = exec_order
        rule_dict[FUNC] = func
        rule_dict[CONDITIONS] = conditions
        rule_deck.add_new(rule_dict)

        def wrapper(*args, **kargs):
            return func(*args, **kargs)

        return wrapper

    return rule_dec


def get_rules_agenda(agenda_name: str):
    rule_deck = RuleDeck()
    if rule_deck:
        return [rule_item for rule_item in rule_deck if rule_item[AGENDA] == agenda_name]
