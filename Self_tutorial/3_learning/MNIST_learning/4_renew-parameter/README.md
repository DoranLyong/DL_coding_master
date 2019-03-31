[(back)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning)

# 가중치 매개변수 갱신 방법 
손실 함수를 가중치 매개변수에 대해 미분하여 손실 함수가 최소가 되는 방향으로 갱신한다 

## <img src="2_where_to_do.PNG" width=35> 필요한 개념 
* ### [미분](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/4_renew-parameter/1_diff)
    * ### 미분 계산 법 
        * 수치적 미분(numerical differentiation)
        * 해석적 미분(analytic differentiation) 
            > backpropagation으로 구현 됨 <br/>
        

    * ### 편미분(다변수 미분)
        * 다변수 함수의 기울기<sub>gradient</sub>

<br/>

## <img src="5_how_to_do.png" width=35> 최적 매개변수 탐색 기법의 본질 
### 1. 경사 하강법(gradient descent)
### 2. 신경망에서의 기울기 