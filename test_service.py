import unittest
from server import accept_client_message

class Testserver(unittest.TestCase):
    def testaccept_client_message(self):
        self.assertEqual(accept_client_message({
       "action": "presence",
       "time": 1682704782.6792958,
       "user": {
               "Имя":
               "C0deMaver1ck",
               "password":
               "CorrectHorseBatteryStaple"
               }
       }))

if __name__ == '__main__':
    unittest.main()
