import subprocess
import time


for i in range(10,0,-1):
    print(i)
    time.sleep(1)
subprocess.Popen(["start","alarm.wav"],shell=True)