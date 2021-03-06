[(back)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning)

# 데이터를 취급할 때 주의할 점 
학습에 필요한 데이터를 어떻게 관리하고 주의할 점은 무엇인지 정리해보자. 

<br/>

## 1. Data split 
### (1) 준비된 데이터를 다음과 같이 3개로 쪼갠다 
* training set<sup>훈련 집합</sup>, validation set<sup>검증 집합</sup>, testing set<sup>시험 집합
    * 훈련 데이터: 모델을 학습시켜 최적의 가중치 매개변수를 찾을 때 사용 <br/>

    * 검증 데이터: 학습된 모델의 성능 평가 
        > train acurracy와 validation accuracy가 비슷하다 ⇒ overfitting이 적다 <br/>
        
    * 시험 집합: unseen 데이터를 통해 모델의 성능 평가 

        > <img src="dataset.png" width=400>

### (2) 왜 쪼개나? 
* 범용화된(=일반화된) 모델을 찾기 위함 
    > <span style="color:skyblue">벙용 능력</span>: 아직 보지 못한 데이터(unseen data)로도 문제를 올바르게 풀어내는 능력 

<br/>

## 2. 주의할 점 
과적합(overfitting, 오버피팅)을 피할 수 있도록 데이터 셋을 구성하라 
* overfitting : 한 data-set에만 지나치게 최적화된 상태 
    > 한쪽 이야기(특정 데이터셋)만 너무 많이 들어서 편견이 생겨버린 상태 


오버피팅을 피하기 위한 노하우를 찾아보자 