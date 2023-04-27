from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 10000))
s.listen(5)#подключается 5 клиентов

while True:
    client, addr = s.accept()
    print('Получаем запрос на соединение:', addr)
    timestr = time.time(time.time()) + '\n'
    client.send(timestr.encode('utf-8')) #ajhvbhetncz cjj,otybt
    client.close()
