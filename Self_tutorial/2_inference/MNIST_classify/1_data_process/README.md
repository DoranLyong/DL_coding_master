[ (back) ](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/2_inference/MNIST_classify)

데이터가 물리적 메모리 공간을 차지하면 '객체' 

# 데이터 처리 
p.97 <br/>

※ [데이터 전처리](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/2_inference/MNIST_classify/1_data_process/data_preprocess) 

<br/>

## 1. 데이터 로드 처리 
*load_data.py

(1) 데이터 내려받기(download) & 코드로 불러오기(load) <br/>

(2) 데이터를 'numpy.ndarray' 자료형으로 변환해서 저장  
> serialized_data → [Pickle] → numpy.array 

<br/>

## 2. MNIST 이미지 표출하기 

* PIL 패키기 
* mnist_show.py
> Python Image Library

***
<br/>


## '데이터 로딩' 코드 분석 

※ w.r.t
*  [파일 처리(열기, 읽기, 쓰기, 닫기)](https://blog.naver.com/cheeryun/221351470622)
    > with open(...) as <파일 객체>:
* [피클(pickle)](https://blog.naver.com/cheeryun/221378069487)
    > python [데이터 직렬화](https://blog.naver.com/cheeryun/221378092544) 컨버터 

<br/>

Dataprocess.py
```python
dataset_dir = os.path.dirname(os.path.abspath(__file__))
print("directory_path= ", dataset_dir)

save_file = dataset_dir + "/mnist.pkl" # dataset path 


def load_mnist(normalize=True, flatten=True, one_hot_label=False):

    """
    normalize : 이미지의 픽셀 값을 0 ~ 1 사이의 값으로 정규화할지 결정 

    one_hot_label : 원-핫 인코딩
        레이블을 원-핫(one-hot) 배열로 돌려줌. 
        * one-hot array = [0,0,1,0,0,0,0,0,0,0]처럼 한 원소만 1인 배열

    flatten : 입력 이미지를 1차원 배열로 평활화할지 결정 

    Returns
    -------
    (train_img, train_label), (test_img, test_label)
    """
    with open(save_file, 'rb') as f:
        dataset = pickle.load(f)

    if normalize: 
        for key in ('train_img', 'test_img'):
            dataset[key] = dataset[key].astype(np.float32)
            dataset[key] /=255.0 

    if one_hot_label:
        dataset['train_label'] = _change_one_hot_label(dataset['train_label'])
        dataset['test_label'] = _change_one_hot_label(dataset['test_label'])   

    if not flatten:
        for key in ('train_img', 'test_img'):
            dataset[key] = dataset[key].reshape(-1, 1, 28, 28)
    
    return (dataset['train_img'], dataset['train_label']), (dataset['test_img'], dataset['test_label'])


def _change_one_hot_label(X):
    T = np.zeros((X.size, 10))
    for idx, row in enumerate(T):
        row[X[idx]] = 1
        
    return T
```
<br/>

***

## MNIST 이미지 표출
### ★ flatten=true 설정으로 데이터를 로드했다면, 이미지는 1차원 numpy.array로 저장돼 있음. <br/>

* but, 이미지는 2차원 배열이다 

    > ∴ 원래 형상(shape)인 28 x 28 크기로 다시 변형해라 <br/>
    > ☞  <numpy인스턴스>.reshape(28, 28)

* load_mnist( ... )
    > load_data.py 참고 

<br/>

mnist_show.py
```python
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

```