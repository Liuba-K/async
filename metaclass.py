import dis

"""
отсутствие вызовов accept и listen для сокетов;
использование сокетов для работы по TCP;
отсутствие создания сокетов на уровне классов, то есть отсутствие конструкций такого вида: 
class Client: s = socket() ..."""
class ClientVerifier(type):
    def __init__(self):
        try:
