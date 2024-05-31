import cv2
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
import os


file_path = "C:\\TEMP\\20240523\\01.jpg"
output_dir = "C:\\TEMP\\20240523\\"

#이미지 input
img = cv2.imread(file_path)
#RGB -> Gray
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



# 커널 정의 (모폴로지 연산에 사용)
kernel = np.ones((3, 3), np.uint8)


# 모폴로지 Gradient 적용(경계 이미지 추출)
gradient_image = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

#잡영 제거(adaptivethreshold)
th = cv2.adaptiveThreshold(gradient_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 5)

finimg = cv2.bitwise_not(th)
contours, _ = cv2.findContours(finimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 원본 이미지를 복사하여 윤곽선을 그림
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 1)

for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        cropped_contour = img[y:y+h, x:x+w]
    
        contour_file_path = os.path.join(output_dir, f'contour_{i}.png')
        cv2.imwrite(contour_file_path, cropped_contour)
        print(f'Contour {i}: x={x}, y={y}, width={w}, height={h}')

final_image_path = os.path.join(output_dir, 'contours.png')
cv2.imwrite(final_image_path, img_contours)



cv2.drawContours(img, contours, -1, (0,255,0), 1)
cv2.imshow('modified.png',img)
cv2.waitKey(0)  




#작은 구멍을 메우고 경계 강화(morph close)
closed_image = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

cv2.imshow('img', closed_image)
cv2.waitKey(0)

k = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
dst = cv2.dilate(closed_image, k)
merged = np.hstack((closed_image, dst))


#가로선 검출
lines = cv2.HoughLinesP(dst, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=7)

# 가로선 제거
if lines is not None:
    for line in lines:
        for x1, y1, x2, y2 in line:
            if abs(y1 - y2) < 20:  # y 좌표가 거의 같은지 확인 (가로선 필터링)
                cv2.line(dst, (x1, y1), (x2, y2), (0, 0, 0), 2)


cv2.imshow('img', dst)
cv2.waitKey(0)     


#contour 찾기
contours, _ = cv2.findContours(closed_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


for i, contour in enumerate(contours):
     x, y, w, h = cv2.boundingRect(contour)
     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
     
     

cv2.imshow('img', img)
plt.imshow(img)
plt.show()
cv2.waitKey(0)     


text = pytesseract.image_to_string(img)
print("Extracted Text:")
print(text)