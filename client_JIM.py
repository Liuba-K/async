from socket import *
import json


def create_presence_messages():
    pass


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 7777))
    msg = '''{
    "action": "presence",
    "time":1682704782.6792958,
    "user": {
    "Имя":
    "C0deMaver1ck",
    "password":
    "CorrectHorseBatteryStaple"
    }
    }'''

    # msg = 'Привет, сервер'.encode('utf-8')
    msg_json = json.dumps(msg)
    msg_encode = msg_json.encode('utf-8')
    s.send(msg_encode)
    # s.send(msg_json)
    tm = s.recv(1024)

    s.close()
    print("Сервер: ", tm.decode('utf-8'))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
