import os

import keyboard

from CoreMethods.CoreMethods import (debounce_key, setImagePath, formFill)


def exit_program():
    print("r+4 keys pressed - Exiting... Goodbye!")
    os._exit(0)  # Exit the current process


def main():
    # valueOfNationalityDropDownDisplayed = nationalityDropDownDisplayed()
    setImagePath()
    # print("CheckInDate -->"+checkInDate+"  and CheckOutDate-->"+checkOutDate)
    print("Press - r+1 - For filling FORM only")
    print("Press - r+4 - For exiting the script")

    # Add listener
    keyboard.add_hotkey('r+4', exit_program)

    while True:
        if keyboard.is_pressed("r+1"):
            print("Keys Pressed - r+1 - Filling first page only")
            formFill()
            debounce_key("r+1")  # Wait until the key is released


if __name__ == "__main__":
    main()
