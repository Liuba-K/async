"""
# задание 4
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое
 и выполнить обратное преобразование (используя методы encode и decode).

"""
def converter(i):
    d = i.encode('UTF-8')
    return d

def converter_back(i):
    d = i.decode('UTF-8')
    return d

if __name__ == "__main__":
    #val = str("разработка")
    val4 = ['разработка', 'администрирование', 'protocol', 'standard']
    #val = 1
    for i in val4:
        print(converter(i))

        new = converter(i)
        print(converter_back(new))
        print("***"*20)

