[(back)](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/4_renew-parameter)

# 미분 (differentiation)

## <img src="definition.png" width=35> [미분 개념](https://blog.naver.com/cheeryun/221453596358)
* 특정 시점에 가까워 질 때(dt → 0), 이 점 근처의 변화율을 나타내는 최상의 <b>상수 근사값</b> <br/>

    * <img  src="diff.gif" >   <b>[식 1]</b> <br/> 
        > 컴퓨터로 계산할 때 

    * <img src="diff_math.gif"> <b>[식 2]</b> <br/>
        > 수학적으로 표현 


<br/>

## <img src="meeting_problem.png" width=35> 수치 미분의 문제점 

* ###   [[식1] 대로 구현해보기](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/4_renew-parameter/1_diff/1_diff_eq)
    * 반올림 오차 문제 이해
    * 함수 차분 문제 이해 

<br/>

***

## <img src="6_but_why.png" width=35> 편미분 (다변수 미분)
 다변수 함수에 대한 미분법 ☞ 편미분 
    
<b>__ EXAMPLE __ </b> f(x<sub>0</sub> ,  x<sub>1</sub>) = x<sub>0</sub><sup>2</sup> + x<sub>1</sub><sup>2</sup>을 변수 x<sub>0</sub> , x<sub>1</sub>에 대하여 미분하시오 


### <img src="5_how_to_do.png" width=35> [편미분 방법](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/4_renew-parameter/1_diff/2_partial_deriv)
* 어느 변수에 대한 미분인지를 먼저 구별해야 함 
    * x<sub>0</sub>에 대한 미분 :   <img src="partial_x0.gif" >
    * x<sub>1</sub>에 대한 미분 : <img src="partial_x1.gif">

* 편미분은 변수가 하나인 미분과 마찬가지로 <span style="color:orange"> 특정 장소의 기울기</span>를 구함 
    * 단, 여러 변수 중 목표 변수 하나에 초점을 맞추고 다른 변수는 상수 값으로 고정 

<br/>

# <img src="what_to_do_object.png" width=35> 편미분을 통해 다변수 함수의 기울기를 표현함 
편미분의 결과인 <img src="partial_x0.gif">와 <img src="partial_x1.gif">를 벡터로 정리하면 다변수 함수의 <span style="color:skyblue">기울기(gradient)</span>가 됨 
* <img src="gradient_vector.gif">  

    > <img src="gradient.jpg" width=200>

* ## [구현](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/3_learning/MNIST_learning/4_renew-parameter/1_diff/3_gradient)

