rule_deck = []


def rule(agenda: str, exec_order: int = 0):
    def rule_dec(func):
        rule_dict = dict()
        rule_dict["agenda"] = agenda
        rule_dict["exec_order"] = exec_order
        rule_dict["func"] = func
        rule_deck.append(rule_dict)

        def wrapper(*args, **kargs):
            return func(*args, **kargs)

        return wrapper

    return rule_dec
