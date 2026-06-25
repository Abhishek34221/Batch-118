from datetime import datetime
import time

# current = datetime.today()
# print(current)


# current = datetime.now().strftime("%A %d-%m-%y %H:%M:%S")
# print(current)

import pyautogui
import time
time.sleep(4)
for i in range(10):
    pyautogui.typewrite("Hello how are", interval=0.05)