from const import AGENDA_NAME, ITEMS_PROVIDED


class AgendaItems:
    def __init__(self, agenda_item: dict):
        self.agenda_name = agenda_item[AGENDA_NAME]
        self.items_provided = agenda_item[ITEMS_PROVIDED]
