# This file contains some useful functions for metrics regarding provisioning
import pickle
from .employee import Employee
from .resource import Resource
import csv
from parsing.rule import Rule
import timeit

# gets provisioning metrics for a given resource given a rule
# rule should be a function that takes a user and returns a boolean (examples below)
def get_metrics(resource, rule, resource_map, company):
    actual_users = resource_map[resource]
    predicted_users = set()
    start = timeit.default_timer()
    for user in company:
        if rule.passes(user):
            predicted_users.add(user.id)
    end = timeit.default_timer()
    print("Time: ", end - start)
    print("actual: %d , predicted: %d"%(len(actual_users),len(predicted_users)))
    metrics = calculate_metrics(actual_users, predicted_users)
    return metrics

# calculates recall and precision based on actual and predicted sets
# returns a tuple: precision, recall
def calculate_metrics(actual, predicted):
    true_positive = actual.intersection(predicted)
    false_positive = predicted.difference(actual)
    false_negative = actual.difference(predicted)

    TP = len(true_positive)
    FP = len(false_positive)
    FN = len(false_negative)

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    return precision, recall

def load_resource_map():
    LOAD_PATH = "../../data/resource_employee_map.pkl"
    resource_map = pickle.load(open(LOAD_PATH,"rb"))
    return resource_map

def load_company():
    LOAD_PATH = "../../data/users.csv"
    company = set()
    with open(LOAD_PATH, 'r') as f:
        reader = csv.reader(f)
        next(reader) #skip header line
        for user in reader:
            attributes = {}
            if user[0] == 'null':
                attributes["id"] = -1
            else:
                attributes["id"] = int(user[0])
            if user[1] == 'null':
                attributes['department'] = -1
            else:
                attributes["department"] = int(user[1])
            if user[2] == 'null':
                attributes["cost_center"] = -1
            else:
                attributes["cost_center"] = int(user[2])
            if user[3] == 'null':
                attributes["manager_id"] = -1
            else:
                attributes["manager_id"] = int(user[3])
            if user[4] == 'null':
                attributes["location"] = -1
            else:
                attributes["location"] = int(user[4])
            if user[5] == 'null':
                attributes["lowest_dir_id"]  = -1
            else:
                attributes["lowest_dir_id"]  = int(user[5])
            if user[6] == 'null':
                attributes["job_family"] = -1
            else:
                attributes["job_family"] = int(user[6])
            employee = Employee(attributes)
            company.add(employee)

    print("Company size: %d" % len(company))

    return company


if __name__ == "__main__":
    resource_map = load_resource_map()
    company = load_company()

    example_resource = Resource(411231,2072)
    example_rule = Rule(None)
    metrics = get_metrics(example_resource, example_rule, resource_map, company)
    print(metrics)

