from datetime import datetime


class Note:
    id_counter = 1

    def __init__(self, id=str(id_counter), title="", body="",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date
        Note.id_counter += 1

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_date(self):
        return self.date

    def set_title(self):
        self.title = self

    def set_body(self):
        self.body = self

    def set_id(self):
        self.id = str(Note.id_counter)

    def set_date(self):
        self.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_save(self):
        return self.id + ';' + self.title + ';' + self.body + ';' + self.date

    def print_note(self):
        return '\nID: ' + self.id + '\n' + 'Название: ' + self.title + '\n' + 'Описание: ' + self.body + '\n' + \
            'Дата публикации: ' + self.date

    def print_all_notes(self):
        return 'ID: ' + self.id + '. ' + 'Название: ' + self.title
