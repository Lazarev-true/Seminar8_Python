import view
import table
import loading

j = ''

def first_quest():
    global j
    file = open('students', 'r', encoding = 'utf-8')
    lst = file.read().split('\n')
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
                    k += 1
                    j = i
                    ls.append(i)
                tab = table.show(ls)
            loading.progress()
            view.showinfo(tab)
            break
    second_quest(ls, j)


def second_quest(ls, j):
    if k > 1:
        while True:
            lastname = view.getNumb('Введите ФИО: ')
            lastnames = []
            for i in ls:
                FCs = i.split(' ')[0:3]
                lastnames.append(' '.join(FCs))
            if lastname not in lastnames:
                view.showinfo(f'Студента с таким ФИО нет!')
                continue
            else:
                for i in ls:
                    if lastname in i:
                        j = i
                removal(j)                
                break
    else:
        removal(j)

def removal(j):
    with open('students', 'r', encoding = 'utf-8') as f:
        old_data = f.read()

    s = j + '\n'
    s_del = ''

    new_data = old_data.replace(s, s_del)

    with open('students', 'w', encoding = 'utf-8') as f:
        f.write(new_data)

    view.showinfo('Удалено!')