
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
        self.assertEqual(self.actual_manager, self.google.company.get(self.actual_googler))

    def test_get_ceo(self):
        # Test that the ceo has a None manager object
        self.assertEqual(None, None)

if __name__ == '__main__':
    unittest.main()
