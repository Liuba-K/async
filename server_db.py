from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import mapper, sessionmaker
import datetime


#SERVER_DATABASE = sqlite:///server_base.db3
SERVER_DATABASE = "sqlite:///D:/IT/projects/async/server_db.db3"
"""
 Начать реализацию класса «Хранилище» для серверной стороны.
 Хранение необходимо осуществлять в базе данных. В качестве СУБД использовать sqlite. 
 Для взаимодействия с БД можно применять ORM.
"""


class ServerDb:
    class Users:
        def __init__(self, name, ip, port):
            self.login = name
            self.ip = ip
            self.port = port
            self.login_time = datetime.datetime.now()
            self.id = None # обязателен?

    class ClientHistory:
        def __init__(self, name, date, ip, port):
            self.id = None
            self.name = name
            self.date_time = date
            self.ip = ip
            self.port = port

    class ContactList:
        def __init__(self, id_client, id_name):
            self.id = None
            self.id_client = id_client
            self.id_name = id_name
    def __init__(self):
        self.database_engine = create_engine(SERVER_DATABASE, echo=False, pool_recycle=7200)
        self.metadata = MetaData()
        users_table = Table('Users', self.metadata,
                            Column('id', Integer, primary_key=True),
                            Column('user', ForeignKey('Users.id'), unique=True),
                            Column('ip', String),
                            Column('port', Integer),
                            Column('login_time', DateTime)
                            )
        client_history = Table('Client_history', self.metadata,
                               Column('id', Integer, primary_key=True),
                               Column('name', ForeignKey('Users.id')),
                               Column('date_time', DateTime),
                               Column('ip', String),
                               Column('port', String)
                               )
        contact_list = Table('Contacts_list', self.metadata,
                             Column('id', Integer, primary_key=True),
                             Column('id_client', Integer),
                             Column('id_name', Integer)
                             )
        # Создаём таблицы
        self.metadata.create_all(self.database_engine)

        # Создаём отображения
        # Связываем класс в ORM с таблицей
        mapper(self.Users, users_table)
        mapper(self.ClientHistory, client_history)
        mapper(self.ContactList, contact_list)

        # Создаём сессию
        Session = sessionmaker(bind=self.database_engine)
        self.session = Session()
        self.session.commit() #&&

        # Функция выполняющяяся при входе пользователя, записывает в базу факт входа
    def user_login(self, username, ip_address, port):
        print(username, ip_address, port)
            # Запрос в таблицу пользователей на наличие там пользователя с таким именем
        rez = self.session.query(self.Users).filter_by(name=username)
        user = self.Users(username) #
        self.session.add(user)
        self.session.commit()## Комит здесь нужен, чтобы присвоился ID
        new_active_user = self.Users(user.id, ip_address, port, datetime.datetime.now()) #login_time
        self.session.add(new_active_user)
        # Создаем экземпляр класса self.LoginHistory, через который передаем данные в таблицу
        history = self.ClientHistory(user.id, datetime.datetime.now(), ip_address, port)
        self.session.add(history)

        # Сохраняем изменения
        self.session.commit()

    def user_logout(self, username):
        # Запрашиваем пользователя, что покидает нас
        # получаем запись из таблицы Users
        user = self.session.query(self.Users).filter_by(name=username).first()
        print(user)

        # Функция возвращающая историю входов по пользователю или всем пользователям
    def login_history(self, username=None):
            # Запрашиваем историю входа
        query = self.session.query(self.Users.login,
                                       self.ClientHistory.date_time,
                                       self.ClientHistory.ip,
                                       self.ClientHistory.port
                                       ).join(self.Users)
            # Если было указано имя пользователя, то фильтруем по нему
        if username:
            query = query.filter(self.Users.login == username)
        return query.all()

    # Отладка
if __name__ == '__main__':
    test_db = ServerDb()
        # выполняем 'подключение' пользователя
    test_db.user_login('client_1', '192.168.1.4', 8888)
    test_db.user_login('client_2', '192.168.1.5', 7777)
        # выводим список кортежей - активных пользователей
    print(test_db.active_users_list())
        # выполянем 'отключение' пользователя
    test_db.user_logout('client_1')
        # выводим список активных пользователей
    print(test_db.active_users_list())
        # запрашиваем историю входов по пользователю
    test_db.login_history('client_1')
        # выводим список известных пользователей
    print(test_db.users_list())



