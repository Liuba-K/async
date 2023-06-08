"""
1. Реализовать графический интерфейс пользователя на стороне клиента:
Отображение списка контактов;
Выбор чата двойным кликом на элементе списка контактов;
Добавление нового контакта в локальный список контактов;
Отображение сообщений в окне чата;
Набор сообщения в окне ввода сообщения;
Отправка введенного сообщения.
"""

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QTableView, QDialog, QFileDialog , QMessageBox, QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
import os
# GUI - Функция реализующая заполнение таблицы историей сообщений.
def create_stat_model(database):
    # Список записей из базы
    hist_list = database.message_history()

    # Объект модели данных:
    listcontact = QStandardItemModel()
    listcontact.setHorizontalHeaderLabels(
        ['Имя Клиента', 'Последний раз входил', 'Сообщений отправлено', 'Сообщений получено'])
    for row in hist_list:
        user, last_seen, sent, recvd = row
        user = QStandardItem(user)
        user.setEditable(False)
        last_seen = QStandardItem(str(last_seen.replace(microsecond=0)))
        last_seen.setEditable(False)
        sent = QStandardItem(str(sent))
        sent.setEditable(False)
        recvd = QStandardItem(str(recvd))
        recvd.setEditable(False)
        list.appendRow([user, last_seen, sent, recvd])
    return list
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI() #вынести отдельна параметры

    def initGui(self):
        self.setWindowTitle('список контактов')
        self.setFixedSize(800, 600)
        #self.resize(300,100)
        layout = QVBoxLayout()

        #кнопки
        self.refresh_button = QAction('Обновить список', self)
        self.config_button = QAction('Настройки сервера', self)
        self.show_history_button = QAction('История клиентов', self)

        self.statusBar()
        self.toolbar = self.addToolBar('MainBar')
        self.toolbar.addAction(QAction('Выход', self)) #требуются дополнительные параметры
        self.toolbar.addAction(self.refresh_button)
        self.toolbar.addAction(self.show_history_button)
        self.toolbar.addAction(self.config_btn)

        # Надпись о том, что ниже список подключённых клиентов
        self.label = QLabel('Список подключённых клиентов:', self)
        self.label.setFixedSize(240, 15)
        self.label.move(10, 25)

        # Окно со списком подключённых клиентов.
        self.active_clients_table = QTableView(self)
        self.active_clients_table.move(10, 45)
        self.active_clients_table.setFixedSize(780, 400)
        self.show()
        #layout.addWidget()
        #self.setLayout(layout)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()

    #window.statusBar().showMessage('Test Statusbar Message')

    #window.show()
    sys.exit(app.exec())
    #app.exec_()
