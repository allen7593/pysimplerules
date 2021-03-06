from pysrules.agendagroup import RuleConfigs
from pysrules.const import AGENDA_NAME, ITEMS_PROVIDED
from pysrules.exceptions import InitializeException, JsonValidationException


class Initializer:
    def __init__(self, config_item):
        self.config_list = config_item

    def initialize(self):
        if self.config_list:
            if type(self.config_list) is list:
                for config_item in self.config_list:
                    if self.__validate_json(config_item):
                        config = RuleConfigs(self.config_list)
            else:
                raise InitializeException("Invalid type of Config List")
        else:
            raise InitializeException("Config List cannot be empty")

    def __validate_json(self, config_json: dict):
        if AGENDA_NAME not in config_json:
            raise JsonValidationException("Missing 'agenda_name' in Config Json")
        elif ITEMS_PROVIDED not in config_json:
            raise JsonValidationException("Missing 'items_provided' in Config Json")
        elif type(config_json[ITEMS_PROVIDED]) is not list:
            raise JsonValidationException("'items_provided' is not a list")
        elif not config_json[ITEMS_PROVIDED]:
            raise JsonValidationException("'items_provided' cannot be empty")
        return True
