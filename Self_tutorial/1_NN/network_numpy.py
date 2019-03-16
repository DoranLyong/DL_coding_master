import numpy as np 
from dlutile import Activation


def init_weight(): 
    weight = {}     # <dict> 클래스로 인스턴스 
                     # { 'W' : <array> }

    # input -> 1-layer                      
    weight['W1'] = np.array( [ [1, 2 ,3], [4, 5, 6] ])
    weight['B1'] = np.array( np.array( [10, 11, 12] ) )  

    # 1-layer -> 2-layer 
    weight['W2'] = np.array([ [1, 2], [4, 5], [7, 8] ])
    weight['B2'] = np.array( [10, 11] )

    # 2-layer -> output-layer
    weight['W3'] = np.array( [ [1, 2], [4, 5] ])               
    weight['B3'] = np.array( [10, 11] )

    return weight

def forward( weight, X ): 
    # Weights
    W1, W2, W3 = weight['W1'], weight['W2'], weight['W3']
    B1, B2, B3 = weight['B1'], weight['B2'], weight['B3']

    A1 = np.dot(X, W1) + B1 # input -> 1-layer 
    Z1 = Activation.sigmoid(A1)

    A2 = np.dot(Z1, W2) + B2 # 1-layer -> 2-layer 
    Z2 = Activation.sigmoid(A2)

    A3 = np.dot(Z2, W3) + B3 # 2-layer => output-layer 
    Y  = Activation.softmax(A3)

    return Y 


def main():
    weights = init_weight()   # set of weights 
    X = np.array( [1, 0.5] )  # input_data
    Y = forward( weights, X ) # output
    print(Y)

if __name__ == "__main__":
    main()