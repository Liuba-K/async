#import socket
from socket import *
import time
import json
import sys
import argparse
import select #new
import dis
MAX_MSG_LEN = 640
MAX_SYMBOL_LEN_IN_BYTES = 4
MAX_CONNECTIONS = 5 #подключается 5 клиентов


class ServerVerifier:
    pass
def accept_client_message(message,client, names):
    #принимает сообщение клиента
    if message['action'] == 'presence' and 'time' in message and 'user' in message:
        if message['user']['account_name'] not in names.keys():
            names[message['user']['account_name']] = client
            send_message(client, {'response': 200})
        else:
            response = {'response': 400, 'error': 'Bad Request'}
            send_message(client, response)
            client.close()
        #return {'response': 200}
        return
    return {'response': 400, 'error': 'Bad Request'} #необязательное поле
def process_message(message, names, s):
    #отправляет сообщение клиенту
    if message['destination'] in names and names[message['destination']] in s:
        send_message(names[message['destination']], message)
    elif message['destination'] in names and names[message['destination']] not in s:
        raise ConnectionError
    else:
        print(f'Отправка невозможна, пользователь не зарегистрирован')

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

def server_parser():
    parser = argparse.ArgumentParser("port and address")
    parser.add_argument('-p', nargs='?', default='7777', type=int)
    parser.add_argument('-a', nargs='?', help='Input addr ', required=True, default='127.0.0.1')
    namespace = parser.parse_args(sys.argv[1:])
    return namespace

def main():
    s = socket(AF_INET, SOCK_STREAM)

    namespace = server_parser()
    s.bind((namespace.a, namespace.p)) #listen_address, listen_port
    s.settimeout(0.5)
    clients = []
    messages = []
    names = dict()

    s.listen(MAX_CONNECTIONS)

    while True:
        try:
            client, addr = s.accept()
            print('Получаем запрос на соединение:', addr)
        except OSError:
            pass
        recv_data_lst = []
        send_data_lst = []
        err_lst = []
        # Проверяем на наличие ждущих клиентов
        try:
            if clients:
                recv_data_lst, send_data_lst, err_lst = select.select(clients, clients, [], 0)
        except OSError:
            pass

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



