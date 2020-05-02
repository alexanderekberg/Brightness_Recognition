#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:44:18 2020

@author: alex
"""







# Importing the libraries
import tensorflow as tf
import numpy as np


# saved

dataset = np.load('/Users/alex/desktop/ANN_dataset_for_brightness.npy')
X = dataset[:, 0:17]
y = dataset[:, 17:19]

for i in range (27):
    if y[i] == 400:
        y[i] = 4
    elif y[i] == 300:
        y[i] = 3
    elif y[i] == 200:
        y[i] = 2
    elif y[i] == 100:
        y[i] = 1
    


y = tf.keras.utils.to_categorical(y, num_classes=None, dtype='float64')
y = y[:,1:5]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)




from keras.models import Sequential
from keras.layers import Dense

# Training on train set
classifier = Sequential()

classifier.add(Dense(activation="relu", input_dim=17, units=21, kernel_initializer="uniform"))

classifier.add(Dense(activation="relu", units=10, kernel_initializer="uniform"))

classifier.add(Dense(activation="softmax", units=4, kernel_initializer="uniform"))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

classifier.fit(X_train, y_train, batch_size = 21, nb_epoch = 2000)



# Testing on test set
y_pred = classifier.predict(X_test)










# make back to original values "1, 2" etc

# predicted set
indexOfMaximumValue = np.argmax(y_pred, axis = 1)
count = y_pred.shape[0]


for index in range(count):
    if indexOfMaximumValue[index] == 0:
        indexOfMaximumValue[index] = 1
    elif indexOfMaximumValue[index] == 1:
        indexOfMaximumValue[index] = 2
    elif indexOfMaximumValue[index] == 2:
        indexOfMaximumValue[index] = 3
    elif indexOfMaximumValue[index] == 3:
        indexOfMaximumValue[index] = 4


# test set
indexOfMaximumValue2 = np.argmax(y_test, axis = 1)

for index2 in range(count):
    if indexOfMaximumValue2[index2] == 0:
        indexOfMaximumValue2[index2] = 1
    elif indexOfMaximumValue2[index2] == 1:
        indexOfMaximumValue2[index2] = 2
    elif indexOfMaximumValue2[index2] == 2:
        indexOfMaximumValue2[index2] = 3
    elif indexOfMaximumValue2[index2] == 3:
        indexOfMaximumValue2[index2] = 4







# Evaluating the model
# from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(indexOfMaximumValue, indexOfMaximumValue2)