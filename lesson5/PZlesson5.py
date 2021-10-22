"""
Практическое задание к уроку 5:
"""
"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка.
"""
# import sys
#
# try:
#     with open('PZ5_ex1.txt', 'w', encoding='utf-8') as file_obj_1:
#         string_file = True
#         while string_file:
#             string_file = input('Введите строку для записи в файл (для окончания введите пустую строку):')
#             file_obj_1.write(string_file + '\n')
# except Exception as e:
#     print(f'Ошибка: {e}')

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""
# import sys
#
# try:
#     with open('PZ5_ex2.txt', 'r', encoding='utf-8') as file_obj_2:
#         print(f'-------------- Содержимое файла --------------\n{file_obj_2.read()}')
#         file_obj_2.seek(0)
#         poem = file_obj_2.readlines()
#         count_str = 0
#         print(f'-------------- Расчеты --------------')
#         print(f'Количество строк в файле = {len(poem)}')
#         for stroka in poem:
#             stroka = stroka.rstrip('\n')
#             count_str += 1
#             print(f'Количество слов в {count_str} строке = {len(stroka.split())}')
# except Exception as e:
#     print(f'Ошибка: {e}')

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""
# import sys
# from functools import reduce
#
#
# try:
#     with open('PZ5_ex3.txt', 'r', encoding='utf-8') as file_obj_3:
#         list_salary = []
#         print(f'Сотрудники с окладом менее 20 тыс.')
#         for line in file_obj_3.readlines():
#             worker, salary = line.split(', ')
#             if int(salary) < 20000:
#                 print(worker)
#             list_salary.append(int(salary))
#         avg_salary = reduce(lambda x, y: x + y, list_salary) / len(list_salary)
#         print(f'Средняя величина дохода сотрудников = {avg_salary}')
# except Exception as e:
#     print(f'Ошибка: {e}')

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""
# import sys
#
# number_eng_rus = {'One': 'Один',
#                   'Two': 'Два',
#                   'Three': 'Три',
#                   'Four': 'Четыре'
#                   }
#
# try:
#     with open('PZ5_ex4.txt', 'r', encoding='utf-8') as file_obj_r_4, \
#             open('PZ5_ex4_new.txt', 'w', encoding='utf-8') as file_obj_w_4:
#         for line in file_obj_r_4.readlines():
#             line = line.rstrip('\n')
#             letter, number = line.split(' — ')
#             file_obj_w_4.write(f'{number_eng_rus[letter]} - {number}\n')
# except Exception as e:
#     print(f'Ошибка: {e}')

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
# import sys, random
#
# try:
#     with open('PZ5_ex5.txt', 'w+', encoding='utf-8') as file_obj_5:
#         for i in range(5):
#             file_obj_5.writelines(str(random.randint(0, 100)) + ' ')
#         file_obj_5.seek(0)
#         list_number = file_obj_5.read().split()
#         list_number = [int(number) for number in list_number]
#         print(f'Список: {list_number}')
#         print(f'Сумма всех элементов списка = {sum(list_number)}')
# except Exception as e:
#     print(f'Ошибка: {e}')

"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
# import sys
#
# try:
#     with open('PZ5_ex6.txt', 'r', encoding='utf-8') as file_obj_6:
#         dict_subjects = {}
#         for line in file_obj_6.readlines():
#             line = line.rstrip('\n')
#             subject, lessons = line.split(':')
#             sum_hours = 0
#             for hour in lessons.split():
#                 hour_number = ''
#                 for ind in range(len(hour)):
#                     if hour[ind].isdigit():
#                         hour_number += str(hour[ind])
#                 if hour_number != '':
#                     sum_hours += int(hour_number)
#             dict_subjects.setdefault(subject, sum_hours)
#         print(dict_subjects)
# except Exception as e:
#     print(f'Ошибка: {e}')

"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
# import sys
# import json
# from functools import reduce
#
# try:
#     with open('PZ5_ex7.txt', 'r', encoding='utf-8') as file_obj_7:
#         list_profit = []
#         firm_dict = {}
#         for line in file_obj_7.readlines():
#             line = line.rstrip('\n')
#             firm, type_ownership, proceeds, costs = line.split()
#             profit = int(proceeds) - int(costs)
#             firm_dict.setdefault(firm, profit)
#             if profit >= 0:
#                 list_profit.append(profit)
#         avr_profit = reduce(lambda x, y: x + y, list_profit) / len(list_profit)
#         result_list = [firm_dict, {'average_profit': avr_profit}]
#         print(result_list)
#
#     with open('PZ5_ex7.json', 'w') as firm_json:
#         json.dump(json.dumps(result_list), firm_json)
# except Exception as e:
#     print(f'Ошибка: {e}')