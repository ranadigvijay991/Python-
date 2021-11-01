import pyautogui
import time

msg = "F"
n=500
print("START")
count=5
while(count!=0):
    time.sleep(1)
    count -= 1
print("Complete")
for i in range(0,int(n)):
    pyautogui.typewrite(msg+"\n")