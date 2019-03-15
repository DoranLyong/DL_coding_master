#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""
Modification of https://github.com/jskDr/keraspp/blob/master/ex1_1_simple_exercise.py
"""
from keras import models, layers 
import numpy as np 


def Dataset():
    X = np.array([0,1,2,3,4,5,6,7,8,9])
    Y = 10*X + 10      
    return X, Y      

def Evaluate(model):    
    print("Target_label: ", Y[4:])
    print("Predictions: ", model.predict(X[4:]).flatten())
    print("\n", "Evalutaion done!")


def main():
    # Load D___
    global X, Y
    X, Y = Dataset() # (input, output)      

    # D_____ network 
    model = models.Sequential()  # 함수형 FP
    model.add( layers.Dense(1, input_shape=(1,)))

    # C______ the network 
    model.compile( loss="mse", optimizer='SGD')

    # T____ it 
    model.fit( X[:4], Y[:4], epochs = 1000, verbose=1 )  

    print("Well_Done!")
    
    # E_______
    Evaluate(model)


if __name__ == "__main__":
    main()





