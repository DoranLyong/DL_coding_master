[(back)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning)

# 손실 함수 (loss function)
학습의 정도를 나타내는 "<span style="color:skyblue">지표</span>", 가늠자 
> 즉, 모델의 학습 정도를 수량화 시킨 것 .

<br/>

## 1. 정도의 수량화는 왜 필요한가?
대상의 상타나 성능을 객관적으로 볼 수 있게 도와줌 <br/>
* ∴ 수치적으로 정량화 시키는 것이 필요함 
    > 이를 통해 문제점을 얼마나 개선할지 계획을 세울 수 있음 

<br/>

### Example 1_수치적 지표가 없는 막연한 대답 
```
Q: "지금 얼마나 행복해요?" 

A: "아주 행복해요"
```

### Example 2_행복을 수량화해서 대답 
```
Q: "지금 얼마나 행복해요?"

A: "현재 나의 행복 지수는 10.23입니다." 

Q: ?!
```

<br/>

## 2. 신경망의 학습 상태를 나타내는 지표는? 

손실 함수(loss function)을 사용한다 


### (1) 정의 
* '<b><span style="color:orange">나쁨의 정도</span></b>'를 나타내는 지표
    > 현재 신경망이 '훈련 데이터'얼마나 잘 처리 못 하는지를 나타냄 

### (2) 이유 
* [왜 '<b>성능 나쁨</b>'을 지표로 사용할까?]()