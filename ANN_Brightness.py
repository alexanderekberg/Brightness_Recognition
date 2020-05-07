#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:44:18 2020

@author: alex
"""




class AI:
    
    
    def training(dataset, save_folder, save_name):
        import tensorflow as tf
        import numpy as np
        training_dataset = np.load(dataset)
        X = training_dataset[:, 0:17]
        y = training_dataset[:, 17:19]
        
        column_count = y.shape[0]
        for i in range (column_count):
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


        from keras.models import Sequential
        from keras.layers import Dense

        model = Sequential()

        model.add(Dense(activation="relu", input_dim=17, units=21, kernel_initializer="uniform"))

        model.add(Dense(activation="relu", units=10, kernel_initializer="uniform"))

        model.add(Dense(activation="softmax", units=4, kernel_initializer="uniform"))

        model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

        model.fit(X, y, batch_size = 10, nb_epoch = 1000)
        
        model.save(save_folder + save_name)
        
        return
    
    
    
    
   
    def evaluating(model, dataset, save_location, name):
        import numpy as np
        import tensorflow as tf
        
        model = '/Users/alex/desktop/model/model.h5'
        dataset = '/Users/alex/desktop/dataset/evaluating_dataset(hasValue).npy'
        save_location = '/Users/alex/desktop/model_evaluation/'
        name = 'model_accuracy'
        
        model = tf.keras.models.load_model(model)
        testing_dataset = np.load(dataset)
        
        x = testing_dataset[:, 0:17]
        y = testing_dataset[:, 17:19]
        
        column_count = y.shape[0]
        for i in range (column_count):
            if y[i] == 400:
                y[i] = 4
            elif y[i] == 300:
                y[i] = 3
            elif y[i] == 200:
                y[i] = 2
            elif y[i] == 100:
                y[i] = 1
        
        
        y_pred = model.predict(x)



        # predicted values
        predicted_values = np.argmax(y_pred, axis = 1)
        count = y_pred.shape[0]

        for index in range(count):
            if predicted_values[index] == 0:
                predicted_values[index] = 1
            elif predicted_values[index] == 1:
                predicted_values[index] = 2
            elif predicted_values[index] == 2:
                predicted_values[index] = 3
            elif predicted_values[index] == 3:
                predicted_values[index] = 4

        # real values
        real_values = y[:,0]
        
        # number of accurate numbers
        model_value = np.subtract(predicted_values, real_values)
        model_value = (model_value == 0).sum()
        
        # Answer in percent
        answer = model_value / column_count
        answer = answer * 100
        answer = str(int(answer))
        answer = answer + '% acc'

        np.save(save_location + name, answer)
        return
    
    
    
    def model(model, dataset, savefolder):
        import tensorflow as tf
        import numpy as np
        
        model = tf.keras.models.load_model(model)
        dataset = np.load(dataset)
        
        x = dataset[:, 0:17]
        x = np.array(x, dtype=np.float64)
        y = dataset[:, 17:19]
        
        y_pred = model.predict(x)
        predicted_values = np.argmax(y_pred, axis = 1)
        
        
        count = y_pred.shape[0]
        for index in range(count):
            if predicted_values[index] == 0:
                predicted_values[index] = 100
            elif predicted_values[index] == 1:
                predicted_values[index] = 200
            elif predicted_values[index] == 2:
                predicted_values[index] = 300
            elif predicted_values[index] == 3:
                predicted_values[index] = 400
        
        
        predicted_values = np.asarray([predicted_values])
        predicted_values = predicted_values.swapaxes(0, 1)
        
        # addnames to predicted values
        final = np.concatenate((predicted_values, y), axis = 1)
        np.save(savefolder, final)
        return



# Make the model with (hasValue) dataset
AI.training('/Users/alex/desktop/dataset/training_dataset(hasValue).npy', '/Users/alex/desktop/model/', 'model.h5')


# evaluate model with another (hasValue) dataset
AI.evaluating('/Users/alex/desktop/model/model.h5', '/Users/alex/desktop/dataset/evaluating_dataset(hasValue).npy', '/Users/alex/desktop/model_evaluation/', 'model_accuracy')


# Use model on (noValue) dataset
AI.model('/Users/alex/desktop/model/model.h5', '/Users/alex/desktop/dataset/real_dataset(noValue).npy', '/Users/alex/desktop/model_evaluation/' + 'values')











