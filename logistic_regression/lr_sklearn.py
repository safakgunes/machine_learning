# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 10:29:11 2021

@author: SAFAK
"""

import numpy as np

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("data.csv")

M=data[data.diagnosis=="M"]
B=data[data.diagnosis=="B"]
plt.scatter(M.radius_mean,M.texture_mean,color='r')
plt.scatter(B.radius_mean,B.texture_mean,color='c')
plt.xlabel("radius mean")
plt.ylabel("texture mean")
plt.show()
data=data.drop(columns=["id","Unnamed: 32"])
data.diagnosis=[1 if each == "M" else 0 for each in data.diagnosis]
y_data=data.diagnosis.values
x_data=data.drop(columns="diagnosis")

x_data = ((x_data-np.min(x_data))/(np.max(x_data)-np.min(x_data)))

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_data,y_data,test_size=(0.2),random_state=(42))

x_train=x_train.T
y_train=y_train.T
x_test=x_test.T
y_test=y_test.T


from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(x_train.T,y_train.T)
prediction=lr.predict(x_test.T)
print("test accuracy {}".format(lr.score(x_test.T,y_test.T)))