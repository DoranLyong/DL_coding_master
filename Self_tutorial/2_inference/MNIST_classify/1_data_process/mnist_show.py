#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys, os 
sys.path.append(os.pardir)   # 파이썬 모듈 위치 정보에 부모 디렉토리 추가 
import numpy as np 
from Dataprocess import load_mnist
from PIL import Image 


def img_show(img):
    print("Image show")
    image = Image.fromarray(np.uint8(img))
    image.show()


def data_load():
    print("Load MNIST data...")
    (x_train, t_train), (x_test, t_test) = \
                      load_mnist( flatten=True,normalize=False)
    return  (x_train, t_train), (x_test, t_test) 

def main():

    #Load data
    (x_train, t_train), (x_test, t_test) = data_load()

    img = x_train[0]
    label = t_train[0]
    print("label of x_train[0]: ", label)

    # Print Image 
    print("Flatten shape is : ", img.shape)
    reshape_img = img.reshape(28, 28) 
    print("Reshape: ", reshape_img.shape)

    img_show(reshape_img)

    print("Done!")


if __name__ == "__main__":
    main()
