# Created by Tedi Mitiku 07/08/2020
# Test files for distance_valiation.py

import unittest
from distance_validation import l2_distance
import math,random

class TestEuclideanDistanceFunction(unittest.TestCase):
    def test_zero_distance(self):
        #Make sure that the distance between and user and themselves is 0
        user_one_attributes = [1, 2, 3, 5, 18, 10]
        self.assertEqual(l2_distance(user_one_attributes, user_one_attributes), 0)

    def test_same_output(self):
        #Make sure that the output is the same when switching inputs
        user_one_attributes = [1, 2, 3, 5, 18, 10]
        user_two_attributes = [5, 7, 2, 1, 9, 5]
        self.assertAlmostEqual(l2_distance(user_one_attributes, user_two_attributes), 12.80624847)
        self.assertAlmostEqual(l2_distance(user_two_attributes, user_one_attributes), 12.80624847)

    def test_float(self):
        #Make sure that the output is correct with floating point numbers
        user_one_attributes = [0.1, 0.2, 0.3, 0.5, 1.8, 1]
        user_two_attributes = [0.5, 0.7, 0.2, 0.1, 0.9, 0.5]
        self.assertAlmostEqual(l2_distance(user_one_attributes, user_two_attributes), 1.280624847)
        self.assertAlmostEqual(l2_distance(user_two_attributes, user_one_attributes), 1.280624847)

#insert classes for other distance functions we create and need to test
