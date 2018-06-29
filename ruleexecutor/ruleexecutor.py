from agendprepare.agendaitem import AgendaItems
from const import EXEC_ORDER, CONDITIONS, FUNC
from exceptions.ruleExecuterException import RuleExecutorException


class RuleExecutor:
    def execute_all(self, ai: AgendaItems):
        if not ai:
            raise RuleExecutorException("No Agenda Item provided")
        rules = ai.rules
        rules.sort(key=lambda x: x[EXEC_ORDER])
        for rule_item in rules:
            if eval(rule_item[CONDITIONS]):
                rule_item[FUNC](agenda_item=ai)
