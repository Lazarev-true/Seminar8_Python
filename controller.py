import view
import model

def start():

    view.showinfo('Информация о студентах')
    
    view.showinfo(f'Меню: \n{model.menu}')

    while True:
        button_selection = view.getNumb('Выберите команду --> ')
        print()
        if not button_selection in model.commands.keys():
            view.showinfo('Некорректный ввод')
            continue
        else:
            model.commands[button_selection]()
            break