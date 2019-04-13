[(back)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/4_renew-parameter)
# 경사법(경사 하강법) - Gradient Descent 
### 최적 탐색 알고리즘 중 하나 

※ 최적 탐색 알고리즘이란? 
* 신경망의 최적 매개변수(weight, bias)를 찾게 도와주는 알고리즘 
* 최적(optimum): 
    * 신경망 & Machine Learning에서 최적이란? 
        > 손실 함수를 최소로 만드는<sup>(='나쁜 정도'가 최소일 때의)</sup> 매개변수 값  <br/>
        > ``` min Loss(W, B)```

<br/>

## 최적 매개변수를 찾는 과업의 문제점 
* 보통 신경망 모델은 매개변수가 많다 
* 그에 따라 손실 함수의 매개변수도 많다 
    * ```Loss(W, B)```
* 결국 매개변수 공간이 광대해진다... (차원의 저주)

    <img src ="./curse.png" width=400>

<br/>

## 사막에서 바늘 찾기  
이러한 광대한 차원에서 손실 함수의 기울기(gradient)를 잘 이용해 함수의 최솟값을 찾으려는 것이 '경사 하강법'

<img src="./gradient.png" width=400>

<br/>

*** 

## [WARNING]
* 손실 함수의 각 지점에서 함수의 값을 낮추는 방안을 제시하는 지표는 단지 '기울기'뿐 
* 기울기가 가리키는 방향이 Global minima인지는 보장 못함 
    * 실제로 복잡한 손실 함수에서는 기울기가 가리키는 방향에 최솟값이 없을 수도 있음 

<br/>

<b>EXAMPLE</b>: saddle point(안장점)
* 

 <img src="./saddle_poin2.png" width=600>