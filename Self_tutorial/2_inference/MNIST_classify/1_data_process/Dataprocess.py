#!/usr/bin/python
# -*- coding: utf-8 -*- 

import numpy as np 
import os.path
import gzip
import pickle
import os 

key_file = {
    'train_img':'train-images-idx3-ubyte.gz',
    'train_label':'train-labels-idx1-ubyte.gz',
    'test_img':'t10k-images-idx3-ubyte.gz',
    'test_label':'t10k-labels-idx1-ubyte.gz'
}

dataset_dir = os.path.dirname(os.path.abspath(__file__))
print("directory_path= ", dataset_dir)
save_file = dataset_dir + "/mnist.pkl"


def load_mnist(normalize=True, flatten=True, one_hot_label=False):

    """
    normalize : 이미지의 픽셀 값을 0 ~ 1 사이의 값으로 정규화할지 결정 

    one_hot_label : 원-핫 인코딩
        레이블을 원-핫(one-hot) 배열로 돌려줌. 
        * one-hot array = [0,0,1,0,0,0,0,0,0,0]처럼 한 원소만 1인 배열

    flatten : 입력 이미지를 1차원 배열로 평활화할지 결정 

    Returns
    -------
    (train_img, train_label), (test_img, test_label)
    """
    with open(save_file, 'rb') as f:
        dataset = pickle.load(f)

    if normalize: 
        for key in ('train_img', 'test_img'):
            dataset[key] = dataset[key].astype(np.float32)
            dataset[key] /=255.0 

    if one_hot_label:
        dataset['train_label'] = _change_one_hot_label(dataset['train_label'])
        dataset['test_label'] = _change_one_hot_label(dataset['test_label'])   

    if not flatten:
        for key in ('train_img', 'test_img'):
            dataset[key] = dataset[key].reshape(-1, 1, 28, 28)
    
    return (dataset['train_img'], dataset['train_label']), (dataset['test_img'], dataset['test_label'])


def _change_one_hot_label(X):
    T = np.zeros((X.size, 10))
    for idx, row in enumerate(T):
        row[X[idx]] = 1
        
    return T