#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 01:16:32 2017

@author: amisha
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import data set
dataset=pd.read_csv('/home/amisha/Desktop/doc.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,y)

from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=2)
X_poly=poly_reg.fit_transform(X)
poly_reg.fit(X_poly,y)
lin_reg_2=LinearRegression()
lin_reg_2.fit(X_poly,y)

plt.scatter(X,y,color='red')
plt.plot(X,LinearRegression.Predict(X),color='blue')
plt.title('age vs mortality (Polynomial Regression)')
plt.xlabel('age')
plt.ylabel('mortality')
plt.show()
