from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



while keyboard.is_pressed('q') == False: #for stop bot press 'q'

    pic = pyautogui.screenshot(region=(660,350,600,400))

    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):
            #Color of center: r,g,b(255, 219, 195)
            r,g,b = pic.getpixel((x,y)) # r=red, g=green, b=blue

            if b == 195:
                click(x+660,y+350)
                time.sleep(0.05)
                break
