# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 17:11:47 2022

@author: uarvi
"""

import numpy as np 
import pandas as pd 

data = pd.read_csv("Social_Network_Ads.csv")

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

              
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.30, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighboursClassifier(n_neighbors=3)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)
print(accuracy_score)

new_predict = print(classifier.predict(sc.transform([[30,87000]])))

import pickle

model_file = "classifier.pickle"

pickle.dump(classifier, open(model_file, 'wb'))

scaler_file = "sc.pickle"

pickle.dump(sc, open(scaler_file, 'wb'))


