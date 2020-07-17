# Created by Kayla Patterson 07/16/2020
# This file maps each googler to their perspective
# resources and exports it as a pickle file 

import pandas as pd 
import os.path
import pickle 

# importing Resource class 
from resource_map_creator import Resource 

if __name__ == "__main__":
   
    file_path = os.path.expanduser("~/data/sorted_user_resources.csv") 
    read_file = pd.read_csv(file_path, chunksize = 10000) 
    googler_resources = {} 
    

    # Reads csv file and use a dictionary to map googlers id 
    # to a set of their resources 
    for chunk in read_file:
        for index, row in chunk.iterrows():
            googler_id = row['user_id']
            resource = Resource(row['resource_attr_1'], row['resource_attr_2']) 
     
            # If googler_id is in dictionary add current resource 
            # else create new dictionary key and map it to a new set of resources 
            if googler_id in googler_resources:
                googler_resources[googler_id].add(resource)  
            else:
                googler_resources[googler_id] = set()
                googler_resources[googler_id].add(resource)
                

    with open(os.path.expanduser("~/data/googler_resouce_map.pkl"), "wb") as f:
        pickle.dump(googler_resources,f)
        


