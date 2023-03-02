"""
Program: average_scores_test.py
Author: Lily Ellison
Last date modified: 03/02/2023

The purpose of this program is to test the average_scores method in the topic 2 assignment.

"""


import unittest

import self as self

from more_fun_with_collections.topic_2_assignment_1 import average_scores


class MyTestCase(unittest.TestCase):
    def test_average(self):
        self.scores_dict = {"Test1": 31, "Test2": 34, "Test3": 54}
        expected = 39.66666666666666
        actual = average_scores(self.scores_dict)
        self.assertAlmostEqual(expected, actual)

    def test_average_five(self):
        self.scores_dict = {"Test1": 31, "Test2": 34, "Test3": 54, "Test4": 67, "Test5": 71}
        expected = 51.4
        actual = average_scores(self.scores_dict)
        self.assertAlmostEqual(expected, actual)

    def test_average_zero(self):
        self.scores_dict = {}
        expected = "Values in dictionary not valid."
        actual = average_scores((self.scores_dict))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
