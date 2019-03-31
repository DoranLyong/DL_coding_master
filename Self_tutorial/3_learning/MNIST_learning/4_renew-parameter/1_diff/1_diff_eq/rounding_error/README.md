# Rounding Error (반올림 오차)  
### 컴퓨터가 표현할 수 있는 수의 resolution이 제한돼 있어서 생기는 문제 
* ### 숫자가 너무 커 ⇒ overflow 
* ### 숫자가 너무 작아 ⇒ rounding error 


```python 
>> np.float32(10e-50)
0.0 
``` 
* 10e-50은 너무 작아서 컴퓨터가 표현할 수 없음 
    > 0.0으로 인식함 

<br/>

* <img src="what_to_do_object.png" width=35> 개선 하기 
    > 10<sup>-4</sup> = 1e-4   정도면 좋은 결과를 얻는다고 알려짐 

<br/>

***

<img src="10e-50.png" width =300>

* dt = 10e-50  일 때, rounding error 때문에 미분계수가 계산 안 됨 

<br/>

<img src="1e-4.png" width=300>

* dt = 1e-4 일 때, 컴퓨터가 미분계수 계산 잘 함 