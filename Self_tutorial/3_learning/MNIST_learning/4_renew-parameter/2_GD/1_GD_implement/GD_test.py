import numpy as np 
import matplotlib.pyplot as plt 


def plotting(x_history):
    plt.plot( [-5, 5], [0,0], '--b')
    plt.plot( [0,0], [-5, 5], '--b')
    plt.plot(x_history[:,0], x_history[:,1], 'o')

    plt.xlim(-3.5, 3.5)
    plt.ylim(-4.5, 4.5)
    plt.xlabel("X0")
    plt.ylabel("X1")
    plt.show()

def numerical_gradient( f, x ):
    h = 1e-4    # 0.0001 
    grad = np.zeros_like(x)      # x와 형상이 같은 zero-배열을 생성 

    for idx in range(x.size):
        tmp_val = x[idx]

        """ f(x+h) 계산 """
        x[idx] = tmp_val + h 
        fxh1 = f(x)

        """ f(x-h) 계산 """ 
        x[idx] = tmp_val - h 
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)

        x[idx] = tmp_val  # 값 복원  
        
    return grad


def gradient_descent(f, init_x, lr=0.1, step_num=100):
    x = init_x     # 초기 시작점 
    x_history = []

    for i in range(step_num):
        x_history.append( x.copy() )

        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x, np.array(x_history)

def function(x): 
    return x[0]**2 + x[1]**2


def main():
    init_x = np.array( [-3.0, 4.0] ) 
    
    x, x_history= gradient_descent(function, init_x=init_x, lr=0.1, step_num=100)

    print(x)

    plotting(x_history)

if __name__ == "__main__":
    main()