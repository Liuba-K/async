"""
#задание 1
1. Каждое из слов «разработка», «сокет», «декоратор» представить в
строковом формате и проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера
преобразовать строковые представление в
формат Unicode и также проверить тип и содержимое переменных.
"""


def converter(i):
    d = i.encode('UTF-8')
    return d


def writer(i):
    print('тип переменной: {},\n содержание переменной - {}'.format(type(i), i))
    print('{}\n после онлайн конвертера \n тип переменной: {}\n содержание переменной - {}'
          .format('...'*20,type(converter(i)), converter(i)))


def type_description(i):
    if isinstance(i, list):
        for _ in i:
            writer(_)
            print('*'*20)
    elif isinstance(i, str):
        writer(i)
    elif isinstance(i, int):
        i = str(i)
        writer(i)
    else:
        print('Введеные данные не являются листом, строкой или числом')



if __name__ == "__main__":
    #val = str("разработка")
    val = ['разработка', 'сокет', 'декоратор']
    #val = 1

    type_description(val)


