from socket import *
import json
import sys
import threading
import time
#import dis
#from metaclasses import ClientMaker

MAX_MSG_LEN = 640
MAX_SYMBOL_LEN_IN_BYTES = 4  # in utf-8 symbol could have len 1-4 in bytes


def create_presence_messages():
    #сформировать presence-сообщение
    messenger = {
       "action": "presence",
       "time": 1682704782.6792958,
       "user": {
               "Имя":
               "C0deMaver1ck",
               "password":
               "CorrectHorseBatteryStaple"
               }
       }
    return messenger


def send_message(s, msg):
    #отправить сообщение серверу
    msg_json = json.dumps(msg)
    msg_encode = msg_json.encode('utf-8')
    s.send(msg_encode)


def answer_server(s):
    #получить ответ сервера
    encoded_response = s.recv(MAX_MSG_LEN * MAX_SYMBOL_LEN_IN_BYTES) #проверка на длину 640символов

    json_response = encoded_response.decode('utf-8')
    if len(json_response) > MAX_MSG_LEN:
        raise ValueError(f"Message cannot be longer then {MAX_MSG_LEN} symbols")

    response = json.loads(json_response)

    if isinstance(response, dict):
        return response
    raise ValueError("")


def process_message_server(message):
    #разобрать сообщение сервера;
    if message['response'] == 200:
        return '200: ОК'
    else:
        return message['error'], message['response']

    #могут быть и другие трехзначные response
def message_from_server(s):# username
    """Функция - обработчик сообщений других пользователей, поступающих с сервера"""
    while True:
        try:
            message = answer_server(s)
            if message['action'] == 'message' and \
                    "sender" in message and "destination" in message \
                    and "text" in message:
                print(f'\nПолучено сообщение от пользователя {message["sender" ]}:'
                      f'\n{message["text"]}')
            else:
                print(f'Получено некорректное сообщение с сервера: {message}')
        except(ConnectionRefusedError, ConnectionError):#проверить
            print(f'Не удалось декодировать полученное сообщение.')

def create_message(sock, account_name='Guest'):
    """
    Функция запрашивает кому отправить сообщение и само сообщение,
    и отправляет полученные данные на сервер
    :param sock:
    :param account_name:
    :return:
    """
    to_user = input('Введите получателя сообщения: ')
    message = input('Введите сообщение для отправки: ')
    message_dict = {
        "action": 'message',##
        "sender": account_name,
        "destination": to_user,
        "time": time.time(),
        "text": message
    }

    try:
        send_message(sock, message_dict)
    except(ConnectionRefusedError, ConnectionError):#проверить
        sys.exit(1)

def user_interactive(sock): #username
    """Функция взаимодействия с пользователем, запрашивает команды, отправляет сообщения"""

    while True:
        command = input('Введите команду: ')
        if command == 'message':
            create_message(sock)#, username
        else:
            print('Команда не распознана, попробойте снова.')

def main():
    #параметры командной строки скрипта client.py <addr> [<port>] (порт по :
    if len(sys.argv) == 3:
        addr = sys.argv[1]
        port = int(sys.argv[2])
    elif len(sys.argv) == 2:
        addr = sys.argv[1]
        port = 7777
    else:
        addr = '127.0.0.1'
        port = 7777
    print(f'{addr=} {port=}')
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, port)) ##127.0.0.1 7777
    msg = create_presence_messages()
    send_message(s, msg)

    #answer = process_message_server(answer_server(s))

    try:
        answer = process_message_server(answer_server(s))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')
    # запускаем клиенский процесс приёма сообщний
    receiver = threading.Thread(target=message_from_server, args=(s, )) #'username'
    receiver.daemon = True
    receiver.start()
    # затем запускаем отправку сообщений и взаимодействие с пользователем.
    user_interface = threading.Thread(target=user_interactive, args=(s, ))#'username'
    user_interface.daemon = True
    user_interface.start()

    while True:
        time.sleep(1)
        if receiver.is_alive() and user_interface.is_alive():
            continue
        break


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
