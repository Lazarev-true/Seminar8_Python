import view
import model

f = open('students', 'a', encoding = 'utf-8')

def import_manually():
    chapter = view.getNumb('Введите ФИО--> ')
    chapter += ' '
    chapter += view.getNumb('Введите группу --> ')
    chapter += ' '
    chapter += view.getNumb('Введите номер телефона --> ')
    chapter += ' '
    chapter += view.getNumb('Введите адрес студента --> ')
    
    f.write(f'\n{chapter}')
    view.showinfo(f'\nГотово!')

def import_file():
    f.write(f"\n{open('new','r', encoding = 'utf-8').read()}")
    view.showinfo(f'\nГотово!')
    

def insert():
    view.showinfo(f'\nКак добавить?')
    
    view.showinfo(model.variants)

    while True:
        digit = view.getNumb('--> ')
        if not digit in model.seek.keys():
            view.showinfo('Некорректный ввод')
            continue
        else:
            model.variant[digit]()
            break

f.close
