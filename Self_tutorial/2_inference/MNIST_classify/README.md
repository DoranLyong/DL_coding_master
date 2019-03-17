[ (back) ](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/2_inference)

# MNIST number classification 


## Dataset
* [MNIST_database](http://yann.lecun.com/exdb/mnist/)

* 구성 
    > 0 ~ 9 의 숫자 이미지 <br/>
        >   * size: (28, 28) <br/>
        >   * ndim: gray_scale ... (1-channel)<br/>
        >   * value_range: [0, 255] <br/>
        >   * train_set : 60,000장 , test_set: 10,000장  <br/>

    > 각 이미지에 ground_truth인 숫자 라벨<sub>label</sub> 이 붙어 있음


    <img src="./fig_3-24.png" width=300>

<br/>

* 활용 방식 
    > Model learning with the <b>train_set </b>

    > Performance evaluation with the <b>test_set  </b>

<br/> <br/>


## 실습 단계 
(1) [데이터셋을 내려받아(download) 이미지를 넘파이 배열(array)로 변환]()

(2) [신경망의 추론 처리 (for classification)]()
> 모델이 학습 됐다고 가정  

(3) [배치 처리(batch)]()
