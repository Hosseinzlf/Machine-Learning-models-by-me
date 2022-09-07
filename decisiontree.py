#Hossein Zolfaghari
#Sep 2022

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('age_height.csv')
x = df.iloc[:, 0:1].values
y = df.iloc[:,-1].values

#Training the model
from sklearn.tree import DecisionTreeRegressor
DTR = DecisionTreeRegressor()
learned_model = DTR.fit(x,y)

#Visualization
plt.scatter(x,y, color = 'b')
plt.plot(x,DTR.predict(x), color = 'r')
plt.show()