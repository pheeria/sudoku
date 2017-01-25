import unittest
from checkers import *


class TestCheckers(unittest.TestCase):

    def test_line_check_horizontal(self):
        target = {'10': [1, 3], '11': [1, 3, 5], '14': [1, 3]}
        possibilities_linear_check(target, 1, True)
        print(target)
        self.assertDictEqual({'10': [1, 3], '11': [5], '14': [1, 3]}, target)

    def test_line_check_vertical(self):
        target = {'10': [1, 3], '20': [1, 3, 5], '70': [1, 3]}
        possibilities_linear_check(target, 0, False)
        print(target)
        self.assertDictEqual({'10': [1, 3], '20': [5], '70': [1, 3]}, target)