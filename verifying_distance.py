# Created by Tedi Miitku 07/07/20
# This script is for verifying our euclidean distance assumption on
# the 7D Googler attribute vector space.
import math
import random
import pandas as pd
import numpy as np

#Take in Googler attribute data as DataFrame
googler_data = pd.read_csv("data/googler_attribute_table.csv")
googler_data = googler_data.fillna(0) #Replace null values with 0


#Normalizing data
from sklearn.preprocessing import MinMaxScaler
min_max_scaler = MinMaxScaler()
googler_data.iloc[:,0:7] = min_max_scaler.fit_transform(googler_data.iloc[:,0:7])

print(googler_data.head())

#Create distance function to measure l2 distance between two Googlers
#(Probably want to encodify into a Googler class down the line)
def l2_distance(googler_one, googler_two, num):
    """Return the distance of two Googlers in 7D vector space.
    Args:
        @googler_one(1D array): Googler attribute values in 1x7 array. ex. [3, 5, 6, 6, 9, 10, 0]
        @googler_two(1D array): Googler attribute values in 1x7 array.
        @num(int): Number of attributes to calculate distance on.
    Returns:
        int: Euclidean distance between Googlers.
    """
    # Euclidean distance function:
    # sqrt((googler_one_attr1-googler_two_attr1)^2 + (googler_one_attr2-googler_two_attr2)^2 + ......... +
    #                                                                   (googler_one_attr7-googler_two_attr7)^2)
    sub = []
    for i in range(num):
        subtract_val  = googler_one[i] - googler_two[i]
        sub.append(subtract_val**2)
    sum = 0
    for i in range(num):
        sum += sub[i]
    return math.sqrt(sum)

#Calculate distances between several pairs of randomly sampled Googlers
def sample(num, size):
    """Creates a dataframe that contains sample Googler pairs and their euclidean distances from.

    Args:
        num(int): Number of pairs to sample.
        size(int): Range of user ids. Ex: If user_id's range from 0-50, size = 50.
    Returns:
        random_sample(DataFrame): A table with googler pairs and their l2 distances.
    """
    random_sample = pd.DataFrame(columns = ["user_one_id", "user_two_id", "l2"])
    for num in range(num):
        user_one_id = random.randint(0, size)
        user_two_id = random.randint(0, size)

        googler_one_attributes = googler_data.iloc[user_one_id].values[1:6 + 1]
        googler_two_attributes = googler_data.iloc[user_two_id].values[1:6 + 1]
        l2 = l2_distance(googler_one_attributes, googler_two_attributes, 6)

        random_sample = random_sample.append({"user_one_id": user_one_id,
                                            "user_two_id": user_two_id,
                                            "l2": l2 },
                                            ignore_index=True)
    return random_sample

test_data = sample(5,5)
test_data.to_csv(path_or_buf="data/test_data.csv", index=False)
