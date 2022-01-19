# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 21:12:52 2021

@author: AKayal
"""
import epai_3_13_lazy_iterator_generator
from epai_3_13_lazy_iterator_generator import *

class parking_tickets:
    def __init__(self):
        pass
    
    @property
    def return_file_iterator(self,chunk_size=1):
        
        """Lazy function (generator) to read a file piece by piece.
        https://stackoverflow.com/questions/519633/lazy-method-for-reading-big-file-in-python
        """
        with open("nyc_parking_tickets_extract-1.csv", encoding='utf8', errors='ignore') as file_parking:
            yield from file_parking   

      
