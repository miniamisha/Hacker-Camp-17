#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 03:07:56 2017

@author: amisha
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
sc_y=StandardScaler()
X=sc_X.fit_transform(X)
y=sc_y.fit_transform(y)

dataset=pd.read_csv('/home/amisha/Downloads/Book1.csv')
X=dataset.iloc[:,:-4].values
y=dataset.iloc[:,4].values


y_pred=regressor.predict(1from sklearn.svm import SVR
regressor=SVR(kernel ='rbf')
regressor.fit(X,y)


plt.scatter(X,y,color='red')
plt.plot(X,regressor.predict(X),color='blue')
plt.title('Months vs No. of visits ')
plt.xlabel('Months')
plt.ylabel('No. of visit')
plt.show()







