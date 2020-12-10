import unittest
from main import multiply_by_2

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(multiply_by_2(5), 10)

    def test_something2(self):
        self.assertEqual(multiply_by_2(4), 7)

if __name__ == '__main__':
    unittest.main()
