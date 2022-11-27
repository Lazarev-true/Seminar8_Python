import table
import search
import change
import import_students
import delete_line

menu = '1 - список студентов\n\
2 - поиск по списку\n\
3 - изменение информации\n\
4 - добавление новых студентов\n\
5 - удаление из списка'

commands = {'1': table.table_output, 
            '2': search.request_digit,
            '3': change.quest, 
            '4': import_students.insert, 
            '5': delete_line.first_quest
            }

search_digit = '1 - по фамилии\n\
2 - по группе\n\
3 - по номеру телефона\n\
4 - по адресу'

seek = {'1': search.by_full_name, 
        '2': search.by_group,
        '3': search.by_number, 
        '4': search.by_address,
        }

addendum_digit = '1 - ФИО\n\
2 - номер телефона\n\
3 - адрес'

to_change = {'1': change.student_FCs, 
        '2': change.phone_number,
        '3': change.student_address
        }

variants = '1 - из другого файла\n\
2 - вручную'

variant = { '1': import_students.import_file,
            '2': import_students.import_manually
           }