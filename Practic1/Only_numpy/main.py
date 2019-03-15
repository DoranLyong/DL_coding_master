#!/usr/bin/python
# -*- coding: utf-8 -*- 

import numpy as np 
from dlutile import *


def Dataset():
    X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    Y = 10*X + 10
    return X, Y


def main():
    
    # Load D___
    X, Y = Dataset() 

        # mini_batch 
    (x_train, y_train), (x_test, y_test) = (X[:4], Y[:4]), (X[4:], Y[4:]) 
    print("train_shape: ", x_train.shape)
    print("test_shape: ", x_test.shape, "\n")
    


    # D_____ the network 



    
    print("Well done!!!")



if __name__ == "__main__":
    main() 