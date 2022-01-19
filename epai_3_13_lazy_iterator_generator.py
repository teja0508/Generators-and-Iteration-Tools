# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 20:50:07 2021

@author: AKayal
"""
import math
from decimal import *
import collections
# "regular" namedtuples
from collections import namedtuple
from typing import List, NamedTuple


from datetime import date
import pandas as pd


class parking_details(NamedTuple):
    """
    Using the typing module, we can be even more explicit about our data structures.
    
    https://realpython.com/python-namedtuple/

    """
    summonsNumber: int
    plateID: str
    registrationState: str
    plateType: str
    issueDate: date
    violationCode: int
    vehicleBodyType: int
    vehicleMake: str
    violationDescription: str
    
    def setvalue(self,valuelist):
        
        pass

