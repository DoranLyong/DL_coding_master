[(back)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/2_loss_function)
# Mean Squared Error (MSE)
### 평균 제곱 오차(MSE) <br/>

<img src="MSE.png" width=200>

* y<sub>k</sub> : 출력층의 k번째 노트의 출력 
    > 신경망이 추정한 값 
* t<sub>k</sub> : [타겟(target, 정답 레이블)](https://blog.naver.com/cheeryun/221380130245)
* k : [출력 데이터의 차원 수](https://blog.naver.com/cheeryun/221380130245)


<br/>

## 구현 
* p. 112
* MNIST 숫자 분류기 출력단 참고 
```python
def mse(y, t):
    return 0.5 * np.sum( (y-t)**2 )

>> y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0] # softmax function 출력 
>> t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]  # one-hot encoding

>> mse( np.array(y), np.array(t) )
0.09750000000000003
```
### y 출력에서 2번째 노드의 출력값이 0.6으로 제일 크다 
> 신경망은 정답이 '2'일 확률이 0.6이라고 추정함 

### 정답 레이블도 타겟이 '2'로 인코딩 돼 있음 
> [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

### MSE = 0.097 
> '나쁨 정도'가 0.097 