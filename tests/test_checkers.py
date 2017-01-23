import unittest
from checkers import *


class TestCheckers(unittest.TestCase):

    def test_line_check(self):
        target = {'10': [1, 3], '11': [1, 3, 5], '14': [1, 3]}
        possibilities_linear_check(target, 1, True)
        print(target)
        self.assertDictEqual({'10': [1, 3], '11': [5], '14': [1, 3]}, target)
