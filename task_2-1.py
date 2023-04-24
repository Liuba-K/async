"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
"""
import csv
import os, glob
import re


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    for filename in glob.glob('info_*.txt'):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            data = f.read() #!!!Заново прочитывает?
            #вставка переменных в регулярные выражения
            FIND = re.compile(r'\bИзготовитель системы:\s*(\S*)')
            NAME = re.compile(r'\bНазвание ОС:\s*(.*)')
            CODE = re.compile(r'\bКод продукта:\s*(.*)')
            TYPE = re.compile(r'\bТип системы:\s*(.*)')
            #\bНазвание ОС:\s*(.*)|\bКод продукта:\s * (.*) |\bИзготовитель системы:\s * (.*) |\bТип системы:\s * (.*)
            #если последовательность одинаковая в файлах?
            #append обычно долго выполняется

            #Добавим только первые значения по поиску регуляного выражения из каждого файла
            #list вместо str
            p = FIND.findall(data)[0]#.split()[0]
            #p = FIND.findall(data)[0] #IndexError: list index out of range
            n = NAME.findall(data)[0]
            c = CODE.findall(data)[0]
            t = TYPE.findall(data)[0]
            #print(type(p))

            #Формируем четыре списка
            os_prod_list.append(p)
            os_name_list.append(n)
            os_code_list.append(c)
            os_type_list.append(t)

            #Формировние главного списка для хранения данных отчета
            row_data = [p, n, c, t]
            main_data.append(row_data)
    #print(main_data)
    return main_data





def write_to_csv(outfile):


    with open(outfile, 'w+', encoding='utf-8') as f:
        F_N_WRITER = csv.writer(f)
        for row in get_data():
            F_N_WRITER.writerow(row)

write_to_csv('data_report.csv')





