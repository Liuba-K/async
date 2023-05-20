"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
 """
import ipaddress
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):


    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def host_ping(ip_addr,  timeout=500):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    if isinstance(ip_addr, list):
        for i in ip_addr:
            try:
                    #command = ['ping', param, '1', i]
                p = subprocess.Popen(f'ping {i} -w {timeout} {param} 1', shell=True, stdout=subprocess.PIPE)
                    #out = p.stdout.read()
                p.wait()
                print(p)
                if p.returncode == 0:
                    #print(p)
                    #if subprocess.call(command) == 0:
                        #ipaddress.ip_network(i)
                    print('Узел доступен: ', i)
                else:
                    print('Узел недоступен: ', i)
            except ValueError:
                    print('Узел недоступен: ', i)
    else:
        print('Доступность сетевых узлов нельзя проверить, так как ожидается список')


def create_ping():
    ip_addr = []
    #for ip in range(int(input())): #ввести вручную
    #    ip_addr.append(input("Введите ip для проверки"))
    ip_host = ipaddress.ip_network('80.0.1.0/28')
    ip1 = ipaddress.ip_address('192.168.1.0')
        #ip_list = list(ip_host.hosts()) #пробежаться по хостам
    ip_addr.append(ip1)
    ip_addr.append(ip_host)
    return ip_addr

if __name__=='__main__':
    ip_1 = ['yandex.ru', '2.2.2.2', '192.168.0.100', '192.168.0.101']
    ip_2 = create_ping()
    ip_3 = ['10.0.1.0/24', '10.0.1.1/24', '3232235776']
    print(host_ping(ip_1))
    #print(host_ping(ip_2))
    print(host_ping(ip_3)) #None
    #ping('yandex.ru')
    print(ping("10.0.1.0"))


