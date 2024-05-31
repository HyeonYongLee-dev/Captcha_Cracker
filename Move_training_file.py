import os
from datetime import datetime
import shutil


today = datetime.now().strftime('%Y%m%d')
defalut_dir = "C:\\TEMP\\" + today + "\\" + "run_model\\"
desti_dir = "D:\\업무\\trainingset\\"


for i in range (10):
    each_dir = defalut_dir + str(i)
    os.listdir(each_dir)
    