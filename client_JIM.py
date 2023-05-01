﻿from socket import *
import json
import sys


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
    encoded_response = s.recv(1024)
    print(encoded_response)

    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode('utf-8')
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError
def process_message_server(message):
    #разобрать сообщение сервера;
    if message['response'] == 200:
        return '200: ОК'
    else:
        return message['error'], message['response']

    #могут быть и другие трехзначные response

def main():
    #параметры командной строки скрипта client.py <addr> [<port>]:
    addr = sys.argv[1]
    port = int(sys.argv[2])

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, port)) ##127.0.0.1 7777

    msg = create_presence_messages()

    send_message(s, msg)

    answer = process_message_server(answer_server(s))
    print(answer)

    s.close()



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
