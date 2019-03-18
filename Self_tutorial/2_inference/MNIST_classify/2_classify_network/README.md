[ (back) ](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/2_inference/MNIST_classify)

# 신경망의 추론 처리 
p. 100 <br/>

사전 학습된(pretrained) 신경망 모델을 통해 Machine Learning의 ['추론' 작업](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/2_inference)이 어떻게 수행 되는지를 이해한다. 
> MNIST 데이터셋에 대한 숫자 분류기(classifier) 구현  

<br/><br/>

## 샘플 신경망 모델 
* 구성 
    * 입력층 뉴런 : 784개 
        > image_size = 28x28  → flatten( ) → 784 
    * 1층 은닉층 뉴런 : 50개 
    * 2층 은닉층 뉴런 : 100개 
    * 출력층 뉴런: 10개 
        > 분류할 숫자 클래스가 0~9 까지 총 10가지 이므로 

<br/>

## 추론 단계 구현 
(1) [MNIST 데이터 불러오기](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/2_inference/MNIST_classify/1_data_process) <br/>
* normalized 된 데이터와 아닌 데이터에 대한 성능평가 실행 
    > normalized 했을 때 성능이 더 좋게 평가됨 ★★★★★ <br/>

(2) '학습된 가중치 매개변수' 불러오기 
* ./sample_weight.pkl <br/>
    > ※ [(pickle)](https://blog.naver.com/cheeryun/221378069487) <br/>

(3) '추론' 단계 구현 
* 숫자 분류 문제 ⇒ classifier 구현 <br/>

(4) 성능 평가 
* auccuracy 계산 
    > Accuracy<sub>(정확도)</sub> : 타켓<sub>target</sub>을 정확히 맞춘 비율 


```python 
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
    x_test, t_test = load_test_data()     # unnormalized data 
    nx_test, nt_test = load_normal_data() # normalized data

    # (2) Load pretrained weights 
    weights = load_weight() 
    
    # (3) Inference
    accuracy_cnt1 = 0 
    accuracy_cnt2 = 0 

    for i in range(len(x_test)): 
        y  = classify(weights, x_test[i])
        ny = classify(weights, nx_test[i])  # to normalized data 

        p = np.argmax(y) # 확률이 가장 높은 노드의 인덱스 획득 
        q = np.argmax(ny) 

        if p == t_test[i]:
            accuracy_cnt1 += 1   # 맞춘 개수 증가 

        if q == nt_test[i]:
            accuracy_cnt2 += 1 


    # (4) Evaluate 
    print("Accuracy to unnormalized: {}".format( float(accuracy_cnt1)/len(x_test) )) 
    print("Accuracy to normalized: {}".format(float(accuracy_cnt2)/len(nx_test))    )


if __name__ == "__main__":
    main()
```
```
Accuracy to unnormalized: 0.9207

Accuracy to normalized: 0.9352
```

## 데이터를 정규화<sub>normalization</sub> 했을 때 성능이 더욱 좋다!
※ [데이터 전처리(pre-processing)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/2_inference/MNIST_classify/1_data_process/data_preprocess)