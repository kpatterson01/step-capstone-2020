# This file contains some useful functions for metrics regarding provisioning
# Author: Dean Alvarez
import pickle
from .employee import Employee
from .resource import Resource
import csv
from .parsing.syntax_tree import Syntax_Tree
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

def load_resource_map_from_pickle(file_path):
    LOAD_PATH = file_path #"../data/resource_map.pkl"
    resource_map = pickle.load(open(LOAD_PATH,"rb"))
    return resource_map


def load_resource_map_from_csv(file_path):
    LOAD_PATH = file_path
    resource_map = {}
    with open(LOAD_PATH, 'r', newline='') as f:
        reader = csv.reader(f)
        next(reader) #skip header line
        for row in reader:
            r = Resource(row[4],row[5])
            if r not in resource_map:
                resource_map[r] = set()
            resource_map[r].add(int(row[0]))
    return resource_map


def load_company(file_path):
    LOAD_PATH = file_path
    company = set()
    with open(LOAD_PATH, 'r') as f:
        reader = csv.reader(f)
        next(reader) #skip header line
        for user in reader:
            attributes = {}
            if user[0] == 'null':
                attributes["id"] = -1
            else:
                attributes["id"] = int(float(user[0]))
            if user[1] == 'null':
                attributes['department'] = -1
            else:
                attributes["department"] = int(float(user[1]))
            if user[2] == 'null':
                attributes["cost_center"] = -1
            else:
                attributes["cost_center"] = int(float(user[2]))
            if user[3] == 'null':
                attributes["manager_id"] = -1
            else:
                attributes["manager_id"] = int(float(user[3]))
            if user[4] == 'null':
                attributes["location"] = -1
            else:
                attributes["location"] = int(float(user[4]))
            if user[5] == 'null':
                attributes["lowest_dir_id"]  = -1
            else:
                attributes["lowest_dir_id"]  = int(float(user[5]))
            if user[6] == 'null':
                attributes["job_family"] = -1
            else:
                attributes["job_family"] = int(float(user[6]))
            employee = Employee(attributes)
            company.add(employee)

    print("Company size: %d" % len(company))

    return company


if __name__ == "__main__":
    resource_map = load_resource_map_from_csv("../../data/user_resources.csv")
    company = load_company("../../data/users.csv")

    example_resource = Resource(411231,2072)
    example_rule = 'department == 13'
    syntax_tree = Syntax_Tree(example_rule)
    metrics = get_metrics(example_resource, syntax_tree, resource_map, company)
    print(metrics)
