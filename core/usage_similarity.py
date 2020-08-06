
# Created by Tedi Mitiku
# Function to calculate usage similarity given to lists of resources.

def usage_similarity(resource_list_one, resource_list_two):
    """ Calculates usage similarity between two lists of resources

    Args:
        resource_list_one: A list of tuples containing attribtus representing a resource.
        resource_list_two: A list of tuples containing attribtus representing a resource.

    """
    # Convert list of tuples to set of tuples
    resource_set_one = set()
    resource_set_two = set()
    for resource in resource_list_one:
        resource_set_one.add((resource[0], resource[1]))
    for resource in resource_list_two:
        resource_set_two.add((resource[0], resource[1]))
    # Take intersection to find num of common resources
    num_in_common = len(resource_set_one.intersection(resource_set_two))
    num_total = len(resource_set_one) + len(resource_set_two) - num_in_common
    if(num_total == 0 or num_in_common == 0):
        usage_similarity = 0
    else:
        usage_similarity = int((num_in_common/num_total)*100)
    return usage_similarity
