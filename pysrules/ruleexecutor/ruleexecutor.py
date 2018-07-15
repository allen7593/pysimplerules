from pysrules.agendprepare import AgendaItems
from pysrules.const import EXEC_ORDER, CONDITIONS, FUNC
from pysrules.exceptions import RuleExecutorException


class RuleExecutor:
    def execute_all(self, ai: AgendaItems):
        if not ai:
            raise RuleExecutorException("No Agenda Item provided")
        rules = ai.rules
        rules.sort(key=lambda x: x[EXEC_ORDER])
        for rule_item in rules:
            if eval(rule_item[CONDITIONS]):
                rule_item[FUNC](ai=ai)
