from PIL import Image
from datetime import datetime
import os
import shutil

#학습 데이터 절대경로 가져오기
today = datetime.now().strftime('%Y%m%d')
masked_path = "C:\\TEMP\\" + today + "\\" + "masked\\"

file_list = [file_name for file_name in os.listdir(masked_path) if os.path.isfile(os.path.join(masked_path, file_name))]






img = Image.open(masked_path + 'captcha.png')
width, height = img.size
box = (11, 6, 160, 54) #(left, upper, right, lower)
cropped_image = img.crop(box)
cropped_image.save(masked_path + "captcha_sliced.jpg")





'''
#각 이미지를 저장할 폴더 생성(0 ~ 9)
for i in range(10):
    classified_Number_Folder = masked_path + f"{i}"
    os.makedirs(classified_Number_Folder, exist_ok=True)






file_count = 0
new_width = 33


for file_name in file_list:
    
    img = Image.open(masked_path + file_name)
    width, height = img.size

    #1번
    box = (11, 6, 44, 54) #(left, upper, right, lower)
    cropped_image = img.crop(box)
    cropped_image.save(masked_path + file_name.split(".")[0] + "_0.jpg")
    
    img1 = Image.open(masked_path + file_name.split(".")[0] + "_0.jpg")
    
    resized_image = img1.resize((new_width, 48), Image.BICUBIC)
    resized_image.save(masked_path + file_name.split(".")[0] + "_0.jpg")
    

   
    
    #2번
    box = (45, 6, 71, 54) #(left, upper, right, lower)
    cropped_image = img.crop(box)
    cropped_image.save(masked_path + file_name.split(".")[0] + "_1.jpg")
    
    img2 = Image.open(masked_path + file_name.split(".")[0] + "_1.jpg")
    
    resized_image = img2.resize((new_width, 48), Image.BICUBIC)
    resized_image.save(masked_path + file_name.split(".")[0] + "_1.jpg")
    

    #3번
    box = (72, 6, 87, 54) #(left, upper, right, lower)
    cropped_image = img.crop(box)
    cropped_image.save(masked_path + file_name.split(".")[0] + "_2.jpg")
    
    img3 = Image.open(masked_path + file_name.split(".")[0] + "_2.jpg")

    resized_image = img3.resize((new_width, 48), Image.BICUBIC)
    resized_image.save(masked_path + file_name.split(".")[0] + "_2.jpg")
    

    #4번
    box = (88, 6, 101, 54) #(left, upper, right, lower)
    cropped_image = img.crop(box)
    cropped_image.save(masked_path + file_name.split(".")[0] + "_3.jpg")
    
    img4 = Image.open(masked_path + file_name.split(".")[0] + "_3.jpg")

    resized_image = img4.resize((new_width, 48), Image.BICUBIC)
    resized_image.save(masked_path + file_name.split(".")[0] + "_3.jpg")
    
    
    #5번
    box = (102, 6, 124, 54) #(left, upper, right, lower)
    cropped_image = img.crop(box)
    cropped_image.save(masked_path + file_name.split(".")[0] + "_4.jpg")
    
    img5 = Image.open(masked_path + file_name.split(".")[0] + "_4.jpg")
    
    resized_image = img5.resize((new_width, 48), Image.BICUBIC)
    resized_image.save(masked_path + file_name.split(".")[0] + "_4.jpg")
    


    #6번
    box = (125, 6, 148, 54) #(left, upper, right, lower)
    cropped_image = img.crop(box)
    cropped_image.save(masked_path + file_name.split(".")[0] + "_5.jpg")
    
    img6 = Image.open(masked_path + file_name.split(".")[0] + "_5.jpg")
    
    resized_image = img6.resize((new_width, 48), Image.BICUBIC)
    resized_image.save(masked_path + file_name.split(".")[0] + "_5.jpg")
   
    
    
    #파일 이동
    _1st_letter = file_name[0:1]
    _2nd_letter = file_name[1:2]
    _3rd_letter = file_name[2:3]
    _4th_letter = file_name[3:4]
    _5th_letter = file_name[4:5]
    _6th_letter = file_name[5:6]
    
    
    src_file = masked_path + file_name.split(".")[0] + "_0.jpg"
    img1_dir = _1st_letter + "\\"
    dst_file = masked_path + img1_dir + file_name.split(".")[0] + "_0.jpg"
    shutil.move(src_file , dst_file)
    
    src_file = masked_path + file_name.split(".")[0] + "_1.jpg"
    img2_dir = _2nd_letter + "\\"
    dst_file = masked_path + img2_dir + file_name.split(".")[0] + "_1.jpg"
    shutil.move(src_file , dst_file)
    
    src_file = masked_path + file_name.split(".")[0] + "_2.jpg"
    img3_dir = _3rd_letter + "\\"
    dst_file = masked_path + img3_dir + file_name.split(".")[0] + "_2.jpg"
    shutil.move(src_file , dst_file)

    src_file = masked_path + file_name.split(".")[0] + "_3.jpg"
    img4_dir = _4th_letter + "\\"
    dst_file = masked_path + img4_dir + file_name.split(".")[0] + "_3.jpg"
    shutil.move(src_file , dst_file)

    src_file = masked_path + file_name.split(".")[0] + "_4.jpg"
    img5_dir = _5th_letter + "\\"
    dst_file = masked_path + img5_dir + file_name.split(".")[0] + "_4.jpg"
    shutil.move(src_file , dst_file)

    src_file = masked_path + file_name.split(".")[0] + "_5.jpg"
    img6_dir = _6th_letter + "\\"
    dst_file = masked_path + img6_dir + file_name.split(".")[0] + "_5.jpg"
    shutil.move(src_file , dst_file)

    
    #captcha 파일 삭제
    os.remove(masked_path + file_name)
    
    #다음 파일 작업을 위한 Count 증가
    file_count += 1
'''    