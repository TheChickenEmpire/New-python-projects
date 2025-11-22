import mouse, keyboard, time
def left_click():
    mouse.click(mouse.LEFT)
def right_click():
    mouse.click(mouse.RIGHT)
while True:
    if keyboard.read_key()==",":
        left_click()
    if keyboard.read_key()==".":
        right_click()
    time.sleep(0.0001)
    if keyboard.read_key()=="delete":
        break
# run this program a lot of times in one
# instance of the time for even faster clicking 6 times for best results