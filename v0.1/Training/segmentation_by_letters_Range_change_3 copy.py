import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from datetime import datetime
import os
import shutil
import random
#학습 데이터 절대경로 가져오기
today = datetime.now().strftime('%Y%m%d')
destination_path = os.path.join("C:\\TEMP", today, "Training_Data")
masked_path= os.path.join(destination_path, "masked")





# 6개 숫자를 일정하게 split(중첩되는 글자로 인해 크기를 고정함. split하는 방법 알면 수정 필요)
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
for i in range(6):
    box_list.append(boxes[i])

file_list = [file_name for file_name in os.listdir(masked_path) if os.path.isfile(os.path.join(masked_path, file_name))]

for file in file_list :
    img_dir = os.path.join(masked_path, file)    
    img = cv2.imread(img_dir, cv2.IMREAD_GRAYSCALE)
    # 이미지를 이진화합니다.
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # 윤곽선을 찾습니다.
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 찾은 윤곽선을 이미지에 그립니다.
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

    # 결과 이미지를 출력합니다.
    cv2.imshow('Contours', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


