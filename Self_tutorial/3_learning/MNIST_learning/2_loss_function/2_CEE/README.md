[(back)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/2_loss_function)

# Cross Entropy Error (CEE)
### [교차 엔트로피 오차(CEE)](https://blog.naver.com/cheeryun/221380130245) <br/>

<img src="CEE.png" width=200>

<br/>

<img src="CEE_ex.gif" width=450>

* k : 데이터의 차원 수 
* y<sub>k</sub>: 신경망의 출력 (신경망이 추정한 값)
* t<sub>k</sub>: 정답 레이플 by [one-hot encoding](https://blog.naver.com/cheeryun/221378622013)

※ w.r.t
* log : 밑이 e인 자연로그(ln = log<sub>e</sub>) 
    * 상용로그 : log10() 으로 표현 

# 구현 
