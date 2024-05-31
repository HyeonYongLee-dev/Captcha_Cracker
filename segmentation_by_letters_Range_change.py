import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from datetime import datetime
import os
import shutil

#학습 데이터 절대경로 가져오기
today = datetime.now().strftime('%Y%m%d')
masked_path = "C:\\TEMP\\" + today + "\\" + "masked\\"

file_list = [file_name for file_name in os.listdir(masked_path) if os.path.isfile(os.path.join(masked_path, file_name))]


#각 이미지를 저장할 폴더 생성(0 ~ 9)
for i in range(10):
    classified_Number_Folder = masked_path + f"{i}"
    os.makedirs(classified_Number_Folder, exist_ok=True)


file_count = 0

for file_name in file_list:
    
    img = cv2.imread(masked_path + file_name, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    
    # 바이너리 이미지로 변환
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

     # 윤곽선 검출
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        # 윤곽선을 기준으로 숫자 영역 추출 및 저장
    digit_images = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        digit_image = img[y:y+h, x:x+w]
        digit_images.append((x, digit_image))
    
        
    # 왼쪽에서 오른쪽 순으로 정렬
    digit_images.sort(key=lambda x: x[0])
    
    for idx, (x, digit_image) in enumerate(digit_images):
            plt.imshow(digit_image)
            plt.axis('off')
            plt.show()

    
    
    '''    
    x, y, w, h = 2, 0 , 20, 47
    for i in range(6):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped_img = img[y:y+h, x:x+w]
        tempname = file_name.split(".")[0]
        save_path = f"C:\\TEMP\\{tempname}_{i}.jpg"
        cv2.imwrite(save_path, cropped_img)
        x += w
    
    
    #파일 이동
    _1st_letter = file_name[0:1]
    _2nd_letter = file_name[1:2]
    _3rd_letter = file_name[2:3]
    _4th_letter = file_name[3:4]
    _5th_letter = file_name[4:5]
    _6th_letter = file_name[5:6]
    
    
    src_file = "C:\\TEMP\\" + file_name.split(".")[0] + "_0.jpg"
    img1_dir = _1st_letter + "\\"
    dst_file = masked_path + img1_dir + file_name.split(".")[0] + "_0.jpg"
    shutil.move(src_file , dst_file)
    
    src_file = "C:\\TEMP\\" + file_name.split(".")[0] + "_1.jpg"
    img2_dir = _2nd_letter + "\\"
    dst_file = masked_path + img2_dir + file_name.split(".")[0] + "_1.jpg"
    shutil.move(src_file , dst_file)
    
    src_file = "C:\\TEMP\\" + file_name.split(".")[0] + "_2.jpg"
    img3_dir = _3rd_letter + "\\"
    dst_file = masked_path + img3_dir + file_name.split(".")[0] + "_2.jpg"
    shutil.move(src_file , dst_file)

    src_file = "C:\\TEMP\\" + file_name.split(".")[0] + "_3.jpg"
    img4_dir = _4th_letter + "\\"
    dst_file = masked_path + img4_dir + file_name.split(".")[0] + "_3.jpg"
    shutil.move(src_file , dst_file)

    src_file = "C:\\TEMP\\" + file_name.split(".")[0] + "_4.jpg"
    img5_dir = _5th_letter + "\\"
    dst_file = masked_path + img5_dir + file_name.split(".")[0] + "_4.jpg"
    shutil.move(src_file , dst_file)

    src_file = "C:\\TEMP\\" + file_name.split(".")[0] + "_5.jpg"
    img6_dir = _6th_letter + "\\"
    dst_file = masked_path + img6_dir + file_name.split(".")[0] + "_5.jpg"
    shutil.move(src_file , dst_file)

    
    #captcha 파일 삭제
    os.remove(masked_path + file_name)
    
    #다음 파일 작업을 위한 Count 증가
    file_count += 1    



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
    
  
plt.title("threshold")
plt.show()

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

plt.title("dilation")
plt.show()


erosion = cv2.erode(dilation, kernel, iterations=1)
erosion2 = cv2.erode(dilation2, kernel, iterations=1)
erosion3 = cv2.erode(dilation3, kernel, iterations=1)

titles3 = ['original', 'adaptive', 'otsu', 'gaussian + otsu']
images3 = [img, erosion, erosion2, erosion3]


for i in range (4):
    plt.subplot(2, 2, i + 1), plt.imshow(images3[i], 'gray')
    plt.title(titles3[i])
    plt.xticks([]), plt.yticks([])

plt.title("erosion")
plt.show()


x, y, w, h = 11, 1 , 26, 47
for i in range(6):
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped_img = img[y:y+h, x:x+w]
    save_path = f"C:\\TEMP\\slice\\{i}.jpg"
    cv2.imwrite(save_path, cropped_img)
    x += w
    
for i in range (4):
    plt.subplot(2, 2, i + 1), plt.imshow(images2[i], 'gray')
    plt.title(titles2[i])
    plt.xticks([]), plt.yticks([])
    
plt.title("contouring")
plt.show()


'''