 #!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys, os 
sys.path.append(os.pardir)           # 부모 디렉토리 경로를 sys.path에 추가 (p.98)
import numpy as np
from dataset.mnist import load_mnist  # MNIST 데이터를 Numpy 객체로 불러오기 



def miniBatch(x_train, t_train, batchSize=10):
    print("[INFO] mini-batch selection...")

    train_size = x_train.shape[0]  # 전체 데이터 개수(= 전체 batch)
    batch_mask = np.random.choice(train_size, batchSize) # 0~59999 숫자 중 임의로 batchSize 만큼 고름 

    x_batch = x_train[batch_mask]  # 뽑힌 숫자를 index로 사용 
    t_batch = t_train[batch_mask]

    return x_batch, t_batch



def main():
    (x_train, t_train), (x_test, t_test) = load_mnist( normalize=True, one_hot_label=True)
    print(x_train.shape)    # (60000, 784) = (데이터 개수, 평활화된 이미지 배열 28x28 = 784)
    print(t_train.shape)    # (60000, 10) = (데이터 개수, 레이블 클래스 개수)


    minibatch_x, minibatch_t = miniBatch(x_train, t_train, batchSize = 100) 
    print(minibatch_x.shape)
    print(minibatch_t.shape)

if __name__ == "__main__":
    main()