from socket import *
import time
import json


def accept_client_message(message):
    #принимает сообщение клиента
    if message['action'] == 'presence' and 'time' in message:
        return {'response': 200}
    return {
        'response': 400,
        'error': 'Bad Request' #необязательное поле
    }


def main():

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('localhost', 7777))
    s.listen(5)#подключается 5 клиентов

    while True:
        client, addr = s.accept()
        print('Получаем запрос на соединение:', addr)
        data = client.recv(1024)

        json.loads(data.decode('utf-8'))
        print('Было получено сообщение: ', json.loads(data.decode('utf-8')))
        #print(data) #str в байтах b'
        #print(data.decode('utf-8')) #как есть в клиенте
        print('Было получено сообщение: ', json.loads(data))

        msg = 'Ваше сообщение получено'     #то, что видит клиент
        client.send(msg.encode('utf-8')) #отправляем в байтах и только первое..

        #timestr = time.ctime() + '\n'
        #client.send(timestr.encode('utf-8')) #обязательна кодировка
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

'''
def do_action(action):
    if action == "authenticate":
        pass
        # do authenticate
    return result
'''

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e) #traceback
