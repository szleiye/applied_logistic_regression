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
import math

'''-------------------------------------------------------------------
4.2.1 Methods to Examine the Scale of a Contiuous Covariate in the Logit                                                                                       
--------------------------------------------------------------------'''

#read the data Scale_Example
#read the data sets CHDAGE
'Method 1'
    data = pd.read_excel('D:/GitHub/applied_logistic_regression/data/Scale Example/Scale_Example.xlsx')
    x=data["X"]
    y=data["Y"]
    pl.plot(x,y,'o')
    
    lowess1=pd.DataFrame(sm.nonparametric.lowess(y, x, frac=0.8,it=1,delta=0))
    y1=lowess1.iloc[:,1]
    x1=lowess1.iloc[:,0]
    lowess1['y2']=np.log(y1/(1-y1))
    y2=lowess1['y2']
    f1 = plt.figure(1)  
    line1= plt.scatter(x, y,label='raw', marker='.')  
    line2= plt.plot(x1,y1)
    line3= plt.plot(x1,y2)
    plt.legend([line1, line2, line3], ["Line 1", "Line 2", "Line 3"], loc=1)
    plt.show()

#data_1.to_csv("D:/GitHub/applied_logistic_regression/1.csv")

    sss=sns.lmplot("X","Y", data, lowess=True,)

#test-data： princeton cohhpop
#想比较PYTHON 跟 STATA 的lowess smoothing 有什么不一样
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

'Method 2'
    lowess1.loc[lowess1.iloc[:,0]<=32,'p1']=1
    lowess1.loc[lowess1.iloc[:,0]>32,'p1']=0
    lowess1.loc[(lowess1.iloc[:,0]>32) & (lowess1.iloc[:,0]<=44),'p2']=1        
                
'''-------------------------------------------------------------------
4.2.2 Examples of Purposeful Selection
--------------------------------------------------------------------'''
'Example 2'
#read the BURN1000 data
BURN1000 = pd.read_table('D:/GitHub/applied_logistic_regression/data/BURN/BURN1000.txt',header=0,encoding='gb2312',index_col='ID')

#show the data
print(BURN1000.head())

#fitting themodel containing all covariates
death=BURN1000['DEATH']
varX=BURN1000.drop(['DEATH'],1)

varX = sm.add_constant(varX)
varX.head()

logit = sm.Logit(death, varX)
result = logit.fit()
print(result.summary())