import unittest
from client import create_presence_messages, send_message, answer_server, process_message_server

class Testclient(unittest.TestCase):
    def testcreate_presence_messages(self):
        self.assertEqual(create_presence_messages(), {
       "action": "presence",
       "time": 1682704782.6792958,
       "user": {
               "Имя":
               "C0deMaver1ck",
               "password":
               "CorrectHorseBatteryStaple"
               }
       })
    """ 
    def testsend_message(self):
        self.assertEqual(send_message(),)
#как сделать отправку сообщения??
"""
    def test_200process_message_server(self):
        self.assertEqual(process_message_server({'response': 200}), '200: ОК')

if __name__ == '__main__':
    unittest.main()
