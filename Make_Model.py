from PIL import Image
import numpy as np
from sklearn import svm, metrics, model_selection, metrics
import joblib
import os


#0~9까지의 이미지 파일을 모아 놓은 폴더(추후 전역변수로 사용할 것)
image_paths = "C:\\TEMP\\20240503\\masked\\"

# 이미지 데이터를 저장할 리스트
image_data = []
# 레이블을 저장할 리스트(0-9까지 레이블링)
labels = []

# 0 - 9 까지 분류해놓은 폴더를 순회하며 데이터 이미지 및 레이블링 시작
for i in range(10):
    #이미지 경로 조립(ex. "C:\\TEMP\\20240503\\masked\\" + "0,1,2...")
    folderpath = image_paths + str(i) + "\\"
    file_list = os.listdir(folderpath)
    
    for file in file_list:
        #경로 조립
        path = folderpath + file
        # 이미지 로드
        img = Image.open(path)
        # 이미지를 흑백으로 변환하고 크기를 8x8로 조정
        img = img.convert('L').resize((8, 8))
        # 이미지를 numpy 배열로 변환
        img_array = np.array(img)
        # 이미지 데이터를 평평하게 펼쳐서 특징 벡터로 변환
        img_vector = img_array.flatten()
        # 이미지 데이터 리스트에 추가
        image_data.append(img_vector)
        # 레이블 추가 (ex. 클래스 0, 1, 2 ...)
        labels.append(i)

image_data = np.array(image_data) # 이미지 행렬 array
labels = np.array(labels) # 레이블링 행렬 array


#생성 완료 dataset dictionary로 변환
custom_dataset = {'data': image_data, 'target': labels}


#각 딕셔너리의 key를 변수 선언
x = custom_dataset['data']
y = custom_dataset['target']

# model_selection.train_test_split 메서드를 이용하여 데이터셋을 무작위로 학습 / 테스트 세트로 분할

# x: 입력 데이터(이미지에 쓰인 숫자)
# y: 레이블 데이터(이미지를 학습시킨 레이블링)
# test_size = 전체 데이터 중 테스트로 쓰이는 데이터의 비율

# X_train: 학습 세트의 입력 데이터
# X_test: 테스트 세트의 입력 데이터
# y_train: 학습 세트의 레이블 데이터
# y_test: 테스트 세트의 레이블 데이터

X_train, X_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

# 선형 SVM(support vector machine)분류기를 생성. 주어진 데이터를 두 개의 클래스로 분류함
clf = svm.LinearSVC()
#fit 메서드를 이용하여 학습 데이터와 레이블을 학습함
clf.fit(X_train, y_train)

#데이터를 학습한 모델의 예측값을 평가함
predictionY = clf.predict(X_test)
print(f"정확도: {metrics.accuracy_score(y_test, predictionY)}")



#학습 저장(digits.pkl 경로: 파이썬 파일이 실행되는 경로)
joblib.dump(clf, 'digits.pkl')