import time

import pyautogui

# Locate the image on the screen
time.sleep(5)
box = pyautogui.locateOnScreen('image.png')  # Replace 'image.png' with your image file


if box is not None:
    x, y, width, height = box
    print(f"x: {x}, y: {y}, width: {width}, height: {height}")
else:
    print("Image not found on the screen.")
