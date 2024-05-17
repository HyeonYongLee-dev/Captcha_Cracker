import os
import urllib.request
from datetime import datetime
from PIL import Image
import numpy as np
import joblib
import cv2
import shutil

#오늘 날짜 객체 생성
today = datetime.now().strftime('%Y%m%d')
destination_path = "C:\\TEMP\\" + today + "\\" + "run_model\\"

# 폴더 생성
os.makedirs(destination_path, exist_ok=True)


image_url = "https://seller.kshop.co.kr/jwork/authentication/viewCaptcha.do?W=263&H=54&F=50"
file_name = "captcha.png"
final_path = destination_path + file_name
urllib.request.urlretrieve(image_url, final_path)

# 폴더 생성
maskedfolder = destination_path + "masked\\"
os.makedirs(maskedfolder, exist_ok=True)


#각 파일 절대경로 조립
final_path = os.path.join(destination_path, file_name)
# 이미지 로드
img = cv2.imread(final_path, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# BGR 채널 추출
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




    
img = cv2.imread(masked_finished_path, 0)
    
x, y, w, h = 11, 1 , 26, 47
for i in range(6):
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped_img = img[y:y+h, x:x+w]
    save_path = f"{destination_path}{i}.jpg"
    cv2.imwrite(save_path, cropped_img)
    x += w


answer = ''
# 이미지 로드 및 전처리
for i in range (6):
    save_path = f"{destination_path}{i}.jpg"    
    img = Image.open(f"{destination_path}{i}.jpg")
    img = img.convert('L').resize((8, 8))
    img_array = np.array(img)
    img_vector = img_array.flatten()

    clf = joblib.load('randomF.pkl')
    result = clf.predict([img_vector])
    answer += str(result[0])

    
print(answer)

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


