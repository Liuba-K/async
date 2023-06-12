"""
Создание именованного логгера;
Сообщения лога должны иметь следующий формат: "<дата-время> <уровеньважности> <имямодуля> <сообщение>";
Журналирование должно производиться в лог-файл;
На стороне сервера необходимо настроить ежедневную ротацию лог-файлов.
"""
import logging
#logging.basicConfig(filename='server.log', format='',datefmt)

logger = logging.getLogger('service')

handler = logging.FileHandler('server.log')
formater = logging.Formatter('%(created)f,  %(levelname)s, %(module)s, %(message)s')
handler.setFormatter(formater)
logger.addHandler(handler)

logger.critical('Error in service')


