import os
from datetime import datetime
from PIL import Image
import numpy as np
import joblib
import cv2
import shutil
import pyautogui
from PIL import Image







#오늘 날짜 객체 생성
today = datetime.now().strftime('%Y%m%d')
destination_path = "C:\\TEMP\\" + today + "\\" + "run_model\\"


# 폴더 생성
maskedfolder = destination_path + "masked\\"


today = datetime.now().strftime('%Y%m%d')
destination_path = os.path.join("C:\\TEMP", today, "Training_Data")
number_folder = os.path.join(destination_path, )
masked_path= os.path.join(destination_path, "masked")


for i in range(10):
    number_folder = os.path.join(destination_path, str(i))
    os.makedirs(number_folder, exist_ok=True)



file_list = [file_name for file_name in os.listdir(destination_path) if os.path.isfile(os.path.join(destination_path, file_name))]

answer = ''
# 이미지 로드 및 전처리






for file in file_list :
    file_path = os.path.join(destination_path, file)
    img = Image.open(file_path)
    img = img.convert('L').resize((8, 8))
    img_array = np.array(img)
    img_vector = img_array.flatten()

    clf = joblib.load('randomF.pkl')
    result = clf.predict([img_vector])
    answer += str(result[0])
    dst_file = os.path.join(destination_path, str(result[0]))
    shutil.move(file_path , dst_file)


'''
##################################
#이미지 확인
plt.imshow(img)
plt.axis('off')
plt.show()
#################################
'''





# 학습된 모델 불러오기


# 이미지 데이터에 대한 예측 수행



