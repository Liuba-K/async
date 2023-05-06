from socket import *
import time
import json
#obj =  json.loads(s=)


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 10000))
    s.listen(5)#подключается 5 клиентов

    while True:
        client, addr = s.accept()
        print('Получаем запрос на соединение:', addr)
        timestr = time.ctime() + '\n'
        client.send(timestr.encode('utf-8')) #обязательна кодировка
        client.close()
'''{
"action": "authenticate",
"time":1682704782.6792958,
"user": {
"account_name":
"C0deMaver1ck",
"password":
"CorrectHorseBatteryStaple"
}
}'''

def do_action(action):
    if action == "authenticate":
        pass
        # do authenticate
    return result


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e) #traceback
