import os
import time
present = 0
while True:
    os.system('cls')
    if present == 10:
        present = 0
    frame = open(str(present)+".txt", "r").read()
    print(frame)
    present = present + 1
    time.sleep(0.1)