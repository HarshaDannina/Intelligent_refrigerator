# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 10:17:16 2018

@author: HARSHA
"""
#importing libraries
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import recall_score, precision_score

#defining Machine Learning Classifier

def MachineLearning_model(ldr_value):

    #reading sensor data
    dataset = pd.read_csv("sensorvalues.csv")
    
    #Converting door state from strings to binary labels.
    from sklearn.preprocessing import LabelBinarizer
    state_lb = LabelBinarizer()
    Y = state_lb.fit_transform(dataset.state.values)
    
    #Convert features into matrix form
    FEATURES = dataset.columns[0]
    X_data = dataset[FEATURES].as_matrix()
    X_data = X_data.reshape(-1,1)
    #X_data = normalize(X_data)
    
    #Splitting training and testing data
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X_data, Y, test_size=0.3, random_state=1)
    
    
    #Defining the Decision tree classifier
    
    clf = DecisionTreeClassifier()
    
    #Training the classifier
    clf.fit(X_train,y_train)
    
    #Testing the Classifier
    accuracy = clf.score(X_test, y_test)
    print(accuracy)
    pred = clf.predict(X_test)
    precision = precision_score(y_test, pred, average="weighted")
    recall = recall_score(y_test, pred, average="weighted")
    print ("Precision:", precision) 
    print ("Recall:", recall)
    
    
    #Predicting the door state from LDR value
    state = clf.predict(ldr_value)
    
    #Returning door state in binary form to capstone-project.py
    return state

#ldr_value = 900
#state = MachineLearning_model(ldr_value)
#print(state)

