from socket import *
from select import select

ADDRESS = ('localhost', 10000)


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((ADDRESS))
    while True:
        msg = input('Ваше сообщение: ')
        if msg == 'exit':
            break
        s.send(msg.encode('utf-8'))
        data = s.recv(1024)
        print("Ответ: ", data.decode('utf-8'))

    s.close()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)





