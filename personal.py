# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:13:22 2019

@author: beenugopalsingla sip

"""

list1 = [1,2,3,4]
list1
type(list1)

list2 = ['a','b','c']
list2

tuple1 = [1,2,'a','b']
tuple1

dict1 = {1:'bgs', 2:'bc'}
dict1

set1 = set(['ind','aus','aus'])
set1


str1='Python Programming'


for beenu in list1:
    print(beenu)

for beenu in range(1,100,10):
    print(beenu, end=', ')
    
    
for bgs in range(100,1000,2):
    print(bgs, end=', ')


for bgs in range(10,100,16):
    print(bgs, end=' ')
    
tupleFZ1 = (1,2,3,4,5,6,7,8,9)
type(tupleFZ1)

frozenset1 = frozenset(tupleFZ1)
frozenset1

name = ['ab','bc','cd','de']
rollno = [23,24,5,26] 
marks = [90,100,33,99]

mapped = zip(name, rollno, marks)
mapped = set(mapped)
mapped
namez, rollnoz, marksz = zip(*mapped)
namez

import numpy as np

np1 = np.arange(1,101)
np1
type(np1)
np?
np.sort

np2 = np.array([90,50,65,75,100])
np2
np.sort(np2)


np3 = np.array([[2,4],[3,4]])
np3
np3.size
np3.shape
np3.all
np3.searchsorted
np3.squeeze

import pandas as pd
pd?
df1 = pd.DataFrame({'rollno':[1,2,3,4], 'name':["abc","abcd","abcde","abcdef"], 'marks':[10,20,30,40]})
df1
type(df1)
