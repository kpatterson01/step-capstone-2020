# Created by Kayla Patterson 07/16/2020
# This file maps each employee to their perspective
# resources and exports it as a pickle file

import pandas as pd
import os.path
import pickle

from resource import Resource

if __name__ == "__main__":

    file_path = os.path.expanduser("../data/sorted_usage_table.csv")
    read_file = pd.read_csv(file_path, chunksize = 10000)
    employee_resources = {}

    # Reads csv file and use a dictionary to map employees id
    # to a set of their resources
    for chunk in read_file:
        for index, row in chunk.iterrows():
            employee_id = int(row['user_id'])
            resource = Resource(row['resource_attr_1'], row['resource_attr_2'])

            # If employee_id is in dictionary add current resource
            # else create new dictionary key and map it to a new set of resources
            if employee_id in employee_resources:
                employee_resources[employee_id].add(resource)
            else:
                employee_resources[employee_id] = set()
                employee_resources[employee_id].add(resource)


    with open(os.path.expanduser("../data/employee_resource_map.pkl"), "wb") as f:
        pickle.dump(employee_resources,f)
