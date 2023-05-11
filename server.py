from socket import socket, AF_INET, SOCK_STREAM
import time
import select


def listen_socket(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', 10000))
    sock.listen(5)
    sock.settimeout(0.2)

    return sock


def mainloop():
    address = (('', 10000))
    clients = []
    sock = listen_socket(address)

    while True:
        try:
            client, addr = sock.accept()
        except OSError as e:
            pass
        else:
            print('Получаем запрос на соединение:', addr)
            clients.append(client)
        finally:
            recv_lst = []
            send_lst = []
            #err_lst = []

            #w = []
            try:
                if clients:
                    recv_lst, send_lst, err_lst = select.select([], clients, [], 0)
            except Exception as e:
                pass
            if recv_lst:
                for s_client in recv_lst:
                    timestr = time.ctime(time.time()) + '\n'
                    try:
                        s_client.send(timestr.encode('utf-8'))
                    except:
                        clients.remove(s_client)

                for s_client in send_lst:
                    timestr = time.ctime(time.time()) + '\n'
                    try:
                        s_client.send(timestr.encode('utf-8'))
                    except:
                        clients.remove(s_client)


print("запущен")
mainloop()
""" 
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e) #traceback
"""
