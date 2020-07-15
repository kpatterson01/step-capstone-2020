
# **FILENAME SHOULD BE RENAMED**
# File to output csv for visualizing regression of attribute similarity vs usage similarity.

import csv
import numpy as np
import pandas as pd

# Custom classes to represent a Googler and Google
from Googler import Googler
from Google import Google

# Read in googler attributes table and sort by manager id
googler_attributes = pd.read_csv("../data/googler_attributes_table.csv")
googler_attributes = googler_attributes.sort_values(column=["anon_manager_person_id"], ascending=True)
googler_attributes.to_csv("../data/sorted_attribute_table_fake.csv")
print(googler_attributes)

# Read in lines of Googler data and create list of Googler objects
googlers = []
with open('../data/sorted_attribute_table_fake.csv', 'r') as f:
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
        googler = Googler(attributes)
        googlers.append(googler)

print(googlers)
#google_company = Google(googlers)
