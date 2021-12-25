import pyautogui
import time
xpos=[1330,20,24,71]
ypos=[11,748,700,622]
n=[10,10,5,5]
#time.sleep(10)
#print(pyautogui.position())
while True:
    h=int(input("\n\n(Enter q to exit this program)\n To shut down your computer enter time in hours:  "))
    m=int(input("\n To shut down your computer enter time in minutes:  "))
    s=int(input("\n To shut down your computer enter time in seconds:  "))
    t=h*3600+m*60+s
    try:
        x=float(t)
        time.sleep(x)
        for item in range(0,3):
            pyautogui.moveTo(xpos[item],ypos[item],duration=2,tween=pyautogui.linear)
            pyautogui.click(interval=n[item])
        pyautogui.click()
        time.sleep("10")
        break

    except:
        if t=="Q" or t=="q":
            break
        else:
            continue