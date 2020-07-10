import pandas as pd
import os.path

class Resource:

    def __init__(self, attr_1, attr_2):
        self.attr_1 = int(attr_1)
        self.attr_2 = int(attr_2)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        else:
            return self.attr_1 == other.attr_1 and self.attr_2 == other.attr_2

    def __hash__(self):
        string_representation = "%d-%d" % (self.attr_1,self.attr_2)
        return hash(string_representation)


def overlap_ratio(set1, set2):
    num_in_common = len(set1.intersection(set2))
    total_unique_elements = len(set1)+len(set2)-num_in_common
    return num_in_common/total_unique_elements

input_path = os.path.expanduser("~/data/sorted_user_resources.csv")
reader = pd.read_csv(input_path, chunksize = 100000)
resource_users = {}

for chunk in reader:
    for index, row in chunk.iterrows():
        resource = Resource(row['resource_attr_1'],row['resource_attr_2'])
        if resource in resource_users:
            resource_users[resource].add(row['user_id'])
        else:
            resource_users[resource] = {row['user_id']}

set_itr = iter(resource_users.values())

sets = []
for i in range(10):
    sets.append(next(set_itr))

for s in sets:
    print(overlap_ratio(s,next(set_itr)))