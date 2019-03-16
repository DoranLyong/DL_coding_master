[ (Self_tutorial) ](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial)

# 신경망의 신호전달 구현 

예시_3층 신경망

<br/>

## (1) 입력층에서 1층으로 신호 전달 
<img src="fig_3-18.png" width=450, height=300>

```python
X  = np.array( [1, 5] )  # (2,) shape 
W1 = np.array( [1, 2 ,3], [4, 5, 6] ) 
B1 = np.array( [10, 11, 12] )

A1 = np.dot(X, W1) + B1    # Broad casting 

"""
A1 == np.array( [a11, a12, a13] )
"""
```

## (2) 1층에서 2층으로 신호 전달 
<img src="fig_3-19.png" width=450, height=300>

```python
Z1 = relu(A1)    # 활성화 함수 거침 

W2 = np.array( [1, 2], [4, 5], [7, 8] )
B2 = np.array( [10, 11] )

A2 = np.dot(Z1, W2) + B2 

"""
A2 = np.array( [a21, a22] )
"""
```

## (3) 2층에서 1층으로 신호 전달 
<img src="fig_3-20.png" width=450, height=300>

```python
Z2 = relu(A2)    # 활성화 함수 거침 

W3 = np.array( [1, 2], [4, 5] )
B3 = np.array( [10, 11] )

A3 = np.dot(Z2, W3) + B3 

Y  = softmax(A3)

"""
Y = np.array( [y1, y2] )
"""
```

