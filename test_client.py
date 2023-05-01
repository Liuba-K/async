import unittest
from client import create_presence_messages

class Testclient(unittest.TestCase):
    def testcreate_presence_messages(self):
        self.assertEqual(create_presence_messages())

if __name__ == '__main__':
    unittest.main()
