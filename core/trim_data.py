
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

def read_employees(company_hierarchy):
    """ Recursive function to get a list of employee ids in the tree"""
    if(company_hierarchy.get("Reports") is None):
        small_employee_ids.add(int(company_hierarchy.get("Employee")))
        return

    small_employee_ids.add(int(company_hierarchy.get("Employee")))
    for report in company_hierarchy.get("Reports"):
        company_hierarchy = report
        read_employees(company_hierarchy)

read_employees(small_company)
print(small_employee_ids)
print(len(small_employee_ids))

big_user = pd.read_csv("../../data/sorted_user.csv")

for index, row in big_user.iterrows():
    if(int(row["anon_person_id"]) not in small_employee_ids):
        big_user.drop(index, inplace=True)

small_user = big_user
small_user.to_csv("../../data/smalldata/small_user.csv")
print(small_user)
