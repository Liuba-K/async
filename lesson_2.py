
import csv
import re
import pandas as pd

"""
def get_data():
    with open('info_1.txt', 'r',encoding="utf-8") as f:
        for line in f:
            print(line)
"""
d='info_1.txt'
with open(d, 'r') as f:
    #f_logs = ((line.split(":")[0], line.split(":")[1]) for line in f)
    #f_res = ((line.split(":")[1]) for line in f)
    #f_read = csv.reader(f, delimiter=":")
    #f_read = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=':')
    #f_read = csv.DictReader(f)

    for line in f:
        RE_FIND = re.findall(r'Изготовитель системы', line, re.I)
        FIND = re.compile(r'\bИзготовитель системы:\s*(\S*)')
        RE_FIND2 = FIND.findall(line)
        print(RE_FIND, RE_FIND2)
        #print(next(f))

    #Изготовитель системы
    #Название ОС
    #Код     продукта
    #Тип     системы
    #for line in f_read:
     #       print(line)
"""
    for line in f_logs:
        if line[0] == 'Изготовитель системы':
            print(line)
"""

