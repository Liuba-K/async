from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import mapper, sessionmaker
import datetime

"""
Реализовать хранение информации в БД на стороне клиента:
* списокконтактов;
* историясообщений.
Реализовать графический интерфейс для мессенджера, используя библиотеку PyQt. Реализовать графический интерфейс администратора сервера:
* отображение списка всех клиентов;
* отображение статистики клиентов;
* настройка сервера (подключение к БД, идентификация).
"""

CLIENT_DATABASE = "sqlite:///D:/IT/projects/async/client_db.db3"
class ClientDb:
    class Contacts:
        def __init__(self, contact):
            self.id = None
            self.name = contact

    class MessageHistory:
        def __init__(self, from_user, to_user, message):
            self.id = None
            self.from_user = from_user
            self.to_user = to_user
            self.message = message
            self.date = datetime.datetime.now()

        # Конструктор класса:
    def __init__(self):
        #Создаём движок базы данных, объект MetaData, таблицы
        """
        возможно стоит по сложнее  # Создаём движок базы данных, поскольку разрешено несколько клиентов одновременно, каждый должен иметь свою БД
        # Поскольку клиент мультипоточный необходимо отключить проверки на подключения с разных потоков,
        # иначе sqlite3.ProgrammingError
        self.database_engine = create_engine(f'sqlite:///client_{name}.db3', echo=False, pool_recycle=7200,
                                             connect_args={'check_same_thread': False})
        """
        self.database_engine = create_engine(CLIENT_DATABASE, echo=False, pool_recycle=7200) #connect_args=
        self.metadata = MetaData()
        contacts = Table('contacts', self.metadata,
                         Column('id', Integer, primary_key=True),
                         Column('name', String, unique=True)
                         )
        history = Table('message_history', self.metadata,
                        Column('id', Integer, primary_key=True),
                        Column('from_user', String),
                        Column('to_user', String),
                        Column('message', String), #Text error
                        Column('date', DateTime)
                        )
        self.metadata.create_all(self.database_engine)
        # Создаём отображения, сессию
        mapper(self.MessageHistory, history)
        mapper(self.Contacts, contacts)
        Session = sessionmaker(bind=self.database_engine)
        self.session = Session()

        # Необходимо очистить таблицу контактов, т.к. при запуске они подгружаются с сервера.
        self.session.query(self.Contacts).delete()
        self.session.commit()

        # Функция добавления контактов
    def add_contact(self, contact):
        if not self.session.query(self.Contacts).filter_by(name=contact).count():
            contact_row = self.Contacts(contact)
            self.session.add(contact_row)
            self.session.commit()

        # Функция удаления контакта
    def del_contact(self, contact):
        self.session.query(self.Contacts).filter_by(name=contact).delete()
    # Функция добавления известных пользователей.
    # Функция сохраняющяя сообщения
    # Функция проверяющяя наличие пользователя контактах

        # Функция возвращающяя контакты ??? отображение списка всех клиентов;
    def get_contacts(self):
        return [contact[0] for contact in self.session.query(self.Contacts.name).all()]
    #
        # Функция возвращающая историю переписки
    def get_history(self, from_who=None, to_who=None):
        query = self.session.query(self.MessageHistory)
        if from_who:
            query = query.filter_by(from_user=from_who)
        if to_who:
            query = query.filter_by(to_user=to_who)
        return [(history_row.from_user, history_row.to_user, history_row.message, history_row.date) for history_row in query.all()]
if __name__ == '__main__':
    test_db = ClientDb('test1')
    for i in ['test3', 'test4', 'test5']:
        test_db.add_contact(i)
    test_db.add_contact('test4')
    print(test_db.get_contacts())
    print(test_db.get_history('test2'))
    print(test_db.get_history(to_who='test2'))
    print(test_db.get_history('test3'))
    test_db.del_contact('test4')
    print(test_db.get_contacts())
