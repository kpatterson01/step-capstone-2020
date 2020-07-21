import unittest
from resource_provisioning import calculate_metrics

# Test that precision implementation works as expected
class TestPrecisionLogic(unittest.TestCast):

    def test_simple_case(self):
        actual = {1,2,3,4}
        predicted = {2,5}
        expected_precision = 0.5
        calculated_precision , _ = calculate_metrics(actual, predicted)
        self.assertEquals(expected_precision,calculated_precision)

    def test_empty_case(self):
        actual = {1,2,3,4}
        predicted = {}
        self.assertRaises(ZeroDivisionError,calculate_metrics(actual, predicted))

    def test_zero_case(self):
        actual = {1,2,3,4}
        predicted = {5,6}
        expected_precision = 0.0
        calculated_precision , _ = calculate_metrics(actual, predicted)
        self.assertEquals(expected_precision,calculated_precision)


# Test that recall implementation works as expected
class TestRecallLogic(unittest.TestCast):

    def test_simple_case(self):
        actual = {1,2,3,4}
        predicted = {2,5}
        expected_recall = 0.25
        _ , calculated_recall = calculate_metrics(actual, predicted)
        self.assertEquals(expected_recall, calculated_recall)

    def test_empty_case(self):
        actual = {}
        predicted = {}
        self.assertRaises(ZeroDivisionError,calculate_metrics(actual, predicted))

    def test_zero_case(self):
        actual = {1,2,3,4}
        predicted = {5,6}
        expected_recall = 0.0
        _ , calculated_recall = calculate_metrics(actual, predicted)
        self.assertEquals(expected_recall,calculated_recall)
