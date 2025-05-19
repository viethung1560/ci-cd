import unittest
from app import addition

class TestAddition(unittest.TestCase):

    def test_positives(self):
        self.assertEqual(addition(2, 3), 5)

    def test_negatives(self):
        self.assertEqual(addition(-2, -3), -5)

    def test_zero(self):
        self.assertEqual(addition(0, 0), 0)

    def test_mixed(self):
        self.assertEqual(addition(-2, 3), 1)

if __name__ == '__main__':
    unittest.main()
