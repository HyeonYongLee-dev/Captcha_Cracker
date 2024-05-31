import cv2
import numpy as np
import os

def decaptcha(file_path):
    # 이미지 로드
    src = cv2.imread(file_path)

    # 라인의 색상 (BGR 포맷)
    lines_color = (0x70, 0x70, 0x70)

    # 라인의 색상을 기준으로 마스크 생성
    binary_mask = cv2.inRange(src, lines_color, lines_color)

    # 마스크를 사용하여 이미지 생성
    masked = cv2.bitwise_and(src, src, mask=binary_mask)

    # 라인 팽창
    lines_dilate = 3
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (lines_dilate, lines_dilate))
    masked = cv2.dilate(masked, element)

    # 마스크를 그레이스케일로 변환
    masked = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)

    # 큰 라인 복원
    dst = src.copy()
    dst = cv2.inpaint(dst, masked, 3, cv2.INPAINT_NS)

    # 작은 라인 제거
    lines_dilate = 2
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (lines_dilate, lines_dilate))
    dst = cv2.dilate(dst, element)

    # Gaussian 블러 적용
    dst = cv2.GaussianBlur(dst, (5, 5), 0)

    # Bilateral 필터 적용
    dst = cv2.bilateralFilter(dst, 5, 75, 75)

    # 그레이스케일 변환 및 이진화
    dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    _, dst = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 파일 저장
    output_path = os.path.join(
        os.path.dirname(file_path),
        os.path.splitext(os.path.basename(file_path))[0] + "_dst" + os.path.splitext(file_path)[1]
    )
    cv2.imwrite(output_path, dst)

# 파일 경로 설정
file_path = "C:\\TEMP\\20240522\\run_model\\masked\\captcha.png"
decaptcha(file_path)
