[(back)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/2_inference/MNIST_classify/1_data_process)
# 데이터 전처리(pre-processing)
사전에 입력 데이터에 특정 변환을 가하는 것 

<br/>

## 장점 
(1) 모델의 식별 능력이 개선됨 <br/>
(2) 학습 속도가 높아짐 <br/>
(3) etc. 

## 종류 
* 정규화(normalization)
    * 방법1: 데이터들이 0을 중심으로 분포하도록 이동 (평균 0인 정규분포)
    * 방법2: 데이터의 확산 범위를 제한 (표준 편차 크기로 제어)
        > 데이터 전체 평균과 표준편차를 활용함 

        > 데이터가 정규분포를 따르면 해석하기 쉬움<br/> (이미 특징을 아는 distribution이라서)

* 백색화(whitening)
    * 전체 데이터를 균일하게 분포시킴 


기타 등등 ...