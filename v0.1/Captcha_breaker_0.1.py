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
os.makedirs(destination_path, exist_ok=True)



# 캡쳐할 영역의 좌표와 크기 지정 (left, top, width, height)
region = (800, 432, 220, 43)

# 지정된 영역을 캡쳐합니다
screenshot = pyautogui.screenshot(region=region)

# 캡쳐한 이미지를 파일로 저장합니다
screenshot.save(destination_path + "partial_screenshot.png")






# 폴더 생성
maskedfolder = destination_path + "masked\\"
os.makedirs(maskedfolder, exist_ok=True)


#각 파일 절대경로 조립 
file_name = "partial_screenshot.png"
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




    
img = Image.open(masked_finished_path)
width, height = img.size


# box_0 = (12, 6, 34, 40) #(left, upper, right, lower)
# box_1 = (34, 6, 49, 40) #(left, upper, right, lower)
# box_2 = (49, 6, 69, 40) #(left, upper, right, lower)
# box_3 = (69, 6, 89, 40) #(left, upper, right, lower)
# box_4 = (89, 6, 105, 40) #(left, upper, right, lower)
# box_5 = (105, 6, 124, 40) #(left, upper, right, lower)

# 각 box 좌표 정의
boxes = [
    (12, 6, 34, 40),  # box_0
    (34, 6, 49, 40),  # box_1
    (49, 6, 69, 40),  # box_2
    (69, 6, 89, 40),  # box_3
    (89, 6, 105, 40),  # box_4
    (105, 6, 124, 40)  # box_5
]

box_list = []

# box_list에 각 box 좌표 추가
for i in range(6):
    box_list.append(boxes[i])


i = 0

for range in box_list:
    cropped_image = img.crop(range)
    cropped_image.save(f"{destination_path}{i}.jpg")
    i += 1




file_list = [file_name for file_name in os.listdir(destination_path) if os.path.isfile(os.path.join(destination_path, file_name))]

answer = ''
# 이미지 로드 및 전처리

for file in file_list :
    img = Image.open(destination_path + file)
    img = img.convert('L').resize((8, 8))
    img_array = np.array(img)
    img_vector = img_array.flatten()

    clf = joblib.load('randomF.pkl')
    result = clf.predict([img_vector])
    answer += str(result[0])
    print(result[0])


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



