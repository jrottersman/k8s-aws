import unittest
from index import create_message

class TestCreateMessage(unittest.TestCase):

    def test_message(self):
        test = create_message(0)
        self.assertEqual(test["message"], "Automate all the Things")
        self.assertEqual(test["time"], 0)

if __name__ == '__main__':
    unittest.main()
