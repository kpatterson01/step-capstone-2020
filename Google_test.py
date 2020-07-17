
# Test methods in Google class.

import unittest
from Google import Google
from Googler import Googler

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.googlers = [Googler({  "id": 0, "department": 10, "cost_center":10, "manager_id":-1,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Googler({   "id": 14, "department": 10, "cost_center":10, "manager_id":2,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10})]
        self.google = Google(self.googlers)
        self.actual_googler = Googler({ "id": 14, "department": 10, "cost_center":10, "manager_id":2,
                                        "location": 10, "lowest_dir_id":10, "job_family": 10})

    def test_finds_googler(self):
        #Test that the correct googler is found
        self.assertEqual(self.actual_googler, self.google.search(14))

    def test_raises_error(self):
        #Test that an error is thrown when searching for Googler that doesn't exist
        self.assertRaises(ReferenceError, self.google.search, 1000)


class TestManagerHierarchy(unittest.TestCase):

    def setUp(self):
        self.googlers = [Googler({  "id": 0, "department": 10, "cost_center":10, "manager_id":-1,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Googler({   "id": 14, "department": 10, "cost_center":10, "manager_id":0,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10})]
        self.google = Google(self.googlers)
        self.actual_googler = Googler({ "id": 14, "department": 10, "cost_center":10, "manager_id":0,
                                        "location": 10, "lowest_dir_id":10, "job_family": 10})
        self.actual_manager = Googler({ "id": 0, "department": 10, "cost_center":10, "manager_id":-1,
                                        "location": 10, "lowest_dir_id":10, "job_family": 10})

    def test_get_manager(self):
        # Tests that a googles manager is retrieved
        googler = Googler({ "id": 14, "department": 10, "cost_center":10, "manager_id":0,
                                        "location": 10, "lowest_dir_id":10, "job_family": 10})
        manager = self.google.company.get(googler.manager_id)
        self.assertEqual(self.actual_manager, manager)

    def test_get_ceo(self):
        # Test that the ceo has a None manager object
        self.assertEqual(None, None)

class TestDistance(unittest.TestCase):

    def setUp(self):
        self.googlers = [Googler({  "id": 0, "department": 10, "cost_center":10, "manager_id":-1,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Googler({   "id": 1, "department": 10, "cost_center":10, "manager_id":0,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Googler({   "id": 2, "department": 10, "cost_center":10, "manager_id":0,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Googler({   "id": 8, "department": 10, "cost_center":10, "manager_id":0,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Googler({   "id": 14, "department": 10, "cost_center":10, "manager_id":2,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Googler({   "id": 11, "department": 10, "cost_center":10, "manager_id":2,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Googler({   "id": 9, "department": 10, "cost_center":10, "manager_id":8,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Googler({   "id": 12, "department": 10, "cost_center":10, "manager_id":8,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10})]
        self.google = Google(self.googlers)
        # Google:
        #             0
        #     1       2       8
        #           11 14    9 12
        # distance(9, 12): 1
        # distance(11, 12): 2
        # distance(1, 9): 2
        # distance(1, 0): 1
        # distance(9, 9): 0
    def test_distance(self):
        # Test that Googlers with same manager have distance one
        googler_nine = self.google.search(9)
        googler_twelve = self.google.search(12)
        distance = self.google.distance(googler_nine, googler_twelve)
        self.assertEqual(1, distance)

    def test_same_distance(self):
        # Test that the distance between a Googler and themselves is 0
        googler_nine = self.google.search(9)
        distance = self.google.distance(googler_nine, googler_nine)
        self.assertEqual(0, distance)

    def test_max_distance(self):
        # Test that the distance between two Googlers returns the max length of manager chainå
        googler_nine = self.google.search(9)
        googler_one = self.google.search(1)
        distance = self.google.distance(googler_nine, googler_one)
        self.assertEqual(2, distance)

    def test_level_distance(self):
        # Test distance between Googlers on the same level but with different managers
        googler_eleven = self.google.search(11)
        googler_twelve = self.google.search(12)
        distance = self.google.distance(googler_eleven, googler_twelve)
        self.assertEqual(2, distance)


if __name__ == '__main__':
    unittest.main()
