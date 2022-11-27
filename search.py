import view
import model
import table
import loading

with open('students', 'r', encoding = 'utf-8') as f:
    lst = f.read().split('\n')

def by(w, ls):
    while True:
        word = view.getNumb(f'Введите {w}: ')
        if word not in ls:
            view.showinfo(f'Ошибочный ввод')
            continue
        else:
            l = []
            for i in lst:
                if (word in i) and (word in ls):
                    l.append(i)
                tab = table.show(l)
            loading.progress()
            view.showinfo(tab)
            break

def by_full_name():
    ls = []
    for i in lst:
        ls.append(i.split(' ')[0])
    by('фамилию', ls)
            

def by_group():
    ls = []
    for i in lst:
        ls.append(i.split(' ')[3])
    by('группу', ls)

def by_number():
    ls = []
    for i in lst:
        ls.append(i.split(' ')[4])       
    by('номер телефона', ls)

def by_address():
    ls = []
    for i in lst:
        address = i.split(' ')[5:]
        ls.append(' '.join(address))
    by('адрес', ls)

def request_digit():
    view.showinfo('Выберите цифру:')
    
    view.showinfo(model.search_digit)

    while True:
        digit = view.getNumb('Тут --> ')
        print()
        if not digit in model.seek.keys():
            view.showinfo('Некорректный ввод')
            continue
        else:
            model.seek[digit]()
            break
