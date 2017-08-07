# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 21:13:23 2017

@author: Raymond
"""
import csv
import pandas as pd
import numpy as np
import os 

data=pd.read_csv("C:/Users/Raymond/Desktop/a.csv",
                 encoding='utf-8',index_col=False,engine='python',header=None,doublequote=True,skiprows=[0])


skiprows=[0],
         encoding='utf-8',index_col=False,engine='python',sep=",",
                 header=0,quotechar='"',doublequote=True,quoting=csv.QUOTE_NONE
                 
                 
data=pd.read_csv("C:/Users/Raymond/Desktop/查询记录汇总.csv",
                 encoding='utf-8',index_col=None,engine='python',sep=",",header=0)              


data=pd.read_csv("C:/Users/Raymond/Desktop/查询记录汇总.csv",
                 encoding='utf-8',index_col=None,engine='python',quotechar='"',header=0,doublequote=True)  