import pyautogui,time

n=int(input("PLEASE ENTER THE VALUE OF N-->"))

pyautogui.sleep(1)

pyautogui.click(1253,20)
pyautogui.sleep(2)


for a in range(n-1):
    pyautogui.rightClick(180,220)
    pyautogui.sleep(.8)
    pyautogui.click(347, 548)
    pyautogui.sleep(.8)
    pyautogui.click(596, 315)
    pyautogui.sleep(.8)
    pyautogui.doubleClick(180, 220)
    pyautogui.sleep(.8)



