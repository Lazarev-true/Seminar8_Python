import view
import loading
from prettytable import PrettyTable

def table_output():
    f = open('students', 'r', encoding = 'utf-8')
    lst = f.read().split('\n')

    loading.progress()

    table = show(lst)
    
    view.showinfo(table)
       
    f.close()

def show(lst):
        students = []

        for i in lst:
            FCs = i.split(' ')[0:3]
            students.append(' '.join(FCs))
            students.append(i.split(' ')[3])
            students.append(i.split(' ')[4])
            address = i.split(' ')[5:]
            students.append(' '.join(address))

        head = ('FCs', 'Group', 'Number', 'Address')
        tab = PrettyTable(head)

        while students:
            tab.add_row(students[:4])
            students = students[4:]

        return tab