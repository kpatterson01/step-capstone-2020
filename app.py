from flask import Flask, request, render_template
import json
from capstone2020.core.company import Company
from capstone2020.core.employee import Employee
from capstone2020.core.resource import Resource


app = Flask(__name__)

# Create company object from list of employees (Need a pkl with a list of empoyees)
employees = [Employee({  "id": 0, "department": 10, "cost_center":10, "manager_id": -1,
                            "location": 10, "lowest_dir_id":10, "job_family": 10}),
                Employee({   "id": 1, "department": 10, "cost_center":10, "manager_id":0,
                            "location": 10, "lowest_dir_id":10, "job_family": 10}),
                Employee({   "id": 2, "department": 10, "cost_center":10, "manager_id":0,
                            "location": 10, "lowest_dir_id":10, "job_family": 10}),
                Employee({   "id": 8, "department": 10, "cost_center":10, "manager_id":0,
                            "location": 10, "lowest_dir_id":10, "job_family": 10}),
                Employee({   "id": 7, "department": 10, "cost_center":10, "manager_id":8,
                            "location": 10, "lowest_dir_id":10, "job_family": 10})]

# Add resources to employee objects (Need a pkl with a list Resources)
employees[0].add_resource(Resource(1,1))
employees[1].add_resource(Resource(1,1))
employees[2].add_resource(Resource(2,3))
employees[3].add_resource(Resource(2,3))

# Need a pkl for company objects
company = Company(employees)

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
    except:
        return failure_response("One or more employees not found.")
    distance = company.distance(employee_one, employee_two)
    return success_response(distance)

@app.route("/api/usage", methods=["POST"])
def calculate_usage_similarity():
    body = json.loads(request.data)
    try:
        employee_one = company.search(int(body.get("employee_one_id")))
        employee_two = company.search(int(body.get("employee_two_id")))
    except:
        return failure_response("One or more employees not found.")
    usage_similarity = company.usage_similarity(employee_one, employee_two)
    return success_response(usage_similarity)

if __name__ == "__main__":
    app.run()
