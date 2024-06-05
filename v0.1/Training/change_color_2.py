import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
from datetime import datetime

#학습 데이터 절대경로 가져오기
today = datetime.now().strftime('%Y%m%d')
destination_path = os.path.join("C:\\TEMP", today, "Training_Data")

file_list = [file_name for file_name in os.listdir(destination_path) if os.path.isfile(os.path.join(destination_path, file_name))]

# 폴더 생성
maskedfolder= os.path.join(destination_path, "masked")
os.makedirs(maskedfolder, exist_ok=True)


for file_name in file_list:
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
    masked_finished_path = os.path.join(maskedfolder, file_name)
    shutil.move(img_mask_file_path, masked_finished_path)




