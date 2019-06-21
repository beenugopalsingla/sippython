# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:26:04 2019

@author: beenugopalsingla sip

"""

L1 = [1,2, 'SIP', 'Beenu', True]
L1
print(L1)
L1[0]
L1[0] = 99
L1
L1[1]
L1[2]
L1[1] = 20
L1

L1[0], L1[1], L1[4], L1[5]

for i in L1:
    print(i)
    
range(5); range(len(L1))
for i in range(5):
    print(i, end = ' -')
    
for i in range(len(L1)):
    print(L1[i])
    
L1[3]
L1[3].upper()
L1[0:2]
sum(L1[0:2])

len(L1)

L1.count('Beenu')

L1.append('Sana')
L1

L1.remove(99)
L1

L1.pop()
L1.pop(0)
L1

del L1[0]
L1

L2=L1
L2
L3 = L1 + L2
L3
