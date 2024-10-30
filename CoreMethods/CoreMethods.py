import datetime
import os
import random
import string
import time
import tkinter as tk
from datetime import datetime
from tkinter import simpledialog
import cv2
import keyboard
import numpy as np
import pyautogui
from autoit import autoit
import datetime

from config import delay_correct, delay_error, paxOfPerson1, machine, nameOfPerson1, mobileOfPerson1, \
    idTypeOfPerson1, idNumberOfPerson1, genderOfPerson1, paxOfPerson2, nameOfPerson2, mobileOfPerson2, idTypeOfPerson2, \
    idNumberOfPerson2, genderOfPerson2, paxOfPerson3, nameOfPerson3, mobileOfPerson3, idTypeOfPerson3, \
    idNumberOfPerson3, genderOfPerson3, paxOfPerson4, nameOfPerson4, mobileOfPerson4, idTypeOfPerson4, \
    idNumberOfPerson4, genderOfPerson4, paxOfPerson5, nameOfPerson5, mobileOfPerson5, idTypeOfPerson5, \
    idNumberOfPerson5, genderOfPerson5, paxOfPerson6, nameOfPerson6, mobileOfPerson6, idTypeOfPerson6, \
    idNumberOfPerson6, genderOfPerson6, paxOfPerson7, nameOfPerson7, mobileOfPerson7, idTypeOfPerson7, \
    idNumberOfPerson7, genderOfPerson7, paxOfPerson8, nameOfPerson8, mobileOfPerson8, idTypeOfPerson8, \
    idNumberOfPerson8, genderOfPerson8, paxOfPerson9, nameOfPerson9, mobileOfPerson9, idTypeOfPerson9, \
    idNumberOfPerson9, genderOfPerson9, paxOfPerson10, nameOfPerson10, mobileOfPerson10, idTypeOfPerson10, \
    idNumberOfPerson10, genderOfPerson10, genderOfPerson20, idNumberOfPerson20, idTypeOfPerson20, mobileOfPerson20, \
    nameOfPerson20, paxOfPerson20, genderOfPerson19, idNumberOfPerson19, idTypeOfPerson19, mobileOfPerson19, \
    nameOfPerson19, paxOfPerson19, genderOfPerson18, idNumberOfPerson18, idTypeOfPerson18, mobileOfPerson18, \
    nameOfPerson18, paxOfPerson18, genderOfPerson17, idNumberOfPerson17, idTypeOfPerson17, mobileOfPerson17, \
    nameOfPerson17, paxOfPerson17, genderOfPerson16, idNumberOfPerson16, idTypeOfPerson16, mobileOfPerson16, \
    nameOfPerson16, paxOfPerson16, genderOfPerson15, idNumberOfPerson15, idTypeOfPerson15, mobileOfPerson15, \
    nameOfPerson15, paxOfPerson15, genderOfPerson14, idNumberOfPerson14, idTypeOfPerson14, mobileOfPerson14, \
    nameOfPerson14, paxOfPerson14, genderOfPerson13, idNumberOfPerson13, idTypeOfPerson13, mobileOfPerson13, \
    nameOfPerson13, paxOfPerson13, genderOfPerson12, idNumberOfPerson12, idTypeOfPerson12, mobileOfPerson12, \
    nameOfPerson12, paxOfPerson12, genderOfPerson11, idNumberOfPerson11, idTypeOfPerson11, mobileOfPerson11, \
    nameOfPerson11, paxOfPerson11, countOfPersons, speed, timer, Person1AttachmentName

global image_directory, RanthamboreTigerReserve_image_path, selectTouristType_image_path, agreeToCancellation_image_path, \
    agreeToTermsConditions_image_path, MemberDetails_image_path, UploadDocument_image_path

timeStart1, timeEnd1, timer1 = '0:0:0.0', '0:0:0.0', timer
timeStart2, timeEnd2, timer2 = '0:0:0.0', '0:0:0.0', timer
timeStart3, timeEnd3, timer3 = '0:0:0.0', '0:0:0.0', timer
timeStart4, timeEnd4, timer4 = '0:0:0.0', '0:0:0.0', timer
timeStart5, timeEnd5, timer5 = '0:0:0.0', '0:0:0.0', timer
timeStart6, timeEnd6, timer6 = '0:0:0.0', '0:0:0.0', timer
timeStart7, timeEnd7, timer7 = '0:0:0.0', '0:0:0.0', timer
timeStart8, timeEnd8, timer8 = '0:0:0.0', '0:0:0.0', timer
timeStart9, timeEnd9, timer9 = '0:0:0.0', '0:0:0.0', timer
timeStart10, timeEnd10, timer10 = '0:0:0.0', '0:0:0.0', timer
timeStart11, timeEnd11, timer11 = '0:0:0.0', '0:0:0.0', timer
timeStart12, timeEnd12, timer12 = '0:0:0.0', '0:0:0.0', timer
timeStart13, timeEnd13, timer13 = '0:0:0.0', '0:0:0.0', timer
timeStart14, timeEnd14, timer14 = '0:0:0.0', '0:0:0.0', timer
timeStart15, timeEnd15, timer15 = '0:0:0.0', '0:0:0.0', timer
timeStart16, timeEnd16, timer16 = '0:0:0.0', '0:0:0.0', timer
timeStart17, timeEnd17, timer17 = '0:0:0.0', '0:0:0.0', timer
timeStart18, timeEnd18, timer18 = '0:0:0.0', '0:0:0.0', timer
timeStart19, timeEnd19, timer19 = '0:0:0.0', '0:0:0.0', timer
timeStart20, timeEnd20, timer20 = '0:0:0.0', '0:0:0.0', timer


def printDateTime():
    print(f"Time: {datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]}")


def getDateTime():
    return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]


def getTimeDiff(timeStart2, timeStart):
    # Calculate the difference
    fmt = "%H:%M:%S.%f"
    start_dt = datetime.datetime.strptime(timeStart, fmt)
    end_dt = datetime.datetime.strptime(timeStart2, fmt)
    diff = end_dt - start_dt
    print("Difference is : ", diff)
    return diff


def multiplePressUsingPyAutoGUI(key, times):
    print("pressing " + " " + key + " " + str(times))
    pyautogui.press(key, presses=times)


def speed_for_first_page(speed):
    time.sleep(speed)


def wait_for_image1_or_image2_and_click(image_path, image_path2, timeout_duration=60, check_interval=0.001):
    timeout_end = time.time() + timeout_duration

    print(f"Waiting for {image_path} to appear on the screen...")

    while time.time() < timeout_end:
        try:
            # Locate the image on the screen
            location = pyautogui.locateCenterOnScreen(image_path, grayscale=True)

            # If the image is found, click on it and break the loop
            if location is not None:
                print(f"Image found at {location}, clicking on it...")
                pyautogui.click(location)
                break
        except pyautogui.ImageNotFoundException:
            # Handle the case where the image is not found
            print(f"Image not found: {image_path}")
            try:
                location = pyautogui.locateCenterOnScreen(image_path2, grayscale=True)
                if location is not None:
                    print(f"Image found at {location}, clicking on it...")
                    pyautogui.click(location)
                    break
            except pyautogui.ImageNotFoundException:
                print(f"Image not found: {image_path2}")

        # Wait for the specified interval before checking again
        time.sleep(check_interval)
    else:
        print("Timeout reached. Image not found.")

    print("Task completed.")
    return location


def wait_for_image_and_click(image_path, timeout_duration=60, check_interval=0.001):
    timeout_end = time.time() + timeout_duration

    print(f"Waiting for {image_path} to appear on the screen...")

    while time.time() < timeout_end:
        try:
            # Locate the image on the screen
            location = pyautogui.locateCenterOnScreen(image_path, grayscale=True)

            # If the image is found, click on it and break the loop
            if location is not None:
                print(f"Image found at {location}, clicking on it...")
                pyautogui.click(location)
                break
        except pyautogui.ImageNotFoundException:
            # Handle the case where the image is not found
            print(f"Image not found: {image_path}")

        # Wait for the specified interval before checking again
        time.sleep(check_interval)
    else:
        print("Timeout reached. Image not found.")

    print("Task completed.")
    return location


def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    user_input = None

    while user_input != "1":
        user_input = simpledialog.askstring("Input", "Enter 1 to continue:")
        if user_input is None:  # User closed the dialog
            print("User cancelled the input.")
            root.destroy()
            exit()

    root.destroy()  # Close the popup


def click_on_image_in_region(left, top, width, height, image):
    time.sleep(1)
    # Define the region of interest (left, top, width, height)
    region = (left, top, width, height)
    # Print debug information
    print(f"Capturing screenshot of region: {region}")

    # Capture a screenshot of the region
    screenshot = pyautogui.screenshot(region=region)

    # Print debug information
    print("Searching for image 'indian_flag.png' within the captured region...")

    try:
        # Locate the image 'indian_flag.png' within the specified region on the screen
        image_location = pyautogui.locateOnScreen(image, region=region)

        if image_location is not None:
            # Click in the center of the image location
            center = pyautogui.center(image_location)
            pyautogui.click(center)
            print("Image found and clicked.")
        else:
            print("Image not found in the specified region.")
    except pyautogui.ImageNotFoundException:
        print("Image not found on the screen.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def human_typing(text):
    for char in text:
        autoit.send(char)
        time.sleep(delay_correct)


def human_typing_age(text):
    for char in text:
        autoit.send(char)
        time.sleep(delay_correct + 0.1)


def autoit_slow_type_with_error(text):
    # Choose a random position to make a typing error
    error_position = random.randint(0, len(text) - 1)
    # Choose a random alphabet as the incorrect character
    wrong_character = random.choice(string.ascii_lowercase)

    for i, character in enumerate(text):
        if i == error_position:
            # Type the wrong random character
            autoit.send(wrong_character)
            # Backspace to delete the wrong character
            time.sleep(delay_error)
            autoit.send("{BACKSPACE}")
            time.sleep(delay_correct)
        # Type the correct character
        autoit.send(character)
        time.sleep(delay_correct)


def autoit_slow_type_numbers_with_error(numbers):
    if not numbers:  # Check if numbers is None or empty
        return
    # Choose a random position to make a typing error
    error_position = random.randint(0, len(numbers) - 1)
    # Choose a random digit as the incorrect character
    wrong_character = random.choice(string.digits)

    for i, character in enumerate(numbers):
        if i == error_position:
            # Type the wrong random character
            autoit.send(wrong_character)
            # Backspace to delete the wrong character
            time.sleep(delay_error)
            autoit.send("{BACKSPACE}")
            time.sleep(delay_correct)
            # Additional delay for the correction
        # Type the correct character
        autoit.send(character)
        time.sleep(delay_correct)


def custom_hotkey():
    # Define your desired hotkey combination
    return keyboard.is_pressed("ctrl+alt+x")  # Example: Ctrl+Alt+X


def debounce_key(key):
    # Wait for key release
    while keyboard.is_pressed(key):
        pass


def formFill():
    print("Execution Started At: ", getDateTime())
    persons_list = get_persons_list()
    for i in range(int(countOfPersons)):
        person = persons_list[i]
        pyautogui.press('pageup')
        pyautogui.click(find_image_on_screen_using_opencv(MemberDetails_image_path, 600))
        #Set time Start here
        setTimeStart(i)
        speed_for_first_page(speed)
        autoit.send("{TAB}")
        time.sleep(0.1)
        speed_for_first_page(speed)
        print(person['pax'])
        selectPaxDropdown(person['pax'])
        autoit.send("{TAB}")
        speed_for_first_page(speed)
        autoit_slow_type_with_error(person['name'].strip())
        # pyautogui.typewrite(person['name'])
        autoit.send("{TAB}")
        speed_for_first_page(speed)
        autoit_slow_type_numbers_with_error(person['mobile'].strip())
        # autoit.send(person['mobile'])
        # pyautogui.typewrite(person['mobile'])
        speed_for_first_page(speed)
        autoit.send("{TAB}")
        speed_for_first_page(speed)
        selectIdentityProofDropdown(person['idType'])
        speed_for_first_page(speed)
        autoit.send("{TAB}")
        speed_for_first_page(speed)
        autoit_slow_type_numbers_with_error(person['idNumber'].strip())
        # autoit.send(person['idNumber'])
        # pyautogui.typewrite(person['idNumber'])
        # human_typing(person['idNumber'])
        speed_for_first_page(speed)
        autoit.send("{TAB}")
        speed_for_first_page(speed)
        selectGenderDropdown(person['gender'])
        time.sleep(0.25)
        speed_for_first_page(speed)
        # autoit.send("{TAB}")
        if i == 0:
            pyautogui.click(find_image_on_screen_using_opencv(UploadDocument_image_path, 60))
            time.sleep(0.85)
            pyautogui.typewrite(Person1AttachmentName)
            autoit.send("{ENTER}")
            time.sleep(0.25)
            autoit.send("{TAB}")
            autoit.send("{TAB}")
        else:
            autoit.send("{TAB}")
            autoit.send("{TAB}")
            autoit.send("{TAB}")
        speed_for_first_page(speed)
        setTimeEndAndWaitForTimer(i)
        autoit.send("{ENTER}")
        speed_for_first_page(speed)
        find_image_on_screen_using_opencv(selectTouristType_image_path, 60)
        time.sleep(0.1)
        for _ in range(2):  # Adjust the range as needed
            pyautogui.press('pageup')
        print(f"Iteration {i + 1}" + " complete")

    print("Execution Ended (form filling)  At: ", getDateTime())
    multiplePressUsingPyAutoGUI('pagedown', 3)
    time.sleep(0.5)
    x1, y1, z1, i1 = find_image_on_screen_using_opencv(agreeToCancellation_image_path, 10)
    pyautogui.click(x1, y1)
    x2, y2, z2, i2 = find_image_on_screen_using_opencv(agreeToTermsConditions_image_path, 10)
    pyautogui.click(x2, y2)
    autoit.send("{TAB}")
    printDateTime()


def find_image_on_screen_using_opencv(template_path1, timeout, threshold=0.7):
    template = cv2.imread(template_path1, 0)
    w, h = template.shape[::-1]
    start_time = time.time()

    while True:
        # Capture a screenshot
        screenshot = pyautogui.screenshot()

        # Convert screenshot to numpy array and then to grayscale
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

        # Perform template matching
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Check if the match value is above the threshold
        if max_val >= threshold:
            # Return the location of the matched region
            return max_loc[0], max_loc[1], w, h

        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            return None

        time.sleep(0.01)


def setImagePath():
    global image_directory
    if machine == "laptop" or machine == "pradeeplaptop":
        image_directory = os.getcwd() + '\\images_laptop'
    elif machine == "desktop" or machine == "rohit":
        image_directory = os.getcwd() + '\\images_desktop'

    global RanthamboreTigerReserve_image_path
    RanthamboreTigerReserve_image_path = os.path.join(image_directory, 'RanthamboreTigerReserve.png')

    global selectTouristType_image_path
    selectTouristType_image_path = os.path.join(image_directory, 'selectTouristType.png')

    global agreeToCancellation_image_path
    agreeToCancellation_image_path = os.path.join(image_directory, 'agreeToCancellation.png')

    global agreeToTermsConditions_image_path
    agreeToTermsConditions_image_path = os.path.join(image_directory, 'agreeToTermsConditions.png')

    global MemberDetails_image_path
    MemberDetails_image_path = os.path.join(image_directory, 'MemberDetails.png')

    global UploadDocument_image_path
    UploadDocument_image_path = os.path.join(image_directory, 'UploadDocument.png')


def days_difference_with_checkInDate(checkOutDate1):
    # Define the dates
    current_date = datetime.now()
    compare_date = datetime(2024, 11, 15)

    # Get the higher date
    higher_date = max(current_date, compare_date)

    # Parse checkOutDate
    checkOutDate1 = datetime.strptime(checkOutDate1, "%Y-%m-%d")

    # Calculate the difference in days
    difference_in_days = abs((checkOutDate1 - higher_date).days)
    return difference_in_days


def days_difference_with_checkInDate_checkOutDate(checkInDate1, checkOutDate1):
    # Convert strings to datetime objects if they aren't already
    if isinstance(checkInDate1, str):
        checkInDate1 = datetime.strptime(checkInDate1, "%Y-%m-%d")
    if isinstance(checkOutDate1, str):
        checkOutDate1 = datetime.strptime(checkOutDate1, "%Y-%m-%d")

    # Calculate the difference in days and ensure it's positive
    difference_in_days = abs((checkOutDate1 - checkInDate1).days) - 1
    return difference_in_days


def selectPaxDropdown(case_value):
    if case_value.lower() == "indian":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("in")
        autoit.send("{ENTER}")
    elif case_value.lower() == "foreigner":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("fo")
        autoit.send("{ENTER}")


def selectIdentityProofDropdown(case_value):
    if case_value.lower() == "aadhar":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("aad")
        autoit.send("{ENTER}")
    elif case_value.lower() == "passport":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("pas")
        autoit.send("{ENTER}")
    elif case_value.lower() == "driving license":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("dri")
        autoit.send("{ENTER}")
    elif case_value.lower() == "voter id":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("vot")
        autoit.send("{ENTER}")
    elif case_value.lower() == "pan card":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("pan")
        autoit.send("{ENTER}")
    elif case_value.lower() == "office id":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("off")
        autoit.send("{ENTER}")
    elif case_value.lower() == "student id":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("stu")
        autoit.send("{ENTER}")


def selectGenderDropdown(case_value):
    if case_value.lower() == "male":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("ma")
        autoit.send("{ENTER}")
    elif case_value.lower() == "female":
        multiplePressUsingPyAutoGUI('down', 1)
        pyautogui.typewrite("fe")
        autoit.send("{ENTER}")


def get_persons_list():
    persons = []

    persons.append({
        "pax": paxOfPerson1,
        "name": nameOfPerson1,
        "mobile": mobileOfPerson1,
        "idType": idTypeOfPerson1,
        "idNumber": idNumberOfPerson1,
        "gender": genderOfPerson1
    })

    persons.append({
        "pax": paxOfPerson2,
        "name": nameOfPerson2,
        "mobile": mobileOfPerson2,
        "idType": idTypeOfPerson2,
        "idNumber": idNumberOfPerson2,
        "gender": genderOfPerson2
    })

    persons.append({
        "pax": paxOfPerson3,
        "name": nameOfPerson3,
        "mobile": mobileOfPerson3,
        "idType": idTypeOfPerson3,
        "idNumber": idNumberOfPerson3,
        "gender": genderOfPerson3
    })

    # Person 4
    persons.append({
        "pax": paxOfPerson4,
        "name": nameOfPerson4,
        "mobile": mobileOfPerson4,
        "idType": idTypeOfPerson4,
        "idNumber": idNumberOfPerson4,
        "gender": genderOfPerson4
    })

    # Person 5
    persons.append({
        "pax": paxOfPerson5,
        "name": nameOfPerson5,
        "mobile": mobileOfPerson5,
        "idType": idTypeOfPerson5,
        "idNumber": idNumberOfPerson5,
        "gender": genderOfPerson5
    })

    # Person 6
    persons.append({
        "pax": paxOfPerson6,
        "name": nameOfPerson6,
        "mobile": mobileOfPerson6,
        "idType": idTypeOfPerson6,
        "idNumber": idNumberOfPerson6,
        "gender": genderOfPerson6
    })

    # Person 7
    persons.append({
        "pax": paxOfPerson7,
        "name": nameOfPerson7,
        "mobile": mobileOfPerson7,
        "idType": idTypeOfPerson7,
        "idNumber": idNumberOfPerson7,
        "gender": genderOfPerson7
    })

    # Person 8
    persons.append({
        "pax": paxOfPerson8,
        "name": nameOfPerson8,
        "mobile": mobileOfPerson8,
        "idType": idTypeOfPerson8,
        "idNumber": idNumberOfPerson8,
        "gender": genderOfPerson8
    })

    # Person 9
    persons.append({
        "pax": paxOfPerson9,
        "name": nameOfPerson9,
        "mobile": mobileOfPerson9,
        "idType": idTypeOfPerson9,
        "idNumber": idNumberOfPerson9,
        "gender": genderOfPerson9
    })

    # Person 10
    persons.append({
        "pax": paxOfPerson10,
        "name": nameOfPerson10,
        "mobile": mobileOfPerson10,
        "idType": idTypeOfPerson10,
        "idNumber": idNumberOfPerson10,
        "gender": genderOfPerson10
    })

    # Person 11
    persons.append({
        "pax": paxOfPerson11,
        "name": nameOfPerson11,
        "mobile": mobileOfPerson11,
        "idType": idTypeOfPerson11,
        "idNumber": idNumberOfPerson11,
        "gender": genderOfPerson11
    })

    # Person 12
    persons.append({
        "pax": paxOfPerson12,
        "name": nameOfPerson12,
        "mobile": mobileOfPerson12,
        "idType": idTypeOfPerson12,
        "idNumber": idNumberOfPerson12,
        "gender": genderOfPerson12
    })

    # Person 13
    persons.append({
        "pax": paxOfPerson13,
        "name": nameOfPerson13,
        "mobile": mobileOfPerson13,
        "idType": idTypeOfPerson13,
        "idNumber": idNumberOfPerson13,
        "gender": genderOfPerson13
    })

    # Person 14
    persons.append({
        "pax": paxOfPerson14,
        "name": nameOfPerson14,
        "mobile": mobileOfPerson14,
        "idType": idTypeOfPerson14,
        "idNumber": idNumberOfPerson14,
        "gender": genderOfPerson14
    })

    # Person 15
    persons.append({
        "pax": paxOfPerson15,
        "name": nameOfPerson15,
        "mobile": mobileOfPerson15,
        "idType": idTypeOfPerson15,
        "idNumber": idNumberOfPerson15,
        "gender": genderOfPerson15
    })

    # Person 16
    persons.append({
        "pax": paxOfPerson16,
        "name": nameOfPerson16,
        "mobile": mobileOfPerson16,
        "idType": idTypeOfPerson16,
        "idNumber": idNumberOfPerson16,
        "gender": genderOfPerson16
    })

    # Person 17
    persons.append({
        "pax": paxOfPerson17,
        "name": nameOfPerson17,
        "mobile": mobileOfPerson17,
        "idType": idTypeOfPerson17,
        "idNumber": idNumberOfPerson17,
        "gender": genderOfPerson17
    })

    # Person 18
    persons.append({
        "pax": paxOfPerson18,
        "name": nameOfPerson18,
        "mobile": mobileOfPerson18,
        "idType": idTypeOfPerson18,
        "idNumber": idNumberOfPerson18,
        "gender": genderOfPerson18
    })

    # Person 19
    persons.append({
        "pax": paxOfPerson19,
        "name": nameOfPerson19,
        "mobile": mobileOfPerson19,
        "idType": idTypeOfPerson19,
        "idNumber": idNumberOfPerson19,
        "gender": genderOfPerson19
    })

    # Person 20
    persons.append({
        "pax": paxOfPerson20,
        "name": nameOfPerson20,
        "mobile": mobileOfPerson20,
        "idType": idTypeOfPerson20,
        "idNumber": idNumberOfPerson20,
        "gender": genderOfPerson20
    })
    return persons


def setTimeStart(i):
    print("value of i is: ", i)
    time_start_vars = {0: 'timeStart1', 1: 'timeStart2', 2: 'timeStart3', 3: 'timeStart4', 4: 'timeStart5',
                       5: 'timeStart6', 6: 'timeStart7', 7: 'timeStart8', 8: 'timeStart9', 9: 'timeStart10',
                       10: 'timeStart11', 11: 'timeStart12', 12: 'timeStart13', 13: 'timeStart14', 14: 'timeStart15',
                       15: 'timeStart16', 16: 'timeStart17', 17: 'timeStart18', 18: 'timeStart19', 19: 'timeStart20'}
    global_vars = globals()
    if i in time_start_vars:
        global_vars[time_start_vars[i]] = getDateTime()
        print(f"Start time for Person {i} is: ", global_vars[time_start_vars[i]])


def setTimeEndAndWaitForTimer(i):
    print("value of i is: ", i)
    time_vars = {
        0: 'timeEnd1', 1: 'timeEnd2', 2: 'timeEnd3', 3: 'timeEnd4', 4: 'timeEnd5',
        5: 'timeEnd6', 6: 'timeEnd7', 7: 'timeEnd8', 8: 'timeEnd9', 9: 'timeEnd10',
        10: 'timeEnd11', 11: 'timeEnd12', 12: 'timeEnd13', 13: 'timeEnd14', 14: 'timeEnd15',
        15: 'timeEnd16', 16: 'timeEnd17', 17: 'timeEnd18', 18: 'timeEnd19', 19: 'timeEnd20'
    }
    start_vars = {
        0: 'timeStart1', 1: 'timeStart2', 2: 'timeStart3', 3: 'timeStart4', 4: 'timeStart5',
        5: 'timeStart6', 6: 'timeStart7', 7: 'timeStart8', 8: 'timeStart9', 9: 'timeStart10',
        10: 'timeStart11', 11: 'timeStart12', 12: 'timeStart13', 13: 'timeStart14', 14: 'timeStart15',
        15: 'timeStart16', 16: 'timeStart17', 17: 'timeStart18', 18: 'timeStart19', 19: 'timeStart20'
    }
    global_vars = globals()

    if i in time_vars:
        global_vars[time_vars[i]] = getDateTime()
        print(f"End time for Person {i} is: ", global_vars[time_vars[i]])
        diff = getTimeDiff(global_vars[time_vars[i]], global_vars[start_vars[i]])
        if diff >= datetime.timedelta(seconds=timer):
            print(f"{timer} seconds have passed. Pressing ADD!")
        else:
            remaining_seconds = timer - diff.total_seconds()
            print(f"Waiting for an additional {remaining_seconds} seconds.")
            time.sleep(remaining_seconds)
