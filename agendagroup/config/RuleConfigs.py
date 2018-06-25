from const import AGENDA_NAME
from decorator.dec.singleton import singleton
from exceptions.ruleConfigException import RuleConfigException


@singleton
class RuleConfigs:
    def __init__(self, config_list: list):
        self.config_list = config_list

    def get_rule_config(self):
        return self.config_list

    def get_rule_config_by_agenda(self, agenda_name: str) -> dict:
        for item in self.config_list:
            if item[AGENDA_NAME] == agenda_name:
                return item
        raise RuleConfigException("Agenda name: {} does not exist".format(agenda_name))
