# This is a sample Python script.
import time

import numpy as np
from PIL import ImageGrab
from easyocr import easyocr
from pytesseract import pytesseract


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
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


if __name__ == '__main__':
    print_hi('PyCharm')
    # Define the region of interest (ROI) on the screen
    time.sleep(1)
    text = read_text_from_section(1276, 931, 235, 81)
    print("Extracted Text:", text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
