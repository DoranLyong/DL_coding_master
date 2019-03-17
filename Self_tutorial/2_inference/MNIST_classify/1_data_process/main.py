#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os, sys
sys.path.append(os.pardir)    # 부모 디렉토리의 파일 가져올 수 있게 설정 
import numpy as np 
from Dataprocess import load_mnist



def main():
    # Load data 
    (x_train, t_train), (x_test, t_test) = load_mnist( flatten=True,normalize=False)


    # data shape 
    print("x_train.shape: ",x_train.shape)
    print("t_train.shape: ",t_train.shape)
    print("x_test.shape: ", x_test.shape)
    print("t_test.shape: ", t_test.shape)

if __name__ == '__main__':
    main()