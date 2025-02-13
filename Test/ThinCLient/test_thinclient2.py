# CODE TO MAKE CMD IN FOCUS AND COPY ITS CONTENT IN A FILE (DUE TO PASSWORD ISSUES IT IS UNABLE TO DO IT NEED HELP)

#OPEN THIN CLIENT IN CMD MANUALLY THEN RUN THIS BELOW CODE


import pygetwindow as gw
import pyautogui
import time

def bring_cmd_to_front_and_send_input():
    # Try to find the CMD window with the updated title pattern
    # Searching for both possible titles:
    windows = gw.getWindowsWithTitle("Select Administrator: C:\\Windows\\System32\\cmd.exe")  # Updated title pattern

    if not windows:
        windows = gw.getWindowsWithTitle("Administrator: C:\\Windows\\System32\\cmd.exe")  # Fallback for initial title

    if windows:
        cmd_window = windows[0]  # Get the first matching window
        cmd_window.activate()  # Bring it to the front
        time.sleep(2)  # Give it a moment to come into focus and make sure it's ready

        print("CMD Window is now in focus!")

        # Now let's make sure the cursor is active, before typing
        pyautogui.click()  # Simulate a mouse click to ensure the cursor is in focus in the window

        time.sleep(1)  # Give the system a moment to process

        # Send some input (for example, 'Hello World')
        pyautogui.typewrite('Hello World')  # Type the text
        pyautogui.press('enter')  # Press Enter to send the text
        print("Input sent and Enter key pressed in CMD window.")
    else:
        print("CMD window with the specified title not found!")


# Call the function
def test_r():
    bring_cmd_to_front_and_send_input()

