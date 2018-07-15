from pysrules.decorator import rule


@rule("test_agenda", conditions="ai.get_TestClass().a == 1")
def foobar(ai):
    print(f"when a = {ai.TestClass.a}, execute method foobar()")


@rule("test_agenda", conditions="ai.get_TestClass().a == 2")
def foobar1(ai):
    print(f"when a = {ai.TestClass.a}, execute method foobar1()")
