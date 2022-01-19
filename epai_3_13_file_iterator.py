# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 23:33:22 2021

@author: AKayal
"""
import epai_3_13_lazy_iterator_generator
from epai_3_13_lazy_iterator_generator import *

import epai_3_13_lazy_iterator_file_reader
from epai_3_13_lazy_iterator_file_reader import *
import pandas as pd

class FileIterator(object):
    
    """
    implementing an Iterator as a Class. One way to create iterators in Python is defining a class which implements the methods __init__ and __next__. 
    We show this by implementing a class cycle, which can be used to cycle over an iterable object forever. In other words, an instance of this class returns the element of an iterable until it is exhausted. Then it repeats the sequence indefinitely.
    https://www.python-course.eu/python3_generators.php
    """
    
    def __init__(self, iterable):
        self.iterable = iterable
        self.iter_obj = iter(iterable)
        self.parking_detailsx = ""
        self.header = True
        self.header_info =""
        self.data_frame = pd.read_csv("nyc_parking_tickets_extract-1.csv", encoding='utf8')

    def __iter__(self):
        return self
    
    def return_group_by_make(self):
        return self.data_frame.groupby("Vehicle Make")["Violation Description"].count().sort_values(ascending=False)
    
    def __next__(self):
        while True:
            try:
                if (self.header):
                    next_obj = next(self.iter_obj)
                    self.value = next_obj
                    self.header_info = ["SummonsNumber","PlateID",
                                        "RegistrationState","PlateType","IssueDate","ViolationCode","VehicleBodyType","VehicleMake","ViolationDescription"]
                    self.header = False
                else:
                    next_obj = next(self.iter_obj)
                    self.value = next_obj
                    print(next_obj)
                    # car_fine_rec = self.car_fine(self.value.split (","))
                    # car_fine = namedtuple("car_fine", self.header_info, rename=False)
                    # car_fine_rec = car_fine('car_fine',
                    #                         self.header_info[0],
                    #                         self.header_info[1],
                    #              self.header_info[2],
                    #              self.header_info[3],
                    #              self.header_info[4],
                    #              self.header_info[5],
                    #              self.header_info[6],
                    #              self.header_info[7]) 
                    self.parking_detailsx = parking_details(self.header_info[0],
                                            self.header_info[1],
                                            self.header_info[2],
                                            self.header_info[3],
                                            self.header_info[4],
                                            self.header_info[5],
                                            self.header_info[6],
                                            self.header_info[7],
                                            self.header_info[8])

                return next_obj
            except StopIteration:
                self.iter_obj = iter(self.iterable)


filerecord = parking_tickets()
# print(type(filerecord.return_file_iterator))
# for brand in filerecord.return_file_iterator:
#     print(brand, end=", ")           

 
FileIterator_x = FileIterator(filerecord.return_file_iterator)

for i in range(100):
    next(FileIterator_x)
    print(FileIterator_x.parking_detailsx)
    # print(next(x), end=", ")

print(f"Number of Violation by Car Make:{FileIterator_x.return_group_by_make()}")