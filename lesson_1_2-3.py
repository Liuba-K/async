"""
# задание 2
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
 (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

"""


def bytes_type(i):
    ib = bytes(i, 'UTF-8')
    return ib


def writer2(i):
    print('тип переменной: {}\n содержимое переменной - {}\n длина переменной - {}'
          .format(type(bytes_type(i)), bytes_type(i), len(bytes_type(i))))



"""
# задание 3
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

"""
if __name__ == "__main__":
    #task2
    val2 = ['class', 'function', 'method']
    for _ in val2:
        writer2(_)
        print('*' * 20)
    #task 3
    val3 = ['attribute', 'класс', 'функция', 'type']
    for i in val3:
        try:
            #bytes(i, 'UTF-8')
            bytes(i, 'ascii')

        except UnicodeEncodeError:
            print(f'Задание 3 ***\n Слово "{i}" невозможно записать в виде байтовой строки')

#Задание 3 странное, если использовать UTF-8, то все преобразуется....((