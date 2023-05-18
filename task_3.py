"""
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
(использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
"""
from tabulate import tabulate
columns = ['programming language', 'type', 'year']
tuples_list = [('Python', 'interpreted', '1991'), ('JAVA', 'compiled', '1995'), ('С', 'compiled', '1972')]
print(tabulate(tuples_list))
print(tabulate(tuples_list, headers=columns, tablefmt="grid", stralign="center"))
