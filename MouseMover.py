import pyautogui as pag
import random
import time
import keyboard
print("Press F for exitting")

while True:
  if keyboard.is_pressed('f'):
    print("Exitting ")
    break
  x = random.randint(600,700)
  y = random.randint(200,600)
  pag.moveTo(x,y,0.5)
  time.sleep(random.randint(0.5,5))
  
  
  
  