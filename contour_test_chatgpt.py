import cv2
import numpy as np
import os

def preprocess_image(image_path):
    # 이미지 읽기
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image file not found at {image_path}")
    
    # 이진화 처리
    _, thresh = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
    
    return image, thresh

def find_and_sort_contours(thresh):
    # 윤곽 찾기
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 윤곽을 감싸는 사각형 (bounding box) 찾기 및 필터링
    bounding_boxes = [cv2.boundingRect(contour) for contour in contours]
    bounding_boxes = [box for box in bounding_boxes if box[2] > 5 and box[3] > 5]  # 최소 크기 필터링
    
    # 사각형을 x 좌표 기준으로 정렬
    bounding_boxes = sorted(bounding_boxes, key=lambda box: box[0])
    
    return contours, bounding_boxes

def save_and_draw_contours(image, bounding_boxes, output_folder='digits'):
    # 디렉토리 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for i, (x, y, w, h) in enumerate(bounding_boxes):
        digit_image = image[y:y+h, x:x+w]
        output_path = os.path.join(output_folder, f'digit_{i}.png')
        cv2.imwrite(output_path, digit_image)
        
        # 컨투어를 원본 이미지에 그리기
        result_image = digit_image.copy()
        cv2.rectangle(result_image, (0, 0), (w, h), (0, 255, 0), 2)  # 바운딩 박스 그리기
        cv2.imshow(f'Digit {i}', result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main(image_path):
    try:
        image, thresh = preprocess_image(image_path)
        contours, bounding_boxes = find_and_sort_contours(thresh)
        
        # 개별 숫자 이미지 저장 및 컨투어 그리기
        save_and_draw_contours(image, bounding_boxes)
        print("각 숫자가 개별적으로 저장되고 컨투어가 그려졌습니다.")
    except Exception as e:
        print(f"Error: {e}")

# 사용 예시
image_path = "C:\\TEMP\\20240516\\run_model\\masked\\captcha.png"  # CAPTCHA 이미지 파일 경로
main(image_path)
