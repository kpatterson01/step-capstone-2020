
# File to output data for visualizing regression of employees attribute similarity vs usage similarity.

import csv, json, pickle
from random import randint

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Custom classes to represent an Employee, a Company, and a Resource
from employee import Employee
from company import Company
from resource import Resource
import usage_similarity as usage

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
        attributes["person_type"] =user[7]
        employee = Employee(attributes)
        employees.append(employee)

# Create the company
company = Company(employees, 258004)

print(company.company)
print(company.hierarchy)
print(company.employees)

# with open('../../data/smalldata/small_company_object.pkl', 'wb') as outfile:
#      pickle.dump(company, outfile)

# Load in employee to resource JSON object to get employee usage data
employee_resources = json.load(open("../../data/employee_resource_map.json", 'r'))


# Sample N pairs of employees and calculate distance and usage similarity metrics for those pairs
# (sample function from utilities/distance_validation.py)
def sample(num, low, high, employees, employee_resources):
    """Creates a dataframe that contains sample user pairs and their similarity metrics.

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

        # Remove same employee datapoints
        if (employee_one == employee_two): continue

        #Segment for no managers Check to make sure employees have no reports - Cliff
        if ((len(employee_one.reports) != 0) or (len(employee_two.reports) != 0)): continue

        # Get distance
        dist = company.distance(employee_one, employee_two)

        # Get list of resources
        employee_one_resources = employee_resources.get(str(employee_one.id))
        employee_two_resources = employee_resources.get(str(employee_two.id))

        # Check if there are no resources attached to employee
        if(employee_one_resources is None or employee_two_resources is None):
            usage_similarity = -1
        else:
            usage_similarity = usage.usage_similarity(employee_one_resources, employee_two_resources)

        random_sample = random_sample.append({"user_one_id": employee_one.id,
                                            "user_two_id": employee_two.id,
                                            "distance": dist,
                                            "usage_similarity": usage_similarity,
                                            "user_one_job": employee_one.job_family,
                                            "user_two_job": employee_two.job_family,
                                            "user_one_type": employee_one.person_type,
                                            "user_two_type": employee_two.person_type},
                                            ignore_index=True)
    return random_sample

# Output pairs and respective metrics in a csv
data = sample(500, 0, len(employees) - 1, employees, employee_resources)

# Filter out pairs with no usage data
# metric_data = data[(data["usage_similarity"] > 0) & (data["distance"] > 0)]
# metric_data.to_csv("../../data/more_metric_data_no_reports.csv", mode='a', header=False, index=False)
# print(metric_data)
