#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:44:05 2023

@author: maharsh
"""
import pandas as pd
import numpy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


ecom_exp_maharsh=pd.read_csv(r'Ecom Expense.csv')

print(ecom_exp_maharsh.head(3))
print("_________________________________________________________________\n")
print(ecom_exp_maharsh.shape)
print("_________________________________________________________________\n")
print(ecom_exp_maharsh.columns.values)
print("_________________________________________________________________\n")
print(ecom_exp_maharsh.info())
print("_________________________________________________________________\n")
print("Total null values per columns:")
print(ecom_exp_maharsh.isnull().sum())
print("_________________________________________________________________\n")

print("Tranforming catagorical to numeric")
new=pd.get_dummies(ecom_exp_maharsh,columns=["Gender","City Tier"],drop_first=False)

print(new.shape,new.info(),new.columns.values)
print("_________________________________________________________________\n")
print("Dropping unwanted columns")
new=new.drop(columns=["Transaction ID"])

print(new.shape,new.info(),new.columns.values)
print("_________________________________________________________________\n")

print("Normalizing data")
def normalize(data):
    return (data-data.min())/(data.max()-data.min())

normal_data=normalize(new.astype(numpy.float32))
print (normal_data)
print(normal_data.head(2))
print("_________________________________________________________________\n")

print("generating Histogram")
hist=normal_data.hist(figsize=(9,10))
print("_________________________________________________________________\n")
print("generating Scatter matrix")
pd.plotting.scatter_matrix(normal_data, alpha=.4,figsize=(20,25))
print("_________________________________________________________________\n")

print("Feature selection")
feature_cols = ['Monthly Income', 'Transaction Time', 'Gender_Female', 'Gender_Male', 'City Tier_Tier 1', 'City Tier_Tier 2', 'City Tier_Tier 3']

X=normal_data[feature_cols]
Y=normal_data['Total Spend']

print(X.head(),X.info(),X.shape)
print(Y.head(),Y.info(),Y.shape)
print("_________________________________________________________________\n")
print("spliting data in train and test data. Bulding model out out the selected data")
x_train_maharsh,x_test_maharsh,y_train_maharsh,y_test_maharsh= train_test_split(X, Y, test_size=0.35)
print(x_train_maharsh,x_test_maharsh,y_train_maharsh,y_test_maharsh)

lin_reg = LinearRegression()

lin_reg.fit(x_train_maharsh,y_train_maharsh)

print(lin_reg.coef_)
print(lin_reg.intercept_)

print("_________________________________________________________________\n")
print("R squared value for 1st model")
r_squared = lin_reg.score(x_train_maharsh, y_train_maharsh)
print(r_squared)




print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("Added 'record' column in feature selectin.\nspliting data in train and test data.\nBulding new model out out the selected data")

feature_cols = ['Monthly Income', 'Transaction Time', 'Record', 'Gender_Female', 'Gender_Male', 'City Tier_Tier 1', 'City Tier_Tier 2', 'City Tier_Tier 3']

X=normal_data[feature_cols]
Y=normal_data['Total Spend']

print(X.head(),X.info(),X.shape)
print(Y.head(),Y.info(),Y.shape)

x_train_maharsh,x_test_maharsh,y_train_maharsh,y_test_maharsh= train_test_split(X, Y, test_size=0.35)

print(x_train_maharsh,x_test_maharsh,y_train_maharsh,y_test_maharsh)

lin_reg = LinearRegression()

lin_reg.fit(x_train_maharsh,y_train_maharsh)

print(lin_reg.coef_)

print(lin_reg.intercept_)

print("_________________________________________________________________\n")
print("R squared value for 2nd model")
r_squared = lin_reg.score(x_train_maharsh, y_train_maharsh)
print(r_squared)















