# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 10:17:16 2018

@author: HARSHA
"""

import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import recall_score, precision_score


def MachineLearning_model(ldr_value):

    dataset = pd.read_csv("sensorvalues.csv")
    
    from sklearn.preprocessing import LabelBinarizer
    state_lb = LabelBinarizer()
    Y = state_lb.fit_transform(dataset.state.values)
    
    #from sklearn.preprocessing import normalize
    FEATURES = dataset.columns[0]
    X_data = dataset[FEATURES].as_matrix()
    X_data = X_data.reshape(-1,1)
    #X_data = normalize(X_data)
    
    
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X_data, Y, test_size=0.3, random_state=1)
    
    
    
    
    clf = DecisionTreeClassifier()
    
    
    clf.fit(X_train,y_train)
    accuracy = clf.score(X_test, y_test)
    print(accuracy)
    pred = clf.predict(X_test)
    precision = precision_score(y_test, pred, average="weighted")
    recall = recall_score(y_test, pred, average="weighted")
    print ("Precision:", precision) 
    print ("Recall:", recall)
    
    
    #fig = plot_decision_regions(X_data, Y, clf=clf, legend=2, X_highlight=X_test)
    #plt.show()
    
    
    state = clf.predict(ldr_value)
    return state
#ldr_value = 900
#state = MachineLearning_model(ldr_value)
#print(state)

