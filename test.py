import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()  # 현재 마우스 좌표를 가져옵니다
        print(f"Mouse position: ({x}, {y})")
        time.sleep(1)  # 1초마다 좌표를 출력합니다
except KeyboardInterrupt:
    print("Exiting...")