# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:11:06 2019

@author: beenugopalsingla sip

"""

import statsmodels.api as sm

dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()
mtcars=dataset_mtcars.data
