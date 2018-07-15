from pysrules.decorator import rule


@rule("1==1")
def test_func_1():
    print("1")


@rule("2==2")
def test_func_2():
    print("2")