#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys, os 
sys.path.append(os.pardir)  # 부모 디렉토리 내의 모든 파일을 가져올 수 있도록 설정 
import numpy as np 
import pickle 
from Dataprocess import load_mnist
from dlutile.Activation import sigmoid, softmax 


def load_test_data():
    print("Load test data...")
    (x_train, t_train), (x_test, t_test) = \
                      load_mnist( flatten=True,normalize=False)
    return x_test, t_test       

def load_weight():  # ../1_data_process/load_data.py 참고 
    with open("sample_weight.pkl", "rb") as f:
        weight = pickle.load(f)
    return weight 


def classify(weight, x): 
    W1, W2, W3 = weight["W1"], weight["W2"], weight["W3"]
    B1, B2, B3 = weight["b1"], weight["b2"], weight["b3"]

    # intput -> hidden-layer1
    a1 = np.dot(x,W1) + B1
    z1 = sigmoid(a1)

    # hidden-layer1 -> hidden-layer2
    a2 = np.dot(z1, W2) + B2 
    z2 = sigmoid(a2)

    # hidden-layer2 -> output-layer 
    a3 = np.dot(z2, W3) + B3 
    y = softmax(a3)

    return y 


def main():
    # (1) Load ____ data 
    x_test, t_test = load_test_data()

    # (2) Load pretrained weights 
    weights = load_weight() 
    
    # (3) Inference
    accuracy_cnt = 0 
    for i in range(len(x_test)): 
        y = classify(weights, x_test[i])
        p = np.argmax(y) # 확률이 가장 높은 노드의 인덱스 획득 
        if p == t_test[i]:
            accuracy_cnt += 1   # 맞춘 개수 증가 

    # (4) Evaluate 
    print("Accuracy: {}".format( float(accuracy_cnt)/len(x_test) ))


if __name__ == "__main__":
    main()