# -*- coding: utf-8 -*-
"""
Lei

Ch4 Model-Building Strategies and Methods for Logistic Regression
"""
#import the package we need
#read the data sets described in Section 1.6 the Burn Study
import pandas as pd
import numpy as np
import statsmodels.api as sm

#4.2.1 Methods to Examine the Scale of a Continuous Covariate in the Logit

##read the raw data
data=pd.read_excel("D:/GitHub/applied_logistic_regression/data/Scale Example/Scale_Example.xlsx")

