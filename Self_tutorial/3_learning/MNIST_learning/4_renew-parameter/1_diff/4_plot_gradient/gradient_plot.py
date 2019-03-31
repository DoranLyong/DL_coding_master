#!/usr/bin/python
# -*- coding: utf-8 -*- 


import numpy as np 
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d    # 3D plotting


def function(x):  # 2변수 함수 값 출력 
    if x.ndim == 1:
        return np.sum(x**2)   # f(x0, x1) = x0**2 + x1**2  

    else:
        return np.sum(x**2, axis=1)



def _numerical_gradient_no_batch( f, x ):
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

def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)
        
        return grad

def plot(X0_flat, X1_flat, grad):
    plt.figure()
    plt.quiver(X0_flat, X1_flat, -grad[0], -grad[1],  angles="xy",color="#666666")#,headwidth=10,scale=40,color="#444444")
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.xlabel('x0')
    plt.ylabel('x1')
    plt.grid()
    plt.legend()
    plt.draw()
    plt.show()


def main():

    """ 정의역 (domain) """ 
    x0 = np.arange(-2, 2.5, 0.25)
    x1 = np.arange(-2, 2.5, 0.25) 
    X0, X1 = np.meshgrid(x0, x1)  
    print(X0.shape)      

    # 평활화 
    X0_flat = X0.flatten() 
    X1_flat = X1.flatten()


    """ 기울기 (gradient) """ 
    grad = numerical_gradient(function, np.array([X0_flat, X1_flat]) )
    print(np.array([X0_flat, X1_flat]).shape)


    """ 플로팅 """ 
    plot(X0_flat, X1_flat, grad ) 

    print("Done!")

if __name__ == "__main__":
    main()