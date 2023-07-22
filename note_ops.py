import file_ops as file_ops
import Note


def create_note():
    title = input("введите заголовок: ")
    body = input("введите заметку: ")
    note = Note.Note(title=title, body=body)
    notes = file_ops.read_file()
    for n in notes:
        if Note.Note.get_id(note) == Note.Note.get_id(n):
            Note.Note.set_id(note)
    notes.append(note)
    file_ops.save_to_file(notes, 'a')
    print("Записано!\n")


def show_note(text):
    notes = file_ops.read_file()
    if notes:
        if text == "all":
            print("\nСписок заметок:")
            for n in notes:
                print(Note.Note.print_all_notes(n))

        elif text == "id":
            for n in notes:
              print("id: ", Note.Note.get_id(n))
            id = input("\nвведите id заметки: ")
            flag = True
            for n in notes:
                if id == Note.Note.get_id(n):
                    print(Note.Note.print_note(n) + '\n')
                    flag = False
            if flag:
                print("Нет заметки с таким id\n")

        elif text == "date":
            date = input("Введите дату в формате: dd.mm.yyyy: ")
            flag = True
            for n in notes:
                date_note = str(Note.Note.get_date(n))
                if date == date_note[:10]:
                    print(Note.Note.map_note(n))
                    flag = False
            if flag:
                print("Нет заметки с такой датой\n")
        else:
            print("Журнал пуст!\n")


def del_notes():
    id = input("Введите ID удаляемой заметки: ")
    notes = file_ops.read_file()
    flag = False

    for n in notes:
        if id == Note.Note.get_id(n):
            notes.remove(n)
            flag = True

    if flag:
        file_ops.save_to_file(notes, 'a')
        print("Заметка с id: ", id, " успешно удалена!")
    else:
        print("нет такого id")


def change_note():
    id = input("Введите ID изменяемой заметки: ")
    notes = lF.read_file()
    flag = True
    notes_new = []
    for n in notes:
        if id == Note.Note.get_id(n):
            n.title = input("измените  заголовок:\n")
            n.body = input("измените  описание:\n")
            Note.Note.set_date(n)
            flag = False
        notes_new.append(n)

    if flag:
        file_ops.save_to_file(notes_new, 'a')
        print("Заметка с id: ", id, " успешно изменена!")
    else:
        print("нет такого id")
