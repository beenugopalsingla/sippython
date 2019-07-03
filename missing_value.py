# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:36:35 2019

@author: beenugopalsingla sip

"""

import pandas as pd
import numpy as np

data = {'names':['rahul','tanisha','mayank','nikhil','abhishek'], 'hr':[50,60,85,45,96], 'eng':[56,95,75,85,83], 'sci':[63,85,70,50,87]}
df = pd.DataFrame(data)
df
df.describe
df.shape
df.size
data = pd.DataFrame({'names':['rahul','tanisha','mayank','nikhil','abhishek'], 'hr':[50,60,85,45,96], 'eng':[56,95,75,85,83], 'sci':[63,85,70,50,87]})

data.set_index('names', inplace=True)
data
data.mean()
data.mean(axis=0)
data.mean(axis=1)
ax = data.plot.bar()

data = data.reindex(['shreya','rahul','mishra_ji','mayank','yash','abhijeet','sonali','tanisha','roy','nikhil','abhishek'])
data
data.isnull()
data.notnull()
data.isna()
data.isna()==data.isnull()
data.isna()==data.notnull()
data.hr.isnull()
data.sci.isnull().sum()
data.isnull().sum()
data.fillna(10, inplace=False)
data.dtypes
data


data.fillna(method='pad')
data.fillna(method='backfill', axis=1)

data.dropna()
data.mean(axis=1)
meaneng = data.eng.mean()

data['eng'].fillna(meaneng, inplace=True)
data
data.columns
data['hr'].fillna(33, inplace=True)
data['sci'].fillna(35, inplace=True)
data
data.mean()
data.plot.bar()
#summary  
#learned to see the missing values and then how to fill those missing values with numbers..