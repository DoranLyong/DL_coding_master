#!/usr/bin/python
# -*- coding: utf-8 -*- 


import numpy as np 
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d    # 3D plotting


def function(x):  
    if x.ndim == 1: 
        return np.sum(x**2)      # f(x0, x1) = x0**2 + x1**2

    else: 
        return np.sum(x**2, axis=1)
        

def numerical_gradient( f, x ):
    h = 1e-4    # 0.0001 
    grad = np.zeros_like(x)      # x와 형상이 같은 zero-배열을 생성 

    for idx in range(x.size):
        tmp_val = x[idx]

        """ f(x+h) 계산 """
        x[idx] = tmp_val + h 
        fxh1 = f(x)

        """ f(x-h) 계산 """ 
        x[idx] = tmp_val - h 
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)

        x[idx] = tmp_val  # 값 복원  

    return grad



def main(): 
    print(numerical_gradient(function, np.array([3.0, 4.0])))
    print(numerical_gradient(function, np.array([0.0, 2.0])))
    print(numerical_gradient(function, np.array([3.0, 0.0])))

    print("Done!")



if __name__ == "__main__":
    main()