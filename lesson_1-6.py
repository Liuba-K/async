"""
задание 6
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
 Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
import locale

description_text = '''сетевое программирование 
сокет
декоратор'''

#создать файл
with open('test_file.txt', 'w+') as file:
    file.write(description_text)

print(file)
#окрыть и вывести
with open('test_file.txt', 'r') as file:
    for i in file:#так как несколько строчек

        print(i.encode('utf-8'))
