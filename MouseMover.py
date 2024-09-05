import pyautogui as pag
import random
import time
import keyboard

print("Press F to exit")

w_press_count = 0  # Initialize count for 'w' presses

while True:
    if keyboard.is_pressed('f'):
        print("Exiting")
        break
    
    # Move the mouse randomly
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, 0.5)
    
    # Sleep for random time
    time.sleep(random.uniform(0.5, 5))  # Use uniform for float values
    
    # Press 'w' and increment the count
    keyboard.press_and_release('w')
    w_press_count += 1
    
    if w_press_count == 3:  # Check if 'w' has been pressed 3 times
        print("Waiting for 3 seconds after pressing 'w' three times.")
        time.sleep(3)
        w_press_count = 0  # Reset the count


  
  
  