from socket import *
import time
import json
from client_JIM import answer_server

def accept_client_message(message):
    #принимает сообщение клиента
    if message['action'] == 'presence' and 'time' in message:
        return {'response': 200}
    return {
        'response': 400,
        'error': 'Bad Request' #необязательное поле
    }


def main():
    listen_port = 7777
    listen_address = ''

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((listen_address, listen_port))
    s.listen(5)#подключается 5 клиентов

    while True:
        client, addr = s.accept()
        #print(answer_server(client))
        print('Получаем запрос на соединение:', client)
        #data = client.recv(1024)

        #json.loads(data.decode('utf-8'))
        #print('Было получено сообщение: ', json.loads(data.decode('utf-8')))
        message_from_cient = answer_server(client)
        print(message_from_cient)
        msg = 'Ваше сообщение получено'     #то, что видит клиент
        client.send(msg.encode('utf-8')) #отправляем в байтах и только первое..

        #timestr = time.ctime() + '\n'
        #client.send(timestr.encode('utf-8')) #обязательна кодировка
        client.close()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e) #traceback
