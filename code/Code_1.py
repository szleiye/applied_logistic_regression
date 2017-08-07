# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 11:11:05 2017

@author: Raymond
"""

import pandas as pd
import numpy as np
import pylab as pl 
import statsmodels.api as sm
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

'''-------------------------------------------------------------------
4.2.1 Methods to Examine the Scale of a Contiuous Covariate in the Logit
--------------------------------------------------------------------'''

#read the data Scale_Example
#read the data sets CHDAGE
data = pd.read_excel('D:/GitHub/applied_logistic_regression/data/Scale Example/Scale_Example.xlsx')
x=data["X"]
y=data["Y"]
pl.plot(x,y,'o')

lowess1=pd.DataFrame(sm.nonparametric.lowess(y, x, frac=0.8,it=1,delta=0))
y1=lowess1.iloc[:,1]
x1=lowess1.iloc[:,0]

f1 = plt.figure(1)  
line1= plt.scatter(x, y,label='raw', marker='.')  
line2= plt.plot(x1,y1)
plt.legend([line1, line2], ["Line 1", "Line 2"], loc=1)
plt.show()

data_1.to_csv("D:/GitHub/applied_logistic_regression/1.csv")

sss=sns.lmplot("X","Y", data, lowess=True,)


data = pd.read_table("http://data.princeton.edu/eco572/datasets/cohhpop.dat",sep='       ',header=None)
y=data.iloc[:,1]
x=data.iloc[:,0]

lowess1=pd.DataFrame(sm.nonparametric.lowess(y, x, frac=0.15,it=0,delta=0))
y1=lowess1.iloc[:,1]
x1=lowess1.iloc[:,0]

f1 = plt.figure(1)  
line1= plt.scatter(x, y,label='raw', marker='.')  
line2= plt.plot(x1,y1)
plt.legend([line1, line2], ["Line 1", "Line 2"], loc=1)
plt.show()