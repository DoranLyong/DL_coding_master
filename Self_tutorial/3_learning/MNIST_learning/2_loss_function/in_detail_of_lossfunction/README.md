[(back)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/2_loss_function)

# [왜 손실 함수를 지표로 사용할까?](https://blog.naver.com/cheeryun/221387314571)

### 우리가 원하는 건 (목적)
* ### 주어진 데이터를 ```정확하고 정밀하게 예측하는 모델```을 만드는 것

### 우리의 목표는 
* ### '<b>정확도</b>(accuracy)'를 최대로 끌어내는 매개변수 값을 찾는 것.

<br/>
그렇다면,

## <img src="6_but_why.png" width=33> 평가 지표를 '<span style="color:skyblue"> 얼마나 좋으냐</span>(accuracy)'를 사용하는게 더 자연스럽지 않나? <br/>
* ### <span style="color:orange">손실 함수의 값<sup>(=얼마나 나쁜가요?)</span>을 통해 우회적으로 평가하는 미유는?
    * 신경망 학습에서의 '미분'의 역할 때문 
        > 활성화 신호 값을 미분 

<br/>

※ 확률에서 우회적으로 표현하는 수식 
* P(A) = 1 - P(A<sup>c</sup>)

<br/>

## 신경망 학습에서 '미분'의 역할 
* ### 매개변수의 갱신 방향을 찾아주는 역할 

    * ### 최적의 매개변수(bias<sup>편향</sup>, weight<sup>가중치</sup>)를 탐색할 때, <br/>
        > <span style="color:orange">손실 함수의 값을 최소로 하는</span>매개변수 값을 찾아야 함  
    * ### 이때, 매개변수의 미분값(=기울기)을 계산함
        > 그 미분 값을 단서<sup>cue</sup>로 해서 매개변수의 값을 서서히 갱신하는 과정을 반복 

        <img src="loss_func.png" width=300>

<br/>

## '가중치 매개변수에 대한 손실 함수의 미분'의 의미 
* ### ```가중치를 조금 변화 시켰을 때, 손실 함수가 어떻게 변하니?```

<br/>

## 매개변수 갱신 방법 
* ### 미분값 < 0  ⇒ 매개변수를 양의 방향으로 변환(=이쪽 방향이다 계속해) → 손실 함수 값을 줄임
* ### 미분값 > 0  ⇒ 매개변수를 음의 방향으로 변환(=반대 방향으로 돌려) → 손실 함수 값을 줄임 
* ### 미분값 = 0 ⇒  매개변수를 어느 쪽으로든 움직여봄 → 손실 함수 값 변화 無 →  <span style="color:orange">갱신 멈춤 </span>