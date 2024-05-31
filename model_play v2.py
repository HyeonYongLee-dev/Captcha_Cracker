import os
import urllib.request
from datetime import datetime
from PIL import Image
import numpy as np
import joblib
import cv2
import shutil
import random





#오늘 날짜 객체 생성
today = datetime.now().strftime('%Y%m%d')
destination_path = "C:\\TEMP\\" + today + "\\" + "run_model\\"

# 폴더 생성
os.makedirs(destination_path, exist_ok=True)



folder_path = destination_path  # 해당 폴더의 경로를 지정하세요.


# 폴더 생성
maskedfolder = destination_path + "masked\\"
os.makedirs(maskedfolder, exist_ok=True)


# 폴더 내의 모든 파일을 검사하고 .jpg 확장자를 가진 파일을 삭제합니다.
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        os.remove(os.path.join(folder_path, filename))

sample_list = 400
for i in range (sample_list):
    image_url = "https://seller.kshop.co.kr/jwork/authentication/viewCaptcha.do?W=263&H=54&F=50"
    file_name = f"captcha{i}.png"
    final_path = destination_path + file_name
    urllib.request.urlretrieve(image_url, final_path)
    final_path = os.path.join(destination_path, final_path)
    img = cv2.imread(final_path, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    bgr = img[:, :, 0:3]
    img_mask = cv2.inRange(img, (0, 0, 0), (180, 30, 30)) # BGR로부터 흑, 백 판별
    #흑백 전환
    img_mask_reverse = cv2.bitwise_not(img_mask)
    #파일 저장
    img_mask_file_path = os.path.join(destination_path, file_name)
    cv2.imwrite(img_mask_file_path, img_mask_reverse)
    #흑백 전환 파일 특정 폴더로 이동
    masked_finished_path = maskedfolder + file_name
    shutil.move(img_mask_file_path, masked_finished_path)



'''
answer = ''
# 이미지 로드 및 전처리
for i in range (6):
    
    file_number = random.randint(10000, 99999)
    new_name = f"{destination_path}{i}_{file_number}.jpg"

    save_path = f"{destination_path}{i}.jpg"       
    img = Image.open(f"{destination_path}{i}.jpg")
    img.save(new_name)
    img = img.convert('L').resize((8, 8))
    img_array = np.array(img)
    img_vector = img_array.flatten()
    clf = joblib.load('randomF.pkl')
    result = clf.predict([img_vector])
    answer += str(result[0])
 
    os.remove(f"{destination_path}{i}.jpg")
'''




#각 이미지를 저장할 폴더 생성(0 ~ 9)
for i in range(10):
    classified_Number_Folder = destination_path + f"{i}"
    os.makedirs(classified_Number_Folder, exist_ok=True)


file_count = 0
file_path = maskedfolder
file_list = os.listdir(file_path)

for file_name in file_list:
    
    img = cv2.imread(maskedfolder + file_name, 0)
        
    x, y, w, h = 11, 1 , 26, 47
    for i in range(6):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped_img = img[y:y+h, x:x+w]
        
        file_number = random.randint(00000, 99999)
        new_name = f"{destination_path}{i}_{file_number}.jpg"


        cv2.imwrite(new_name, cropped_img)
        img2 = Image.open(new_name)
        img2 = img2.convert('L').resize((8, 8))
        img_array = np.array(img2)
        img_vector = img_array.flatten()
        clf = joblib.load('randomF.pkl')
        result = clf.predict([img_vector])
        dst_file = destination_path + str(result[0])
        src_file = new_name
        shutil.move(src_file , dst_file)
        x += w
   
    print(maskedfolder + file_name)
    os.remove(maskedfolder + file_name)
   
# 학습된 모델 불러오기


# 이미지 데이터에 대한 예측 수행


