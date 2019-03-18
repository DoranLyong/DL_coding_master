#!/usr/bin/python
# -*- coding: utf-8 -*- 

import numpy as np 

def step_function(x): # p.69
    return np.array( x>0, dtype=np.int)

def identity(x):  # p.88, p.91
    return x

def sigmoid(x):   # p.72 
    return 1 / (1 + np.exp(-x))

def relu(x):    # p.77
    return np.maximum(0, x)    

def softmax(a): # p.93
    c = np.max(a)
    exp_a     = np.exp( a - c ) # constrain overflow 
    sum_exp_a = np.sum(exp_a) 
    y = exp_a / sum_exp_a
    return y 


    