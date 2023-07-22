import view as view
import note_ops as note_ops


def run():
    while True:
        view.menu()
        input_command = input()
        if input_command == '4':
            note_ops.show_note("all")
        elif input_command == '5':
            note_ops.show_note("id")
        elif input_command == '6':
            note_ops.show_note("date")
        elif input_command == '1':
            note_ops.create_note()
        elif input_command == '2':
            note_ops.show_note("all")
            note_ops.change_note()
        elif input_command == '3':
            note_ops.show_note("all")
            note_ops.del_notes()
        else:
            print("Завершение программы")
            break