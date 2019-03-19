#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys, os 
sys.path.append(os.pardir)  # 부모 디렉토리 내의 모든 파일을 가져올 수 있도록 설정 
import numpy as np 
import pickle 
from Dataprocess import load_mnist
from dlutile.Activation import sigmoid, softmax, softmax2


def load_test_data():
    print("Load test data...")
    (x_train, t_train), (x_test, t_test) = \
                     load_mnist( normalize=False, flatten=True)

    
    return x_test, t_test   

def load_normal_data():
    print("Load test data...")  
    (x_train, t_train), (x_test, t_test) = \
             load_mnist(normalize=True, flatten=True, one_hot_label=False) 
    return x_test, t_test     


def load_weight():  # ../1_data_process/load_data.py 참고 
    with open("sample_weight.pkl", 'rb') as f:
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
    y = softmax2(a3)

    return y 


def main():
    # (1) Load ____ data 
    #x_test, t_test = load_test_data()     # unnormalized data 
    nx_test, nt_test = load_normal_data() # normalized data

    # (2) Load pretrained weights 
    weights = load_weight() 
    
    # (3) Inference
    batch_size = 100 
    #accuracy_cnt1 = 0 
    accuracy_cnt2 = 0 

    for i in range(0, len(nx_test), batch_size):
        # batch_process 
        x_batch = nx_test[i : i+batch_size]
    
        #y  = classify(weights, x_test[i])
        y_batch = classify(weights, x_batch)  # to normalized data 

        p = np.argmax(y_batch, axis=1) # 확률이 가장 높은 노드의 인덱스 획득 
        #q = np.argmax(ny) 
        
        accuracy_cnt2 += np.sum( p == nt_test[i:i+batch_size] )

    # (4) Evaluate 
    print("Accuracy to normalized: {}".format(float(accuracy_cnt2)/len(nx_test))    )


if __name__ == "__main__":
    main()