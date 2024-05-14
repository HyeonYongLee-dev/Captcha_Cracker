import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils
import zipfile
from PIL import Image

img = cv2.imread("C:\\TEMP\\20240509\\masked\\990024.jpg", 0)
#plt.imshow(img, 'gray')


#pixel에서 불필요한 음영을 제거(adaptive threshold)
th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 2)

#pixel의 threshold값을 계산하여 pixel의 음영 level을 확인
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#plots
titles = ['original', 'adaptive', 'otsu', 'gaussian + otsu']
images = [img, th, th2, th3]

for i in range (4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
'''   
plt.title("threshold")
plt.show()
'''
#remove noise/line

#kernel = np.ones((3,3), np.uint8)
kernel = np.ones((3,3), np.uint8)
dilation = cv2.dilate(th, kernel, iterations=1)
dilation2 = cv2.dilate(th2, kernel, iterations=1)
dilation3 = cv2.dilate(th3, kernel, iterations=1)

titles2 = ['original', 'adaptive', 'otsu', 'gaussian + otsu']
images2 = [img, dilation, dilation2, dilation3]

for i in range (4):
    plt.subplot(2, 2, i + 1), plt.imshow(images2[i], 'gray')
    plt.title(titles2[i])
    plt.xticks([]), plt.yticks([])
'''    
plt.title("dilation")
plt.show()
'''

erosion = cv2.erode(dilation, kernel, iterations=1)
erosion2 = cv2.erode(dilation2, kernel, iterations=1)
erosion3 = cv2.erode(dilation3, kernel, iterations=1)

titles3 = ['original', 'adaptive', 'otsu', 'gaussian + otsu']
images3 = [img, erosion, erosion2, erosion3]


for i in range (4):
    plt.subplot(2, 2, i + 1), plt.imshow(images3[i], 'gray')
    plt.title(titles3[i])
    plt.xticks([]), plt.yticks([])
'''
plt.title("erosion")
plt.show()
'''

x, y, w, h = 11, 1 , 26, 47
for i in range(6):
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped_img = img[y:y+h, x:x+w]
    save_path = f"C:\\TEMP\\slice\\{i}.jpg"
    cv2.imwrite(save_path, cropped_img)

    cv2.rectangle(dilation, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.rectangle(dilation2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.rectangle(dilation3, (x, y), (x + w, y + h), (0, 255, 0), 2)
    x += w
    
for i in range (4):
    plt.subplot(2, 2, i + 1), plt.imshow(images2[i], 'gray')
    plt.title(titles2[i])
    plt.xticks([]), plt.yticks([])
    
plt.title("contouring")
plt.show()


