[(back)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning)

# [미니배치 학습 (mini-batch learning)](https://blog.naver.com/cheeryun/221380230376)

[Batch 처리](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/2_inference/MNIST_classify/3_batch_process) → <img src="meeting_problem.png" width=33>크흠... 한 번에 너무 많으니까 Loss function 구하기 빡신데? → 그럼 mini-batch 


## 배치(batch)처리 vs 미니배치(mini-batch learning)
* p.102, 배치 처리: 
    > 입력 데이터를 한번에 넣기 
* p.115, 미니배치 학습: 
    > 모든 훈련 데이터에 대한 손실 함수를 한번에 구하기 

<br/>

표현은 달리 했지만 맥락은 똑같음: <br/>
이미지를 한 장씩 넣으면 번거롭다 → 한 뭉탱이로 넣자```(batch 처리)``` → 60,000장 뭉탱이를 한 번에 넣고 학습하기에는 손실함수 구할 때 빡시다 → 그러면 100장 뭉탱이만 넣어서 하자```(mini-batch)``` 

*** 

