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
        user = self.Users(login)#
        self.session.add(user)
        self.session.commit()## Комит здесь нужен, чтобы присвоился ID


