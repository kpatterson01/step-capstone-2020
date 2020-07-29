from flask import Flask, request, render_template
import json, pickle, csv
from capstone2020.core.company import Company
from capstone2020.core.employee import Employee
from capstone2020.core.resource import Resource

import pandas as pd

app = Flask(__name__)

# Company object - Persistently stored in pickle file
company = pickle.load(open('./data/smalldata/small_company_object.pkl', 'rb'))

# Employee to resource dictionary for usage similarity data
employee_resources = json.load(open("./data/employee_resource_map.json", 'r'))


def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code


def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hierachyTree.html")
def hierachy_tree():
    return render_template("hierachyTree.html")


@app.route("/provisionMetrics.html")
def provision_metrics():
    return render_template("provisionMetrics.html")

@app.route("/api/distance", methods=["POST"])
def calculate_distance():
    body = json.loads(request.data)
    try:
        employee_one = company.search(int(body.get("employee_one_id")))
        employee_two = company.search(int(body.get("employee_two_id")))
        distance = company.distance(employee_one, employee_two)
    except:
        return failure_response("One or more employees not found.", 500)
    return success_response(distance)

@app.route("/api/usage", methods=["POST"])
def calculate_usage_similarity():
    body = json.loads(request.data)

    try:
        employee_one = company.search(int(body.get("employee_one_id")))
        employee_two = company.search(int(body.get("employee_two_id")))
        distance = company.distance(employee_one, employee_two)
    except:
        return failure_response("One or more employees not found in company.", 500)

    employee_one_resources = employee_resources.get(str(employee_one.id))
    employee_two_resources = employee_resources.get(str(employee_two.id))
    # Check if no resources attached to employee
    if(employee_one_resources is None or employee_two_resources is None):
        return failure_response("No usage data for one or both of these employees", 500)
    else:
        # If so create set of tuples with corresponding resources for each employee
        resource_set_one = set()
        resource_set_two = set()
        for resource in employee_one_resources:
            resource_set_one.add((resource[0], resource[1]))
        for resource in employee_two_resources:
            resource_set_two.add((resource[0], resource[1]))
        usage_similarity = len(resource_set_one.intersection(resource_set_two))
    return success_response(usage_similarity)

if __name__ == "__main__":
    app.run()
