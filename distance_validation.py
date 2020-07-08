# Created by Tedi Mitiku 07/07/20
# This script is for verifying our euclidean distance assumption on
# the 7D Googler attribute vector space.

import math
import random
import pandas as pd
import numpy as np

#Take in Googler attribute data as DataFrame
googler_data = pd.read_csv("data/googler_attribute_table.csv")
googler_data = googler_data.fillna(0) #Replace null values with 0

#Variable to adjust features to include (b/c sample data missing a column)
num_col = 6

#Normalizing function incorporated by Kayla Patterson
#TODO: Implement normalization function from Kayla
from sklearn.preprocessing import MinMaxScaler
min_max_scaler = MinMaxScaler()
googler_data.iloc[:,0:num_col+1] = min_max_scaler.fit_transform(googler_data.iloc[:,0:num_col+1]) #should be [:,0:8] but sample data is missing a column

print(googler_data.head())

# Create distance function to measure l2 distance between two Googlers
# Euclidean distance function:
# sqrt((googler_one_attr1-googler_two_attr1)^2 + (googler_one_attr2-googler_two_attr2)^2 + ......... +
#                                                                   (googler_one_attr7-googler_two_attr7)^2)
#(Probably want to wrap into a Googler class down the line)
def l2_distance(googler_one, googler_two):
    """Return the distance of two Googlers in 7D vector space.
    Args:
        @googler_one(1D array): Googler attribute values in 1x7 array. ex. [3, 5, 6, 6, 9, 10, 0]
        @googler_two(1D array): Googler attribute values in 1x7 array.
    Returns:
        int: Euclidean distance between Googlers.
    """
    sub = []
    for i in range(num_col): #should be range(7) but sample data is missing a column
        subtract_val  = googler_one[i] - googler_two[i]
        sub.append(subtract_val**2)
    sum = 0
    for i in range(num_col):
        sum += sub[i]
    return math.sqrt(sum)

#Calculate distances between several pairs of randomly sampled Googlers
def sample(num, low, high, distance):
    """Creates a dataframe that contains sample Googler pairs and their euclidean distances from.

    Args:
        num(int): Number of pairs to sample.
        low(int): Lower bound of range of user ids. Ex: To sample user_id's in range from 0-50, low = 0, high = 50.
        high(int): Upper bound of range of user ids.
        distance(function): A function
    Returns:
        random_sample(DataFrame): A table with googler pairs and their l2 distances.
    """
    random_sample = pd.DataFrame(columns = ["user_one_id", "user_two_id", "l2"])
    for num in range(num):
        user_one_id = random.randint(low, high)
        user_two_id = random.randint(low, high)

        googler_one_attributes = googler_data.iloc[user_one_id].values[1:num_col+1] #should be [1:8] but sample data is missing a column
        googler_two_attributes = googler_data.iloc[user_two_id].values[1:num_col+1]
        l2 = distance(googler_one_attributes, googler_two_attributes)

        random_sample = random_sample.append({"user_one_id": user_one_id,
                                            "user_two_id": user_two_id,
                                            "l2": l2 },
                                            ignore_index=True)
    return random_sample

#Sample 10 pairs from Googlers with user id 0-10
test_data = sample(10, 0, 50, l2_distance)
test_data.to_csv(path_or_buf="data/test_data.csv", index=False)
