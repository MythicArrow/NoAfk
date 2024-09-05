import pyautogui as pag
import random
import time
import keyboard
import tkinter as tk
from threading import Thread

# Function to handle No-AFK behavior
def no_afk():
    key_press_count = 0
    keys = ['w', 'a', 's', 'd']  # List of keys to press
    
    while not stop:
        if keyboard.is_pressed('f'):
            print("Exiting")
            break
        
        # Move the mouse randomly
        x = random.randint(600, 700)
        y = random.randint(200, 600)
        pag.moveTo(x, y, 0.5)
        
        # Sleep for random time
        time.sleep(random.uniform(0.5, 5))
        
        # Press a random key from the list
        random_key = random.choice(keys)
        keyboard.press_and_release(random_key)
        key_press_count += 1
        
        if key_press_count == 3:
            time.sleep(3)
            key_press_count = 0

# Tkinter window
def start_no_afk():
    global stop
    stop = False
    thread = Thread(target=no_afk)
    thread.start()

def stop_no_afk():
    global stop
    stop = True

# Create Tkinter window
root = tk.Tk()
root.title("No AFK Tool")

# Start button
start_button = tk.Button(root, text="Start", command=start_no_afk)
start_button.pack(pady=10)

# Stop button
stop_button = tk.Button(root, text="Stop", command=stop_no_afk)
stop_button.pack(pady=10)

root.mainloop()


  
  
  