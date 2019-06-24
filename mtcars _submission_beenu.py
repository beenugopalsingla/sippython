# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:11:35 2019

@author: beenugopalsingla sip

"""

import statsmodels.api as sm
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()

mtcars = dataset_mtcars.data

#structure
mtcars.describe
mtcars.dtypes

#summary 
mtcars.describe()

#print first / Last few rows
mtcars.head(5)
mtcars.head(-5)
mtcars[-3:]


#print number of rows
mtcars.rows()   #error

len(mtcars)
 mtcars.count()


#print number of columns
 mtcars.shape
 len(mtcars.columns)


#print names of columns
 mtcars.columns


#filter rows
#cars with cyl=8
mtcars_cyl8 = mtcars[mtcars.cyl == 8]
mtcars_cyl8
mtcars.cyl == 8


#cars with mpg <= 27
mtcars_mpg27 = mtcars[mtcars.mpg <= 27]
mtcars_mpg27
mtcars_mpg27.sort_values(by='mpg', ascending=False)
 
mtcars_mpg28 = mtcars[mtcars.mpg >= 27]
mtcars_mpg28
mtcars_mpg28.sort_values(by='mpg', ascending=False)


#rows match auto tx
 # comment -  i cannot understand this.. i am not able to find what is auto tx
 
 #first row
mtcars.head(1)


#last row
mtcars[-1:] 


# 1st, 4th, 7th, 25th row + 1st 6th 7th columns.

mtcars.sample(n=1)
mtcars.iloc[[1,4,7,25], [1,6,7]]


# first 5 rows and 5th, 6th, 7th columns of data frame
mtcars.iloc[[1,2,3,4,5], [5,6,7]]


#rows between 25 and 3rd last
mtcars.iloc[[25,26,27,28,29], :]


#alternative rows and alternative column
#comment : not able to find this answer


#find row with Mazda RX4 Wag and columns cyl, am
mtcars.loc[['Mazda RX4'], ['cyl']]


#find row betwee Merc 280 and Volvo 142E Mazda RX4 Wag and columns cyl, am
mtcars.loc[['Merc 280', 'Volvo 142E'], ['cyl']]


# mpg > 23 or wt < 2
mtcars_mpg23_wt2 = [mtcars[mtcars.mpg > 23], mtcars[mtcars.wt < 2]]
mtcars_mpg23_wt2


#with or condition
#find unique rows of cyl, am, gear
mtcars.drop_duplicates()  #out of context
mtcars.cyl.unique(), mtcars.am.unique(), mtcars.gear.unique()


#create new columns: first make a copy of mtcars to mtcars2
mtcars2 = mtcars
mtcars2

mtcars2['newdisp'] = mtcars['disp'] / 61 
mtcars2.head()


# multiple mpg * 1.5 and save as original column
mtcars2.mpg*1.5
mtcars2['mpg']=mtcars2.mpg*1.5
mtcars2.head()


#mission accomplished


