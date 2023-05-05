#import socket
from socket import *
import time
import json
import sys
import argparse

MAX_MSG_LEN = 640
MAX_SYMBOL_LEN_IN_BYTES = 4
def accept_client_message(message):
    #принимает сообщение клиента
    if message['action'] == 'presence' and 'time' in message:
        return {'response': 200}
    return {'response': 400, 'error': 'Bad Request'} #необязательное поле

def read_message(s: socket):
    #получить ответ сервера
    encoded_response = s.recv(MAX_MSG_LEN * MAX_SYMBOL_LEN_IN_BYTES) #проверка на длину 640символов
    json_response = encoded_response.decode('utf-8')
    #print(f'response from server: {json_response}')
    if len(json_response) > MAX_MSG_LEN:
        raise ValueError(f"Message cannot be longer then {MAX_MSG_LEN} symbols")

    response = json.loads(json_response)

    if isinstance(response, dict):
        return response
    raise ValueError("")

def send_message(client, msg):
    #отправка ответа клиенту;
    js_message = json.dumps(msg)
    encoded_message = js_message.encode('utf-8')
    client.send(encoded_message)


def main():
    s = socket(AF_INET, SOCK_STREAM)
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser("port and address")
        parser.add_argument('-p', nargs='?', default='7777', type=int)
        parser.add_argument('-a', nargs='?', help='Input addr ', required=True)
        namespace = parser.parse_args(sys.argv[1:])

        s.bind((namespace.a, namespace.p)) #listen_address, listen_port
    else:
        s.bind(('', 7777))#127.0.0.1
    s.listen(5)#подключается 5 клиентов

    while True:
        client, addr = s.accept()
        print('Получаем запрос на соединение:', addr)
        try:

            message_from_client = read_message(client)
            print('Сообщение от клиента:', message_from_client)

            msg = accept_client_message(message_from_client)    #то, что видит клиент
            #client.send(json.dumps(msg).encode('utf-8')) #отправляем в байтах и только первое..
            send_message(client, msg)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)



