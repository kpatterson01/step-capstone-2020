#This is an external sort for CSV files
#Algorithm info:
# read and sort a chunk of the data using conventional methods
# write sorted data to disk
# repeat until all data is in sorted chunks
# read small amount from each chunk
# merge these mini-chunks
#visit https://en.wikipedia.org/wiki/External_sorting for more info

import csv
import os
import pandas as pd
import heapq

class Row:
    #this is a custom class for the row data in our user_resources dataset.
    #the purpose of this is so we can create a heap for mering chunks
    def __init__(self,user_id,access_date,access_hour,access_minute,resource_attr_1,resource_attr_2,reader_number):
        self.user_id = int(user_id)
        self.access_date = access_date
        self.access_hour = access_hour
        self.access_minute = access_minute
        self.resource_attr_1 = resource_attr_1
        self.resource_attr_2 = resource_attr_2
        self.reader_number = reader_number

    def __eq__(self,other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.user_id == other.user_id

    def __lt__(self,other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.user_id < other.user_id


def write_csv_out(row, out_path):
    info = [row.user_id,row.access_date,row.access_hour,row.access_minute,
            row.resource_attr_1,row.resource_attr_2]
    with open(out_path, 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(info)

#number of lines per chunk. This should be changed based on how much ram is avaliable
chunk_size = 100000

input_path = os.path.expanduser("~/data/user_resources.csv")
output_path = os.path.expanduser("./sorted_user_resources.csv")

chunk_number = 0
reader = pd.read_csv(input_path,chunksize=chunk_size)
for chunk in reader:
    sorted_chunk = chunk.sort_values(by=['user_id'])
    sorted_chunk.to_csv('tmp%d.csv'%chunk_number)
    chunk_number+= 1


readers = []
heap = []
heapq.heapify(heap)
for i in range(chunk_number):
    f = open('tmp%d.csv'%i)
    reader = csv.reader(f,delimiter=',')
    readers.append(reader)
    next(reader) #skip header
    row = next(reader)
    row_obj = Row(row[1],row[2],row[3],row[4],row[5],row[6],i)
    heapq.heappush(heap,row_obj)

heapq.heapify(heap)

while(len(heap) > 0):
    min_item = heapq.heappop(heap)
    write_csv_out(min_item,output_path)
    reader_number = min_item.reader_number
    reader = readers[reader_number]
    try:
        row = next(reader)
        row_obj = Row(row[1],row[2],row[3],row[4],row[5],row[6],reader_number)
        heapq.heappush(heap,row_obj)
    except:
        pass
