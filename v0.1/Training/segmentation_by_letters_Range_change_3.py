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
    img = Image.open(img_dir)
    width, height = img.size
    
    
    i = 0
    for box in box_list:  # 'range'를 'box'로 변경
        cropped_image = img.crop(box)
        cropped_image_np = np.array(cropped_image)  # PIL 이미지를 numpy 배열로 변환
        resized_img_np = cv2.resize(cropped_image_np, dsize=(20, 34), interpolation=cv2.INTER_LINEAR)
        resized_img = Image.fromarray(resized_img_np)  # 다시 PIL 이미지로 변환
        file_name = f"{file.split('.')[0]}_{i}_{random.randint(0, 99999):05d}.jpg"
        file_path = os.path.join(destination_path, file_name)
        resized_img.save(file_path)
        i += 1


