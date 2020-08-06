
# Test methods in Company class.

import unittest
from company import Company
from employee import Employee
from resource import Resource
import json

class TestManagerialHierarchy(unittest.TestCase):

    def setUp(self):
        self.employees = [Employee({  "id": 0, "department": 10, "cost_center":10, "manager_id": -1,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 1, "department": 10, "cost_center":10, "manager_id":0,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 2, "department": 10, "cost_center":10, "manager_id":0,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 8, "department": 10, "cost_center":10, "manager_id":0,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 7, "department": 10, "cost_center":10, "manager_id":8,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10})]
        self.company = Company(self.employees, 0)
        # Company:
        #             0
        #     1       2       8
        #                   7

        self.actual_hierarchy = {"Employee": 0, "Reports":[ {"Employee": 1},
                                                             {"Employee": 2 },
                                                             {"Employee": 8, "Reports":[ {"Employee": 7 }]}
                                                                        ]}

    def test_hierarchy(self):
        # Test that the dictionary hierarchy is created correctly
        company_hierarchy = self.company.hierarchy
        self.assertEqual(self.actual_hierarchy, company_hierarchy)


class TestMaxDepth(unittest.TestCase):

    def setUp(self):
        self.employees = [Employee({  "id": 0, "department": 10, "cost_center":10, "manager_id": -1,
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
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 18, "department": 10, "cost_center":10, "manager_id":9,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 4, "department": 10, "cost_center":10, "manager_id":18,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10})]
        self.company = Company(self.employees, 0)
        # Company One:
        #             0
        #     1       2       8
        #           11 14    9 12
        #                   18
        #                     4
    def test_max_depth(self):
        #Test max depth of this company is 4
        depth = self.company.depth
        self.assertEqual(4, depth)

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.employees = [Employee({  "id": 0, "department": 10, "cost_center":10, "manager_id": -1,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 14, "department": 10, "cost_center":10, "manager_id":2,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10})]
        self.company = Company(self.employees, 0)
        self.actual_employee = Employee({ "id": 14, "department": 10, "cost_center":10, "manager_id":2,
                                        "location": 10, "lowest_dir_id":10, "job_family": 10})

    def test_finds_employee(self):
        #Test that the correct employee is found
        self.assertEqual(self.actual_employee, self.company.search(14))

    def test_raises_error(self):
        #Test that an error is thrown when searching for employee that doesn't exist
        self.assertRaises(ReferenceError, self.company.search, 1000)

class TestDistance(unittest.TestCase):

    def setUp(self):
        self.employees = [Employee({  "id": 0, "department": 10, "cost_center":10, "manager_id": -1,
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
        self.company = Company(self.employees, 0)
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

class TestUsageSimilarity(unittest.TestCase):

    def setUp(self):
        self.employees = [Employee({  "id": 0, "department": 10, "cost_center":10, "manager_id": 5,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10}),
                        Employee({   "id": 1, "department": 10, "cost_center":10, "manager_id":5,
                                    "location": 10, "lowest_dir_id":10, "job_family": 10})]
        self.company = Company(self.employees, 0)
        self.resource_one = Resource(1, 2)
        self.resource_two = Resource(5, 6)
        self.resource_three = Resource(1, 4)
        self.resource_four = Resource(2, 5)

    def test_usage_similarity_metric(self):
        # Test that correct usage similarity metric is returned for a resource in common
        employee_one = self.company.search(0)
        employee_two = self.company.search(1)

        employee_one.add_resource(self.resource_one)
        employee_one.add_resource(self.resource_two)

        employee_two.add_resource(self.resource_two)
        employee_two.add_resource(self.resource_four)

        usage_similarity = self.company.usage_similarity(employee_one, employee_two)
        self.assertAlmostEqual(0.33333333, usage_similarity)

    def test_no_similarity(self):
        # Test that zero is returned if two employees have no resources in common
        employee_one = self.company.search(0)
        employee_two = self.company.search(1)

        employee_one.add_resource(self.resource_one)
        employee_one.add_resource(self.resource_two)

        usage_similarity = self.company.usage_similarity(employee_one, employee_two)
        self.assertAlmostEqual(0, usage_similarity)

    def test_no_resources(self):
        # Test that zero is returned with no division error if employees have no resources
        employee_one = self.company.search(0)
        employee_two = self.company.search(1)

        usage_similarity = self.company.usage_similarity(employee_one, employee_two)
        self.assertAlmostEqual(0, usage_similarity)

if __name__ == '__main__':
    unittest.main()
