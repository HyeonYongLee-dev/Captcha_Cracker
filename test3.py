import cv2
import numpy as np
from matplotlib import pyplot as plt


def remove_horizontal_lines(image_path, output_path):
    # 이미지 로드
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 바이너리 이미지로 변환
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

    # 커널을 이용해 가로줄 검출
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
    detected_lines = cv2.morphologyEx(binary, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)

    
    # 가로줄을 제거
    cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt in cnts:
        cv2.drawContours(binary, [cnt], -1, (0, 0, 0), 2)

    # 원본 이미지에서 가로줄 제거된 부분으로 복원
    final_image = cv2.bitwise_not(binary)
    result = cv2.bitwise_and(img, img, mask=final_image)

    # 결과 이미지 저장
    cv2.imwrite(output_path, result)

    print("가로줄을 제거한 이미지를 저장했습니다.")

# 이미지 경로 및 출력 경로 설정
image_path = 'C:\\TEMP\\20240521\\masked\\01.jpg'
output_path = 'C:\\TEMP\\20240521\\masked\\02.jpg'
remove_horizontal_lines(image_path, output_path)
