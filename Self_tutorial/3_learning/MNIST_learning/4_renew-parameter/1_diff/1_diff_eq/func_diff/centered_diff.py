#!/usr/bin/python
# -*- coding: utf-8 -*- 

import numpy as np 
import matplotlib.pylab as plt 


def function(x):
    return 0.01 * x **2 + 0.1 * x

def tangent_line(f, x, numerical=True):       # f는 예시 함수 f(x)
    if numerical == True:
        d        =  numerical_diff(f, x)      # 점 x에서의 미분값 
        print("수치해석 미분계수 = ", d)

    y_intercept  =  f(x) - d*x
    return lambda t : d*t + y_intercept      # g(x) = f'(5)x + y절편


# 중앙 차분 
def numerical_diff(f, x): 
    #dt = 10e-50  # 조낸 작은 수 0.000000000000....1
    dt = 1e-4
    return (f(x + dt) - f(x-dt)) / (2*dt) 



""" 정의역 (domain) """
x = np.arange(0.0, 20.0, 0.1)    # [0.0, 20.0] in 0.1 step
print(x.shape)

""" 치역 (range, =target set) """ 
y = function(x)
print(y.shape)


""" 수치 미분 (numerical diff)"""
xx = 10 
num_div = numerical_diff(function, xx)    # x=10에서의 수치 미분값 
print(num_div)


""" 미분 계수의 접선 구하기 """ 
num_tLine = tangent_line(function, xx, numerical=True)
t_y = num_tLine(x)


""" 그래프 """
plt.xlabel("x")
plt.ylabel("y")

plt.plot(x, y)
plt.plot(x, t_y, '--r')
plt.show()
