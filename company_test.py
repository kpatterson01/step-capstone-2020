
# Test methods in Company class.

import unittest
from company import Company
from employee import Employee

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.employees = [Employee({  "id": 0, "department": 10, "cost_center":10, "manager_id":None,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 14, "department": 10, "cost_center":10, "manager_id":2,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10})]
        self.company = Company(self.employees)
        self.actual_employee = Employee({ "id": 14, "department": 10, "cost_center":10, "manager_id":2,
                                        "location": 10, "lowest_dir_id":10, "job_family": 10})

    def test_finds_employee(self):
        #Test that the correct employee is found
        self.assertEqual(self.actual_employee, self.company.search(14))

    def test_raises_error(self):
        #Test that an error is thrown when searching for employee that doesn't exist
        self.assertRaises(ReferenceError, self.company.search, 1000)


class TestManagerHierarchy(unittest.TestCase):

    def setUp(self):
        self.employees = [Employee({  "id": 0, "department": 10, "cost_center":10, "manager_id": None,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 14, "department": 10, "cost_center":10, "manager_id":0,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10})]
        self.company = Company(self.employees)
        self.actual_employee = Employee({ "id": 14, "department": 10, "cost_center":10, "manager_id":0,
                                        "location": 10, "lowest_dir_id":10, "job_family": 10})
        self.actual_manager = Employee({ "id": 0, "department": 10, "cost_center":10, "manager_id":-1,
                                        "location": 10, "lowest_dir_id":10, "job_family": 10})

    def test_get_manager(self):
        # Tests that a companys manager is retrieved
        employee = Employee({ "id": 14, "department": 10, "cost_center":10, "manager_id":0,
                                        "location": 10, "lowest_dir_id":10, "job_family": 10})
        manager = self.company.search(employee.manager_id)
        self.assertEqual(self.actual_manager, manager)

class TestDistance(unittest.TestCase):

    def setUp(self):
        self.employees = [Employee({  "id": 0, "department": 10, "cost_center":10, "manager_id": None,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 1, "department": 10, "cost_center":10, "manager_id":0,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 2, "department": 10, "cost_center":10, "manager_id":0,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 8, "department": 10, "cost_center":10, "manager_id":0,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 14, "department": 10, "cost_center":10, "manager_id":2,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 11, "department": 10, "cost_center":10, "manager_id":2,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 9, "department": 10, "cost_center":10, "manager_id":8,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 12, "department": 10, "cost_center":10, "manager_id":8,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10})]
        self.company = Company(self.employees)
        # Company:
        #             0
        #     1       2       8
        #           11 14    9 12
        # distance(9, 12): 1
        # distance(11, 12): 2
        # distance(1, 9): 2
        # distance(1, 0): 1
        # distance(9, 9): 0
    def test_distance(self):
        # Test that employees with same manager have distance one
        employee_nine = self.company.search(9)
        employee_twelve = self.company.search(12)
        distance = self.company.distance(employee_nine, employee_twelve)
        self.assertEqual(1, distance)

    def test_same_distance(self):
        # Test that the distance between a employee and themselves is 0
        employee_nine = self.company.search(9)
        distance = self.company.distance(employee_nine, employee_nine)
        self.assertEqual(0, distance)

    def test_max_distance(self):
        # Test that the distance between two employees returns the max length of manager chain
        employee_nine = self.company.search(9)
        employee_one = self.company.search(1)
        distance = self.company.distance(employee_nine, employee_one)
        self.assertEqual(2, distance)

    def test_level_distance(self):
        # Test distance between employees on the same level but with different managers
        employee_eleven = self.company.search(11)
        employee_twelve = self.company.search(12)
        distance = self.company.distance(employee_eleven, employee_twelve)
        self.assertEqual(2, distance)

    def test_manager_distance(self):
        # Test that the distance to CEO is the length of the path to the CEO
        employee_twelve = self.company.search(12)
        ceo = self.company.search(0)
        distance = self.company.distance(ceo, employee_twelve)
        self.assertEqual(2, distance)


if __name__ == '__main__':
    unittest.main()
