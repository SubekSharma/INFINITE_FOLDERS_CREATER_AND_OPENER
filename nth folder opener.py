import pyautogui,time

n=int(input("PLEASE ENTER THE VALUE OF N CORRESPONDING TO THE FOLDER YOU WISH TO OPEN-->"))

pyautogui.click(1253,20)
pyautogui.sleep(1)


for a in range(n-1):
    pyautogui.click(180,220)
    pyautogui.press('enter')
    pyautogui.sleep(.3)

