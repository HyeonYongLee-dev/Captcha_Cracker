import joblib
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

image_path = "C:\\TEMP\\20240527\\run_model\\partial_screenshot.png"

# 이미지 로드 및 전처리
img = Image.open(image_path)




img = img.convert('L').resize((8, 8))
'''
##################################
#이미지 확인
plt.imshow(img)
plt.axis('off')
plt.show()
#################################
'''


img_array = np.array(img)
img_vector = img_array.flatten()

# 학습된 모델 불러오기
clf = joblib.load('randomF.pkl')

# 이미지 데이터에 대한 예측 수행
prediction = clf.predict([img_vector])

print("결과!!!:", prediction)