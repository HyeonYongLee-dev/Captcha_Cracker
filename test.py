import cv2
import joblib
from skimage.feature import hog
import numpy as np
from matplotlib import pyplot as plt 
 
 
# Read the input image 
im = cv2.imread("C:\\TEMP\\20240516\\run_model\\masked\\captcha.png")
 
# Convert to grayscale and apply Gaussian filtering
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
 
#가우시안 블러를 통해 noise 제거
#im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)
 
# Threshold the image(이미지 이진화)
ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)

# Find contours in the image(윤곽선 찾기)
ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
# Get rectangles contains each contour
rects = [cv2.boundingRect(ctr) for ctr in ctrs]
 
# For each rectangular region
for rect in rects:
    # Draw the rectangles
    cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3) 
    # Make the rectangular region around the digit
    leng = int(rect[3] * 1.6)
    pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
    pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
    roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
    if roi.size <= 0:
        continue
 
    # Resize the image
    roi = cv2.resize(roi, (8, 8), interpolation=cv2.INTER_AREA)
    roi = cv2.dilate(roi, (3, 3))
 
cv2.imshow("Resulting Image with Rectangular ROIs", im)
cv2.waitKey()