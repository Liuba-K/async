from socket import *
import json
import sys


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
    print(f'response from server: {json_response}')
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

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, port)) ##127.0.0.1 7777

    msg = create_presence_messages()

    send_message(s, msg)

    answer = process_message_server(answer_server(s))

    s.close()



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
