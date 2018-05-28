import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
data = pd.read_csv('dataset.csv')

x = np.array(data[['Time', 'Temp']])
y = np.array(data[['State']]).ravel()

knn.fit(x,y)

time = raw_input("Enter time")
temp = raw_input("Enter temp")

data =. []

data.append(float(time))
data.append(float(temp))

a = knn.predict([data])

print(a[0])}