
# File to output data for visualizing regression of employees attribute similarity vs usage similarity.

import csv
import json
from random import randint
import pickle

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Custom classes to represent an Employee, a Company, and a Resource
from employee import Employee
from company import Company
from resource import Resource


# Read in employee attributes table and sort by manager id
# employee_attributes = pd.read_csv("../../data/user.csv") #NOTE: Currently a fake dataset
# employee_attributes = employee_attributes.fillna(-1) # Replace all None values with -1
# employee_attributes = employee_attributes.sort_values(by=["anon_manager_person_id"], ascending=True)
# employee_attributes.to_csv("../../data/sorted_user.csv", index=False)


# Read in lines of employee data and create list of employee objects
employees = []
with open('../../data/smalldata/small_user.csv', 'r') as f:
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

print(company.company)
print(company.hierarchy)
print(company.employees)


# with open('../../data/smalldata/small_company_object.pkl', 'wb') as outfile:
#      pickle.dump(company, outfile)

# Load in employee to resource JSON object to calculate usage usage_similarit
employee_resources = json.load(open("../../data/employee_resource_map.json", 'r'))


#Sample N pairs of employees and calculate distance and usage similarity metrics for those pairs

# (sample function from utilities/distance_validation.py)
def sample(num, low, high, employees, employee_resources):
    """Creates a dataframe that contains sample user pairs and their euclidean distances from.

    The range for low - high is 0 - 268027 based on number of entries in user.csv.
    Args:
        num(int): Number of pairs to sample.
        low(int): Lower bound of range of user ids. Ex: To sample user_id's in range from 0-50, low = 0, high = 50.
        high(int): Upper bound of range of user ids.
        employees: Employees in company.
        employee_resources: Dict mapping employees to their resources.

    Returns:
        random_sample(DataFrame): A table with user pairs and their l2 distances.
    """
    random_sample = pd.DataFrame(columns = ["user_one_id", "user_two_id", "distance", "usage_similarity"])
    for i in range(num):
        rand_one= randint(low, high)
        rand_two = randint(low, high)

        employee_one = employees[rand_one]
        employee_two = employees[rand_two]

        dist = company.distance(employee_one, employee_two)

        # Get list of resources
        employee_one_resources = employee_resources.get(str(employee_one.id))
        employee_two_resources = employee_resources.get(str(employee_two.id))

        # Check if no resources attached to employee
        if(employee_one_resources is None or employee_two_resources is None):
            usage_similarity = -1
        else:
            # If so create set of tuples with corresponding resources for each employee
            resource_set_one = set()
            resource_set_two = set()
            for resource in employee_one_resources:
                resource_set_one.add((resource[0], resource[1]))
            for resource in employee_two_resources:
                resource_set_two.add((resource[0], resource[1]))
            # Take intersection to find num of common resources
            usage_similarity = len(resource_set_one.intersection(resource_set_two))

        random_sample = random_sample.append({"user_one_id": employee_one.id,
                                            "user_two_id": employee_two.id,
                                            "distance": dist,
                                            "usage_similarity": usage_similarity},
                                            ignore_index=True)
    return random_sample

# Output pairs and respective metrics in a csv
data = sample(500, 0, len(employees) - 1, employees, employee_resources)


metric_data = data[data["usage_similarity"] > 0]
metric_data.to_csv("../../data/metric_data_two.csv", mode='a', header=False, index=False)
print(metric_data)
