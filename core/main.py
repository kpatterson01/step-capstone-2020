
# File to output data for visualizing regression of employees attribute similarity vs usage similarity.

import csv
import json
from random import randint
import pickle

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Custom classes to represent an Employee, a Company, and a Resource
from employee import Employee
from company import Company
from resource import Resource


# Read in employee attributes table and sort by manager id
employee_attributes = pd.read_csv("../../data/user.csv") #NOTE: Currently a fake dataset
employee_attributes = employee_attributes.fillna(-1) # Replace all None values with -1
employee_attributes = employee_attributes.sort_values(by=["anon_manager_person_id"], ascending=True)
employee_attributes.to_csv("../../data/sorted_user.csv", index=False)


# Read in lines of employee data and create list of employee objects
employees = []
with open('../../data/sorted_user.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for user in reader:
        attributes = {}
        attributes["id"] = user[0]
        attributes["department"] = user[1]
        attributes["cost_center"] = user[2]
        attributes["manager_id"] = user[3]
        attributes["location"] = user[4]
        attributes["lowest_dir_id"] = user[5]
        attributes["job_family"] = user[6]
        employee = Employee(attributes)
        employees.append(employee)

# Create the company
company = Company(employees)

for employee in company.employees:
    print(employee.reports)

# Output JSON file of hierarchy for Tree visualization
with open('../../data/company_hierarchy.json', 'w') as outfile:
    json.dump(company_hierarchy, outfile, indent=2, sort_keys=True)


# Read in employee to resources data and attach list of resources accessed objects to every employee
employee_resources = pickle.load(open('../data/employee_resource_map.pkl', 'rb'))
for employee in company.employees:
    if(employee_resources.get(employee.id) is not None):
        for resource in employee_resources.get(employee.id):
            employee.add_resource(resource)

# Sample N pairs of employees and calculate distance and usage similarity metrics for those pairs

# (sample function from utilities/distance_validation.py)
def sample(num, low, high, company):
    """Creates a dataframe that contains sample user pairs and their euclidean distances from.

    The range for low - high is 0 - 268027 based on number of entries in user.csv.
    Args:
        num(int): Number of pairs to sample.
        low(int): Lower bound of range of user ids. Ex: To sample user_id's in range from 0-50, low = 0, high = 50.
        high(int): Upper bound of range of user ids.
        company: Company with employees.

    Returns:
        random_sample(DataFrame): A table with user pairs and their l2 distances.
    """
    random_sample = pd.DataFrame(columns = ["user_one_id", "user_two_id", "distance", "usage_similarity"])
    for i in range(num):
        employee_one = company.search(randint(low, high))
        employee_two = company.search(randint(low, high))
        dist = company.distance(employee_one, employee_two)
        usage_similarity = company.usage_similarity(employee_one, employee_two)
        random_sample = random_sample.append({"user_one_id": employee_one.id,
                                            "user_two_id": employee_two.id,
                                            "distance": dist,
                                            "usage_similarity": usage_similarity},
                                            ignore_index=True)

    return random_sample

# Output pairs and respective metrics in a csv
metric_data = sample(50, 0, 50, company)
metric_data = pd.to_csv("../../data/metric_data.csv")
