[ (back) ](https://github.com/DoranLyong/DL_coding_master/tree/master/Self_tutorial/2_inference/MNIST_classify)

데이터가 물리적 메모리 공간을 차지하면 '객체' 

# 데이터 처리 
※ p.97

<br/>

(1) 데이터 내려받기(download) & 코드로 불러오기(load)

(2) 데이터를 'numpy.ndarray' 자료형으로 변환 
> 데이터의 형변환 


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