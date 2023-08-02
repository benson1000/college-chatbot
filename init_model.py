import tensorflow as tf #It is used for building and training deep learning models. 
import tflearn  #TFlearn is a modular and transparent deep learning library built on top of Tensorflow. It provides a higher level API to tensorflow for facilitating and showing up new experiments
from tensorflow.python.framework import ops  #defines the fundamental building blocks of TensorFlow operations and computational graphs. It is responsible for defining and managing the nodes and edges in the computational graph


#Defining the Deep Learning model structure.

def init_model(X_train,y_train,X_test,y_test):       
    
    ops.reset_default_graph()  #It is used to reset the default graph.                                                     
    net = tflearn.input_data(shape=[None, len(X_train[0])])    #input layer ,the size of the layer is the same size as x training data list
    net = tflearn.fully_connected(net, 850, activation='relu')                 # two hidden layers  each one is made up of 850 neurons
    net = tflearn.fully_connected(net, 850,activation='relu')
    net = tflearn.fully_connected(net, len(y_train[0]), activation = "softmax")   #output layer according to the length of the y train list
    net = tflearn.regression(net)
    model = tflearn.DNN(net)
    
    import os
    if os.path.exists("model.tflearn.meta"):     #if the model already exists ;load this model 
        model.load("model.tflearn")
    else: #else start training from the first
        #training our dataset, setting the number of epochs to 20, setting the batchsize to 10
        model.fit(X_train, y_train,validation_set=(X_test,y_test), n_epoch=20, batch_size=8, show_metric=True)  
        #save our model                                                                                                  
        model.save("model.tflearn")                                                                              
    return model
