import os
from datetime import datetime
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time







def capture_screenshot(i):
    # 오늘 날짜 객체 생성
    today = datetime.now().strftime('%Y%m%d') #오늘 날짜 "yyyyMMdd"
    destination_path = os.path.join("C:\\TEMP", today, "Training_Data")

    # 폴더 생성
    os.makedirs(destination_path, exist_ok=True)
    
    # Captcha 영역을 캡쳐
    region = ((800, 432, 220, 43))
    screenshot = pyautogui.screenshot(region=region)
    
    # 캡쳐한 이미지를 파일로 저장
    screenshot_path = os.path.join(destination_path, f"captcha_{i}.jpg")
    screenshot.save(screenshot_path)

    return screenshot_path





###############################################################
#캡쳐 시작




##크롬 드라이버 경로 지정
##크롬 드라이버 버전: 116.0.5845
CHROMEDRIVER_PATH = os.path.join("C:\\TEMP", "Chrome_Driver", "chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# 서비스 설정
service = Service(executable_path=CHROMEDRIVER_PATH)

# 드라이버 실행
driver = webdriver.Chrome(service=service, options=options)

##웹사이트 open
url = 'https://seller.kshop.co.kr/jwork/authentication/loginForm.do'
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.implicitly_wait(20)


#학습을 위해 캡쳐할 파일의 갯수 지정
Captcha_files = 600

for i in range(Captcha_files):
    capture_screenshot(i)
    driver.refresh()
    
driver.close()