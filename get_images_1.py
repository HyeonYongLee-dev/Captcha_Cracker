import os
import urllib.request
from datetime import datetime


#오늘 날짜 객체 생성
today = datetime.now().strftime('%Y%m%d')

default_path = "C:\\python\\"
destination_path = "C:\\TEMP\\" + today + "\\"

# 폴더 생성
os.makedirs(destination_path, exist_ok=True)



for i in range(10):
    image_url = "https://seller.kshop.co.kr/jwork/authentication/viewCaptcha.do?W=263&H=54&F=50"
    file_name = "{:02d}.jpg".format(i + 1)
    final_path = destination_path + file_name
    urllib.request.urlretrieve(image_url, final_path)
    print(f"다운로드 완료: {final_path}")