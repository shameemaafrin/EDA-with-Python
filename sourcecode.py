# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 19:36:32 2022

@author: jsham
"""



import pandas as pd
import matplotlib.pyplot as plt
import os

#Displays the working directory
os.getcwd()  

#to read the dataset
tordata_orig = pd.read_csv("1950-2020_actual_tornadoes.csv")
tordata = pd.read_csv("1950-2020_actual_tornadoes.csv") 

# displays few data
tordata.info()
tordata

# displays the data types
tordata.dtypes

# displays all months
tordata.mo

#Histogram to display month
tordata.mo.plot(kind='hist')

#Histogram to display year
x=tordata.yr
plt.hist(x, bins = 35)
plt.show()

#displays sorted values
tordata.sort_values("mo")
tordata.sort_values("st")

#bar graph to compare  month and magnitude
x=tordata['mo']
y=tordata['mag']
plt.xlabel('MONTH')
plt.ylabel('MAGNITUDE')
plt.bar(x,y)
plt.show()

#groups two or more values for better analysis
tordata.groupby(['mo'])[['mag']].sum() 
tordata.groupby(['st'])[['inj','fat']].sum() 
tordata.groupby(['st'])['inj'].mean()
tordata.groupby(['st'])['fat'].mean()
tordata.groupby(['st'])[['inj','fat']].mean()

#explains how many times the state has occured
torstate=tordata.groupby(['st']).size()
print(torstate)

#bar graph to show state and number of tornados
x=tordata['st']    #workssss
y=tordata['stn']
plt.xticks(fontsize=5,rotation=90)
plt.xlabel('STATE')
plt.ylabel('NUMBER OF TORNADOES')
plt.bar(x,y)
plt.show()

#bar graph to show month and number of tornados
x=tordata['mo']    
y=tordata['stn']
plt.xticks(fontsize=5,rotation=90)
plt.xlabel('MONTH')
plt.ylabel('NUMBER OF TORNADOES')
plt.bar(x,y)
plt.show()

#bar graph to show month and magnitude
x=tordata['mo']    
y=tordata['mag']
plt.xticks(fontsize=5,rotation=90)
plt.xlabel('MONTH')
plt.ylabel('MAGNITUDE')
plt.bar(x,y)
plt.show()

#boxplot to show year
plt.boxplot(tordata.yr)






