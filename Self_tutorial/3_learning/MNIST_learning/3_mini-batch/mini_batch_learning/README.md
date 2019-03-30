[(back)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/3_mini-batch)

# 미니 배치 학습법(mini-batch learning) 
※ p.116

통계 조사에서 전국민을 대상으로한 전수 조사는 비용이 많이듬. 
* 그래서 <span style="color:orange"><b>모집단</b></span>을 추려서 근사치로 전체를 파악함 

<br/>

미니배치 학습도 이와 같음 

<br/>

batch size가 너무 커서 전수 조사하기 힘듬 
* mini-batch로 <span style="color:orange"><b>모집단</b></span>을 추려서 손실 함수를 구함 

<br/>

### <b>__ EXAMPLE __</b> 60,000장의 훈련 데이터가 살고 있음 
* 100장을 무작위로 뽑아 
* 뽑힌 100장에 대해서만 모델을 학습함 
* 손실 함수가 최소가 될 때까지 매개변수를 갱신하며 반복 

<br/>

## <img src="5_how_to_do.png" width=35> 구현 
* 훈련 데이터 집합에서 무작위로 뽑는 코드가 필요함 
    * ```np.random.choice( <숫자 범위>, <뽑을 개수> )```
* [MNIST 데이터 전처리](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/2_inference/MNIST_classify/1_data_process)
    * 정규화 & 인코딩 

```python 
 #!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys, os 
sys.path.append(os.pardir)           # 부모 디렉토리 경로를 sys.path에 추가 (p.98)
import numpy as np
from dataset.mnist import load_mnist  # MNIST 데이터를 Numpy 객체로 불러오기 



def miniBatch(x_train, t_train, batchSize):
    print("[INFO] mini-batch selection...")

    train_size = x_train.shape[0]  # 전체 데이터 개수(= 전체 batch)
    batch_mask = np.random.choice(train_size, batchSize) # 0~59999 숫자 중 임의로 batchSize 만큼 고름 

    x_batch = x_train[batch_mask]  # 뽑힌 숫자를 index로 사용 
    t_batch = t_train[batch_mask]

    return x_batch, t_batch



def main():
    (x_train, t_train), (x_test, t_test) = load_mnist( normalize=True, one_hot_label=True)
    print(x_train.shape)    # (60000, 784) = (데이터 개수, 평활화된 이미지 배열 28x28 = 784)
    print(t_train.shape)    # (60000, 10) = (데이터 개수, 레이블 클래스 개수)


    minibatch_x, minibatch_t = miniBatch(x_train, t_train, batchSize = 100) 
    print(minibatch_x.shape)
    print(minibatch_t.shape)

if __name__ == "__main__":
    main()
```
```
>> (60000, 784)
(60000, 10)
[INFO] mini-batch selection...
(100, 784)
(100, 10)
```

<br/>

***

## [<b>NOTE</b>] 
텔레비전 시청률도 모든 세대의 텔레비전이 아니라 선택된 일부 가구의 텔레비전만을 대상으로 구함 <br/>

### EXAMPLE
* 경기도에서 무작위로 1,000가구 선정 
* 1,000가구를 대상으로 시청률 계측 
* 경기도 전체의 시청률로 근사 시킴 

1,000가구의 시청률이 전체 시청률과 정확히 일치하지는 않음, 
* 전체의 대략적인 값으로 사용할 수 있음 

<br/>

미니배치의 손실 함수도 일부 표본 데이터로 전체를 비슷하게 계측함 
* 즉, 전체 훈련 데이터의 대표로서 무작위로 선택한 작은 덩어리(mini-batch)를 사용함 