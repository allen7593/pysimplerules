from const import AGENDA_NAME
from exceptions.ruleConfigException import RuleConfigException


class RuleConfigs:
    class __RuleConfigs:
        def __init__(self, config_list: list):
            self.config_list = config_list

        def get_rule_config(self):
            return self.config_list

        def get_rule_config_by_agenda(self, agenda_name: str) -> dict:
            for item in self.config_list:
                if item[AGENDA_NAME] == agenda_name:
                    return item
            raise RuleConfigException("Agenda name: {} does not exist".format(agenda_name))

    instance = None

    def __init__(self, config_list):
        if not RuleConfigs.instance:
            RuleConfigs.instance = RuleConfigs.__RuleConfigs(config_list)
        else:
            RuleConfigs.instance.config_list = config_list

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)
