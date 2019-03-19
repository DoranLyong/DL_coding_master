#!/usr/bin/python
# -*- coding: utf-8 -*- 

import numpy as np 

def mse(y, t):   # p.113
    return 0.5 * np.sum((y-t)**2)

def cross_entropy_error(y, t): # p.115
    delta 1e-7
    return -np.sum( t * np.log( y + delta ))    


