from socket import *

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 10000))
    while True:
        tm = s.recv(1024)
        print("текущее время: ", tm.decode('utf-8'))

    s.close()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)





