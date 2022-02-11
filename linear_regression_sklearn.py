#This code has been written by HosseinZLF for machine learning class exercies
#University of Paris/Saclay, Feb 2022,





#import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#import data
#you can use your own data by costumizing the x and y based on your needs
dataset=pd.read_csv("grades.csv")
#read the all except the last column as input to our linear regression model
x=dataset.iloc[:,0:-1].values 
 #read the last column as the output
y=dataset.iloc[:,-1].values



#split both x and y to train and test datas with the help of sklearn library
#use train_test_split and set the test_size = 0.2 to use 20 percentage of data
#for test our predicted modelat the final
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split (x, y, test_size=0.2, random_state=0)

#from sklearn library import linear regression 
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
#fit linear regression to x and y training datas
lr.fit(x_train, y_train)
#use predicted model to see that our model works good or not
y_pred=lr.predict(x_test)


#make a table for comparision predicted y and test y 
#and calculation of their differences.
df=pd.DataFrame()
df["y_actual"]=y_test
df["y_pred"]=y_pred
print(df)

#plot all figures
plt.scatter(x_train,y_train, color="b")
plt.plot(x_train,lr.predict(x_train), color="r")
plt.title("Linear Regression for Grades")
plt.xlabel("Days of Studies")
plt.ylabel("Grades")
plt.show()