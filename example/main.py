from example.agendaConfig import agenda_config
from example.importList import import_list
from example.selfDefinedClass import TestClass
from pysrules.agendprepare import AgendaPreparer
from pysrules.initializer import Initializer
from pysrules.ruleReloader import RuleReloader
from pysrules.ruleexecutor import RuleExecutor


init = Initializer(agenda_config)
init.initialize()

reloader = RuleReloader(import_list)
reloader.reload()

preparer = AgendaPreparer()
test_ins = TestClass()
test_ins.a = 1
ai = preparer.prepare_agenda("test_agenda", test_ins)

executor = RuleExecutor()
executor.execute_all(ai)

preparer2 = AgendaPreparer()
test_ins.a = 2
ai2 = preparer.prepare_agenda("test_agenda", test_ins)

executor.execute_all(ai2)

