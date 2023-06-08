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

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('список контактов')
        self.resize(300,100)
        layout = QVBoxLayout()

        layout.addWidget()
        self.setLayout(layout)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
