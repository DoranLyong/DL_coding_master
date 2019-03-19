[(back)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning)

# MNIST number classifier learning 


##  

### (1) [데이터를 취급할 때 주의할 점](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/1_dataissue)

### (2) [손실 함수](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/2_loss_function) (Loss function, = cost function, object function)

### (3) [미니배치 처리](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/3_mini-batch) (mini-batch process)
> batch 처리 → 크흠... 한 번에 많이 넣으니 loss function 구하기 빡신데? → 그럼 mini-batch 

### (4) [가중치 매개변수 갱신 방법](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/4_renew-parameter)
* 최적 탐색 알고리즘
    > ex) 손실 함수의 변화 방향 찾기 <br/>
    > ( 손실 함수가 최소가 되는 방향 찾기 → 손실 함수 미분... )

<br/>

## 학습 알고리즘 구현 해보기 
* ['MNIST 숫자 분류기' 학습](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/mnist_learning)
    > mini-batch 학습 기법 以 