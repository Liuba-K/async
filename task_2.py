"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только
последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
"""
import ipaddress


def host_range_ping(ip_addr, start, end):

    for ip in ip_addr:
        for ip in range(int(input())):  # ввести вручную
    #    ip_addr.append(input("Введите ip для проверки"))



    pass
if __name__=='__main__':
    ip_addr = input('введите проверяемый адрес')

    ip_2 = '10.0.0.0'
    ip_3 = ['10.0.1.0/24', '10.0.1.1/24', '3232235776', '192.168.1.0']

    #print(host_range_ping(ip_3))
    print(host_range_ping(ip_2) #None