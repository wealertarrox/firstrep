import time
import os
n=0
hour=0
min=0
sec=0
hour_1="0"
min_1="0"
sec_1="0"
while n<10000:
    d=print("0"+str(hour)+":"+min_1+str(min)+":"+sec_1+str(sec))
    time.sleep(0)
    sec+=1
    if sec==60:
        sec=0
        min+=1
    if min==60:
        min=0
        hour+=1
    if hour==24:
        hour=0
    if sec>9:
        sec_1=""
    if min>9:
        min_1 = ""
    if hour>9:
        hour_1=""
    if sec < 9:
        sec_1 = "0"
    if min < 9:
        min_1 = "0"
    if hour < 9:
        hour_1 = "0"
    clear = lambda: os.system('cls')
    clear()