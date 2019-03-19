[ (back) ](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/2_inference/MNIST_classify)
# 배치 처리 (batch process)
※ p. 102, 239 

* batch : (일괄적으로 처리되는) 집단, 무리 
    * A group 
        > which is dealt with <b>at the same time</b> or is sent to a particular place <b>at the same time</b><br/>
    
<br/>

"한입만!!!" <br/>
한입 크게 베어먹으면 빨리 먹을 수 있음 

<img src="./batch_symbol.jpg" width=300>

<br/>

### 즉, 배치 처리(batch process)
* 묶음 입력 데이터 만들기 <br/>

    <b>EXAMPEL__</b> 100만원 지불하기 <br/>
    * non-batch ⇒ 1만원 씩 100번 넣기 
    * batch ⇒ 100만원 한 뭉치 넣기 

<br/>

## 처리 방법   
(1) 한 번에 다 넣기는 넘 크다. 조금 작은 덩어리로
* mini-batch <br>

(2) Convolution layer을 위한 batch process? 