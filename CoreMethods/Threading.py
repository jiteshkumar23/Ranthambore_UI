import os
import keyboard
import threading
import time
from CoreMethods.CoreMethods import (debounce_key, setImagePath, formFill)
import numpy as np
from PIL import ImageGrab
from easyocr import easyocr
from pytesseract import pytesseract

global text


def exit_program():
    print("r+4 keys pressed - Exiting... Goodbye!")
    os._exit(0)  # Exit the current process


# Function to be run in a new thread
def background_task():
    global text
    text = read_text_from_section(1276, 931, 235, 81)


def main():
    setImagePath()
    print("Press - r+1 - For filling FORM only")
    print("Press - r+4 - For exiting the script")

    # Add listener
    keyboard.add_hotkey('r+4', exit_program)

    # Start the background task in a new thread
    bg_thread = threading.Thread(target=background_task)
    bg_thread.start()

    while True:
        if keyboard.is_pressed("r+1"):
            print("Keys Pressed - r+1 - Filling FORM only")
            formFill()
            autoit.send(text)
            debounce_key("r+1")  # Wait until the key is released


def read_text_from_section(x, y, width, height):
    # Capture the screenshot of the specified region
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    # Convert the screenshot to a numpy array
    screenshot_np = np.array(screenshot)

    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Read text from the numpy array screenshot
    result = reader.readtext(screenshot_np)

    # Extract text from result
    extracted_text = " ".join([text[1] for text in result])
    return extracted_text


if __name__ == "__main__":
    main()