# This file contains some useful functions for metrics regarding provisioning
import pickle
from employee import Employee
from resource import Resource
import csv

# gets provisioning metrics for a given resource given a rule
# rule should be a function that takes a user and returns a boolean (examples below)
def get_metrics(resource, rule, resource_map, company):
    actual_users = resource_map[resource]
    predicted_users = set()
    for user in company:
        if rule(user):
            predicted_users.add(user.id)
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
    LOAD_PATH = "../data/resource_map.pkl"
    resource_map = pickle.load(open(LOAD_PATH,"rb"))
    return resource_map

def load_company():
    LOAD_PATH = "../data/users.csv"
    company = set()
    with open(LOAD_PATH, 'r') as f:
        reader = csv.reader(f)
        next(reader) #skip header line
        for user in reader:
            attributes = {}
            if user[0] == 'null':
                attributes["id"] = None
            else:
                attributes["id"] = int(user[0])
            if user[1] == 'null':
                attributes['department'] = None
            else:
                attributes["department"] = int(user[1])
            if user[2] == 'null':
                attributes["cost_center"] = None
            else:
                attributes["cost_center"] = int(user[2])
            if user[3] == 'null':
                attributes["manager_id"] = None
            else:
                attributes["manager_id"] = int(user[3])
            if user[4] == 'null':
                attributes["location"] = None
            else:
                attributes["location"] = int(user[4])
            if user[5] == 'null':
                attributes["lowest_dir_id"]  = None
            else:
                attributes["lowest_dir_id"]  = int(user[5])
            if user[6] == 'null':
                attributes["job_family"] = None
            else:
                attributes["job_family"] = int(user[6])
            employee = Employee(attributes)
            company.add(employee)

    print("Company size: %d" % len(company))

    return company


def example_rule(user):
    return user.department == 13

def another_example_rule(user):
    return user.id == 9

if __name__ == "__main__":
    resource_map = load_resource_map()
    company = load_company()

    example_resource = Resource(411231,2072)
    metrics = get_metrics(example_resource, example_rule, resource_map, company)
    print(metrics)

    metrics = get_metrics(example_resource, another_example_rule, resource_map, company)
    print(metrics)
