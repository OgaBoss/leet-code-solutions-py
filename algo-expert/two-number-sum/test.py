import unittest
from index import two_number_sum


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [3, 5, -4, 8, 11, 1, -1, 6]
        self.assertEqual(two_number_sum(arr, 10), [-1, 11])  # add assertion here


if __name__ == '__main__':
    unittest.main()
