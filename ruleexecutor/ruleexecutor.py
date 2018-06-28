from agendprepare.agendaitem import AgendaItems
from exceptions.ruleExecuterException import RuleExecutorException


class RuleExecutor:
    ai: AgendaItems

    def __init__(self, ai: AgendaItems):
        self.ai = ai

    def execute_all(self):
        if not self.ai:
            raise RuleExecutorException("No Agenda Item provided")

