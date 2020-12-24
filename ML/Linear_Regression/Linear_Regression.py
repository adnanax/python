#!/usr/bin/env python
# coding: utf-8

# # Linear Regression with Single Variable

# Importing the necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# Creating a dataframe
df = pd.read_csv('E:\\DataSets\\homeprices.csv')
df

#Plotting the dataset
get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel ('Area (Sqr Feet)')
plt.ylabel ('Price (US$)')
plt.title('Home Prices')
plt.scatter(df.area,df.price, color='red', marker='+')


# Plotting the prediction price line
get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel ('Area (Sqr Feet)')
plt.ylabel ('Price (US$)')
plt.title('Home Prices')
plt.scatter(df.area,df.price, color='red', marker='+')
plt.plot(df.area,reg.predict(df[['area']]), color='blue')# plot the predicted price line


# Applying the Linear Regression model on the dataset

reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)

#Predicting the Price
reg.predict([[3300]])


# Checking the coefficient and intercept of the line
reg.coef_

reg.intercept_

# y = mx + c
135.78767123 * 3300+ 180616.43835616432


# Predicting the Price
reg.predict([[5000]])


# Loading area file to the datagram
d = pd.read_csv('E:\\DataSets\\areas.csv')
d.head()


#Predicting the prices and writing to the file
p= reg.predict(d)
d['prices'] = p
d.to_csv('E:\\DataSets\\prediction.csv',index=False)

