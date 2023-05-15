from socket import *
from subprocess import Popen, CREATE_NEW_CONSOLE

p_list = []

while True:
    user = input("Запустить 5 клиентов (s) / Закрыть клиентов (x) / Выйти (q) ")
    if user == 'q':
        break
    elif user == 's':
        for _ in range(5):
            # Флаг CREATE_NEW_CONSOLE нужен для ОС Windows,
            # чтобы каждый процесс запускался в отдельном окне консоли
            p_list.append(Popen('python time_client_random.py', creationflags=CREATE_NEW_CONSOLE))
        print(' Запущено 5 клиентов')
    elif user == 'x':
        for p in p_list:
            p.kill()
        p_list.clear()
        """ 
def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 10000))
    while True:
        tm = s.recv(1024)
        print("текущее время: ", tm.decode('utf-8'))

    mes = input()
    if mes == 'r':
        client.set_read()
    elif mes == 'w':
        client.set_write()

    s.close()



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
"""
