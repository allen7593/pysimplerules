import inspect

from agendagroup.config.RuleConfigs import RuleConfigs
from agendprepare.agendaitem import AgendaItems
from const import ITEMS_PROVIDED
from decorator.dec import get_rules_agenda
from exceptions.agendaprepareException import AgendaPrepareException


def get_obj_name(obj) -> str:
    if type(obj) in [int, str, list, dict, set, tuple, float]:
        raise AgendaPrepareException("Primitive types are not supported")
    if inspect.isclass(type(obj)):
        return str(type(obj).__name__)


class AgendaPreparer:
    def __init__(self):
        self.rule_config_ins = RuleConfigs()
        if not self.rule_config_ins:
            raise AgendaPrepareException("Rule Config cannot be empty, please initialize rule config using Initializer")

    def prepare_agenda(self, agenda_name: str, *args) -> AgendaItems:
        agenda_item = self.rule_config_ins.get_rule_config_by_agenda(agenda_name)
        ai = AgendaItems(agenda_item)
        rules = get_rules_agenda(agenda_name)
        ai.rules = rules
        for obj in args:
            if type(obj) in agenda_item[ITEMS_PROVIDED]:
                obj_name = get_obj_name(obj)
                setattr(ai, obj_name, obj)
                f = lambda: getattr(ai, obj_name)
                f.__name__ = "get_" + obj_name
                setattr(ai, "get_" + obj_name, f)
        return ai
