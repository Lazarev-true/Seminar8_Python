import view
import model
import table
import loading

j = ''
p = []

def quest():
    with open('students', 'r', encoding = 'utf-8') as f:
        lst = f.read().split('\n')

    while True:
        group = view.getNumb('Введите название группы: ')
        groups = []
        for i in lst:
            groups.append(i.split(' ')[3])
        if group not in groups:
            view.showinfo(f'Такой группы нет!')
            continue
        else:
            global k
            k = 0
            ls = []
            for i in lst:
                if group in i:
                    ls.append(i)
                    k += 1
                tab = table.show(ls)
            loading.progress()
            view.showinfo(tab)
            break
    second_quest(ls)


def second_quest(ls):
    global p
    global j
    if k > 1:
        while True:
            lastname = view.getNumb('Введите фамилию: ')
            lastnames = []
            for i in ls:
                lastnames.append(i.split(' ')[0])
            if lastname not in lastnames:
                view.showinfo(f'Студента с такой фамилией нет!')
                continue
            else:
                for i in ls:
                    if lastname in i:
                        j = i
                        FCs = i.split(' ')[0:3]
                        p.append(' '.join(FCs))
                        p.append(i.split(' ')[3])
                        p.append(i.split(' ')[4])
                        address = i.split(' ')[5:]
                        p.append(' '.join(address))
                        tab = table.show([i])
                loading.progress()
                view.showinfo(tab)
                break
        addendum()
    else:
        for i in ls:
            j = i
            FCs = i.split(' ')[0:3]
            p.append(' '.join(FCs))
            p.append(i.split(' ')[3])
            p.append(i.split(' ')[4])
            address = i.split(' ')[5:]
            p.append(' '.join(address))
            tab = table.show([i])
        
        addendum()

def addendum():

    view.showinfo(f'\nКакую информацию изменить?')
    
    view.showinfo(model.addendum_digit)

    while True:
        digit = view.getNumb('--> ')
        if not digit in model.to_change.keys():
            view.showinfo('Некорректный ввод')
            continue
        else:
            model.to_change[digit]()
            break

def student_FCs():
    p[0] = view.getNumb('Введите новые ФИО ')
    s = ' '.join(p)
    replacement(s)

def phone_number():
    p[2] = view.getNumb('Введите новый номер телефона ')
    s = ' '.join(p)
    replacement(s)

def student_address():
    p[3] = view.getNumb('Введите новый адрес студента ')
    s = ' '.join(p)
    replacement(s)

def replacement(s):
    with open('students', 'r', encoding = 'utf-8') as f:
        old_data = f.read()

    new_data = old_data.replace(j, s)

    with open('students', 'w', encoding = 'utf-8') as f:
        f.write(new_data)

    view.showinfo(f'\nДействие выполнено!')