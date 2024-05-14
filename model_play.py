import os
import urllib.request
from datetime import datetime
from PIL import Image
import numpy as np
import joblib

#오늘 날짜 객체 생성
today = datetime.now().strftime('%Y%m%d')

default_path = "C:\\python\\"
destination_path = "C:\\TEMP\\" + today + "\\"

image_url = "https://seller.kshop.co.kr/jwork/authentication/viewCaptcha.do?W=263&H=54&F=50"
file_name = "captcha.png"
final_path = destination_path + file_name
urllib.request.urlretrieve(image_url, final_path)




# 이미지 로드 및 전처리
img = Image.open(final_path)




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