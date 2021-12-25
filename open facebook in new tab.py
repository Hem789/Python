import pyautogui
import PIL
import time
import keyboard
time.sleep(1)
#x,y=pyautogui.position()
#print(x,"\n",y)
i=0
xPos=[250,865,862,835,889,1311,1128]
yPos=[51,242,299,307,377,95,478]
inter=[20,20,2,1,2,20,10,0]
time.sleep(10)
print(pyautogui.position())
#moveDuration=[


for donkey in range(1,12):
    if donkey==4:
        pyautogui.write("aw3some.evil00@gmail.com",interval=0.25)
        continue
    elif donkey==2:
        pyautogui.hotkey('ctrl','a')
        time.sleep(1)
        pyautogui.write("https://www.facebook.com/?stype=lo&jlou=AfdC5Cy4SpO8LfiqVIl8dd8aOWnURqEdbJNOomO0Jg23Rh0XP7Hp3KMJPLfH3PhPeDG7HG0dWAr5aIfaL1stYcRL0E2PsT7sz8TvQusKNv3c1g&smuh=63645&lh=Ac8FCTZF3UR-GxB7b7I",interval=0.1)
        time.sleep(1)
        pyautogui.press('enter')    
    elif donkey==7:
        pyautogui.write("hem123",interval=0.25)
        continue
    elif keyboard.is_pressed('x'):
        print("x has been pressed")
        break
    else:
        pyautogui.moveTo(xPos[i],yPos[i],duration=2,tween=pyautogui.linear)
        #x,y=pyautogui.position()
        #print()
        pyautogui.click(interval=inter[i])
        i+=1
        
        
        
"""        pyautogui.moveTo(268,16, duration=1, tween=pyautogui.easeInQuad)aw3com
pyautogui.click()
time.sleep(25)
pyautogui.moveTo(509,507,duration=2,tween=pyautogui.linear)hem123
pyautogui.click()
#time.sleep(20)some.evi
pyautogui.moveTo(865,242,duration=2,tween=pyautogui.linear)
pyautogui.click(interval=10)l00@gmail.
#time.sleep(2)
pyautogui.write("aw3some.evil00@gmail.com",interval=.5)
#pyautogui.click(862,299,interval=10)
time.sleep(1)
pyautogui.click(835,307)
time.sleep(1)
pyautogui.write("hem123",interval=0.5)
time.sleep(2)
pyautogui.click(889,377,interval=20)
pyautogui.moveTo(1311,95,duration=1,tween=pyautogui.easeInOutQuad)
pyautogui.click(interval=10)
pyautogui.moveTo(1128,474)
pyautogui.click()"""