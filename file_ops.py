import Note

path = 'notes.csv'


def read_file():
    try:
        return_notes = []
        file = open(path, 'r', encoding='utf-8')
        notes = file.read().strip().split('\n')
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(id=split_n[0], title=split_n[1], body=split_n[2], date=split_n[3])
            return_notes.append(note)
    except Exception:
        print('журнал пуст!\n')
    finally:
        return return_notes


def save_to_file(array, mode):
    file = open(path, mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open(path, mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_save(notes))
        file.write('\n')
    file.close()
