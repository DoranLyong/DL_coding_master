#!/usr/bin/python
# -*- coding: utf-8 -*- 

import numpy as np 

def mse(y, t):   # p.113
    return 0.5 * np.sum((y-t)**2)

def cross_entropy_error(y, t): # p.115, 118
    
    delta = 1e-7

    if y.ndim == 1:   # batch_size = 1 
        t = t.reshape(1, t.size) # 1행  t.size 열 
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
           
    return -np.sum( t * np.log(y + delta)) / batch_size




