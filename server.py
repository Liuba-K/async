from socket import socket, AF_INET, SOCK_STREAM
import time
import select


def listen_socket(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', 10000))
    sock.listen(5)
    sock.settimeout(0.2)

    return sock

def read_requests(r_clients, all_clients):
    """ Чтение запросов из списка клиентов
    """
    responses = {}
    # Словарь ответов сервера вида {сокет: запрос}
    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)
    return responses


def write_responses(requests, w_clients, all_clients):
    """ Эхо-ответ сервера клиентам, от которых были запросы
    """
    for sock in w_clients:
        if sock in requests:
            try:
                # Подготовить и отправить ответ сервера
                resp = requests[sock].encode('utf-8')
                # Эхо-ответ сделаем чуть непохожим на оригинал
                sock.send(resp.upper())
            except:
                # Сокет недоступен, клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)

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
            wait = 10
            recv_lst = []
            send_lst = []
            #err_lst = []

            #w = []
            try:
                if clients:
                    recv_lst, send_lst, err_lst = select.select([], clients, [], wait)
            except Exception as e:
                pass
            requests = read_requests(recv_lst, clients)
            if requests:
                write_responses(requests, send_lst, clients)


print("запущен")
mainloop()
""" 
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e) #traceback
"""
