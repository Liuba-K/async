from socket import *
import time

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 10000))
    s.listen(5)#подключается 5 клиентов

    while True:
        client, addr = s.accept()
        print('Получаем запрос на соединение:', addr)
        timestr = time.ctime(time.time()) + '\n'
        client.send(timestr.encode('utf-8')) #обязательна кодировка
        client.close()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e) #traceback
