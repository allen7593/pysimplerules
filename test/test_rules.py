from pysrules.decorator import rule


@rule("test_agenda", conditions="ai.get_TestClass().a == 1")
def test_rule_1(ai):
    raise Exception("test_rule_1")


@rule("test_agenda", conditions="ai.get_TestClass().a == 2")
def test_rule_2(ai):
    raise Exception("test_rule_2")


# @rule("test_agenda", conditions="ai.get_TestClass().a == 3")
# def test_rule_3(ai):
#     raise Exception("test_rule_3")
