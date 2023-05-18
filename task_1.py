"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
 """
import ipaddress


def host_ping(ip_addr):
        if isinstance(ip_addr, list):
            for i in ip_addr:
                try:
                    ipaddress.ip_network(i)
                    print('Узел доступен: ', i)
                except ValueError:
                    print('Узел недоступен: ', i)
        else:
            print('Доступность сетевых узлов нельзя проверить, так как ожидается список')

def create_ping():
    ip_host = ipaddress.ip_network('80.0.1.0/28')
    #ip1 = ipaddress.ip_address('192.168.1.0')
    #l=[]
    #l=l.append(ip1)
    ip_addr = list(ip_host.hosts())
    #ip_addr = l.extend(l)
    return ip_addr

if __name__=='__main__':
    #ip_1 = '10.0.1.1/24'
    ip_2 = create_ping()
    ip_3 = ['10.0.1.0/24', '10.0.1.1/24']
    #print(host_ping(ip_1))
    print(host_ping(ip_2))
    print(host_ping(ip_3))


