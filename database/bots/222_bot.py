import os
import subprocess
import time
while True:
    print(500)
# shell_process = subprocess.Popen(('python.exe', "", "D:/test2.py"), shell=True)
# time.sleep(1)
os.system("taskkill  /F /pid "+str(9792))

