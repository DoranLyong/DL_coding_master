[(Self_tutorial)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial)
# 학습(Learning)
## 컴퓨터가 데이터를 가지고 학습한다! 
데이터의 패턴 찾기 

* Machine Learning 작업 2 가지 <br/>
    (1) 학습(learning) <br/>
    (2) [추론(inference)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/2_inference) <br/>
    ※ p.95, 176 

<br/>

### 컴퓨터의 학습(learning)
* 데이터 패턴에 적합한 가중치 매개변수의 최적값을 <b>자동으로 찾는 과정</b>  
    > (모델의 가중치 파라미터를 알아서 찾아주면 좋겠다)

<br/>

### 학습을 시키기 위해 필요한 것? <br/>

* 우리는 시험을 통해 내가 무엇을 공부하고 어느 정도 알고 있는지 측정함 → 부족한 부분 더 공부 <br/>

* 컴퓨터를 학습 시킬때도 마찬가지 
    * 모델이 학습된 정도를 나타내는 지표(=가늠자, 시험)
        > 손실 함수(= 목적 함수 or 비용 함수) <br/>
        > Loss(= object, cost) function 

    * 최적 탐색 알고리즘 (최적의 공부 방법 찾기)
        > ex) GD, SGD, Adam ... etc  

    * 매개변수 갱신 (찾을 방법대로 공부한다) <br/>
        > <img src="e_6.1.png" width=140> 

# 학습 예시 문제 
* [MNIST 숫자 분류 학습]()