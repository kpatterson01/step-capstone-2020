import pickle
from resource import Resource
from user import user

def get_metrics(resource, rule):
    resource_map = load_resource_map()
    actual_users = resource_map[resource]
    predicted_users = set()
    company = load_company()
    for user in company:
        if rule(user):
            predicuted_users.add(user)

    metrics = calculate_metrics(actual_users, predicted_users)
    return metrics

def calculate_metrics(actual, predicted):
    true_positive = actual.intersection(predicted_users)
    false_positive = predicted.difference(actual_users)
    false_negative = actual.difference(predicted_users)

    TP = len(true_positive)
    FP = len(false_positive)
    FN = len(false_negative)

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    return precision, recall

def load_resource_map():
    LOAD_PATH = "../../data/resource_map.pkl"
    resource_map = pickle.load(open(LOAD_PATH,"rb"))
    return resource_map

def load_company():
    LOAD_PATH = "../../data/users.csv"
    company = set()
    with open(LOAD_PATH, 'r') as f:
        reader = csv.reader(f)
        for user in reader:
            attributes = {}
            attributes["id"] = user[0]
            attributes["department"] = user[1]
            attributes["cost_center"] = user[2]
            attributes["manager_id"] = user[3]
            attributes["location"] = user[4]
            attributes["lowest_dir_id"] = user[5]
            attributes["job_family"] = user[6]
            usr = User(attrivutes)
            company.append(usr)

    return company

def example_rule(user):
    return user.manager_id == 1234

if __name__ == "__main__":
    example_resource = Resource(123,456)
    metrics = get_metrics(example_resource, example_rule)
    print(metrics)
