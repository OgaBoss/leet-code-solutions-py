import unittest
from index import is_valid_subsequence


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [3, 5, -4, 8, 11, 1, -1, 6]
        self.assertEqual(is_valid_subsequence(arr, [5, 11, 1, -1]), True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
