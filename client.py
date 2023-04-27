from socket import *


s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 10000))
tm = s.recv(1024)
s.close()
print("текущее время: ", tm.decode('utf-8'))
