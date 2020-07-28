
import csv
import json
from random import randint
import pickle

import numpy as np
import pandas as pd

from company import Company
from employee import Employee

with open('../../data/company_hierarchy.json', 'r') as infile:
    small_company = json.load(infile)

small_employee_ids = set()
traverse = small_company

def read_employees_from_tree(company_hierarchy):
    """ Recursive function to get a list of employee ids in the tree"""
    if(company_hierarchy.get("Reports") is None):
        small_employee_ids.add(int(company_hierarchy.get("Employee")))
        return

    small_employee_ids.add(int(company_hierarchy.get("Employee")))
    for report in company_hierarchy.get("Reports"):
        company_hierarchy = report
        read_employees_from_tree(company_hierarchy)

read_employees_from_tree(small_company)
print(small_employee_ids)
print(len(small_employee_ids))

# big_user = pd.read_csv("../../data/sorted_user.csv", chunksize=10000, iterator=True)
# for chunk in big_user:
#     for index, row in chunk.iterrows():
#         if(int(row["anon_person_id"]) not in small_employee_ids):
#             chunk.drop(index, inplace=True)
#             chunk.to_csv("../../data/smalldata/small_user.csv", mode='a', index=False)

# columns = ["anon_person_id", "anon_department", "anon_cost_center_num", "anon_manager_person_id",
#         "anon_location_country","anon_lowest_dir_person_id", "anon_visible_job_family", "anon_person_type"]
#
# small_user = pd.DataFrame(columns=columns)
#
# with open('../../data/sorted_user.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for user in reader:
#         if(int(user[0]) in small_employee_ids):
#             employee_data = { "anon_person_id": user[0],
#                             "anon_department": user[1],
#                             "anon_cost_center_num": user[2],
#                             "anon_manager_person_id": user[3],
#                             "anon_location_country": user[4],
#                             "anon_lowest_dir_person_id": user[5],
#                             "anon_visible_job_family": user[6],
#                             "anon_person_type": user[7] }
#             small_user = small_user.append(employee_data, ignore_index=True)
#
#
# small_user.to_csv("../../data/smalldata/small_user.csv", index=False)
# print(small_user)


columns = ["anon_person_id", "anon_department", "anon_cost_center_num", "anon_manager_person_id",
        "anon_location_country","anon_lowest_dir_person_id", "anon_visible_job_family", "anon_person_type"]

small_usage = pd.DataFrame(columns=columns)

with open('../../data/user-resource-2009.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for resource in reader:
        if(int(user[0]) in small_employee_ids):
            usage_data = { "anon_person_id": resource[0],
                        "access_date": resource[1],
                        "resource_attr_1": resource[2],
                        "resource_attr_2": resource[]
                        }
            small_usage = small_usage.append(employee_data, ignore_index=True)

small_usage.to_csv("../../data/smalldata/small_usage.csv", index=False)
print(small_usage)
