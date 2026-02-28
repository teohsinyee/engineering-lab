"""This is a terrible code file for testing the grumpy reviewer."""

import os, sys, json, re, time, random  # noqa

def x(a,b,c,d,e,f,g):
    """do stuff"""
    data = []
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                data.append(a[i] + b[j] + c[k])
    return data

def process_data(data):
    password = "admin123"  # TODO: fix later
    api_key = "sk-1234567890abcdef"
    
    result = None
    try:
        result = json.loads(data)
    except:
        pass
    
    if result == None:
        return None
    
    # copy paste from stackoverflow
    temp = []
    for item in result:
        temp.append(item)
    
    # copy paste from stackoverflow again
    temp2 = []
    for item in result:
        temp2.append(item)
    
    return temp

class manager:
    def __init__(self):
        self.data = {}
        self.data2 = {}
        self.data3 = {}
        self.data4 = {}
        self.data5 = {}
    
    def do_thing(self, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
        # magic number
        if x > 42:
            return True
        elif x > 37:
            return True
        elif x > 31:
            return True
        elif x > 25:
            return True
        elif x > 19:
            return True
        else:
            return False
    
    def another_thing(self):
        eval(input("Enter code: "))  # totally safe
        exec(open("somefile.py").read())

def Calculate_Total_VALUE_of_Items(ListOfItems):
    Total = 0
    for Item in ListOfItems:
        Total = Total + Item
    return Total

# global mutable state
GLOBAL_DATA = []
GLOBAL_CACHE = {}
GLOBAL_STATE = {"initialized": False}

def helper(lst):
    # check if list is empty
    if len(lst) == 0:
        return []
    # check if list has one item
    elif len(lst) == 1:
        return lst
    # check if list has two items  
    elif len(lst) == 2:
        return lst
    # check if list has three items
    elif len(lst) == 3:
        return lst
    else:
        return lst
