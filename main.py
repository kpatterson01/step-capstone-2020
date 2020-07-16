
# **FILENAME SHOULD BE RENAMED**
# File to output data for visualizing regression of Googler attribute similarity vs usage similarity.

import csv
import numpy as np
import pandas as pd

# Custom classes to represent a Googler and Google
from Googler import Googler
from Google import Google

# Read in Googler attributes table and sort by manager id
googler_attributes = pd.read_csv("../data/googler_attribute_table_fake.csv") #NOTE: Currently a fake dataset
googler_attributes = googler_attributes.sort_values(by=["anon_manager_person_id"], ascending=True)
googler_attributes.to_csv("../data/sorted_attribute_table_fake.csv", index=False)
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

googlers = googlers[1:] #Drop labels row
print(googlers)


# Create the Google company
google = Google(googlers)
print(google.company)

# Read in googler to resources data and attach list of resources accessed objects to every Googler

# Sample N pairs of Googlers and calculate distance and usage similarity metrics for those pairs

# Output pairs and respective metrics in a csv
