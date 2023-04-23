"""
# задание 5

5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
"""
import subprocess


def ping(i):
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for i in subproc_ping.stdout:
        #l = i.decode('ascii')
        #print(i)
        line = i.decode('cp866') #кириллицa
        print(line)

if __name__ == "__main__":
    #args = ['ping', 'yandex.ru']
    #ping(args)
    webs = ['yandex.ru', 'youtube.com']
    for web in webs:
        args = ['ping', web]
        ping(args)

