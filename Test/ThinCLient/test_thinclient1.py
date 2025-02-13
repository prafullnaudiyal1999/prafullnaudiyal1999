# ThinClient DOWNLOAD + INSTALL + MAKE CMD AT FOCUS IN WIN (IM STUCK HERE)

import os
import platform
import zipfile
import urllib.request
import subprocess
import pytest
import time
import pyautogui
from urllib.error import HTTPError, URLError

@pytest.fixture(scope="function", autouse=True)
def cleanup_activities():
    print("\n\nCLEANUP start")
    system = platform.system()
    architecture = platform.machine()
    if system == "Windows":
        home_dir = os.path.expanduser('~')  # Get home directory of the current user
        downloads_folder = os.path.join(home_dir, "Downloads")
        filename = "Monotype_Fonts_Headless_Sync_Service_win_v110.zip"
        file_path = os.path.join(downloads_folder, filename)  # Construct full file path
        try:
            if os.path.exists(file_path):
                print(f"File exists: {file_path}")
                os.remove(file_path)  # Delete the file after yielding
                # print(f"File deleted: {file_path}
            else:
                print(f"File does not exist: {file_path}")
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")
        print("CLEANUP ended\n")
    elif system == "Darwin":
        if architecture == "arm64":
            pass
        elif architecture == "x86_64":
            pass
    else:
        raise Exception("Unsupported OS or architecture : Please add details for Linux too as Thin client is supported in Linux")

@pytest.fixture()
def thin_client_installation():
    print("Installing MTFApp start")

    system = platform.system()
    architecture = platform.machine()
    timeout = 600 # timeout after 10 min
    check_interval = 5

    if system == "Windows":
        home_dir = os.path.expanduser('~')  # Get home directory of the current user
        downloads_folder = os.path.join(home_dir, "Downloads")
        url =  "https://monotype-app.s3.amazonaws.com/hls/releasecandidate/win/Monotype_Fonts_Headless_Sync_Service_win_v110.zip"
        filename ="Monotype_Fonts_Headless_Sync_Service_win_v110.zip"
        file_path = os.path.join(downloads_folder, filename)  # Construct full file path
        print(f"Downloading installer to {file_path}...")
        urllib.request.urlretrieve(url, file_path)

        start_time = time.time()  # Get the current time when the check starts
        while True:
            # Check if the file exists
            if os.path.exists(file_path):
                print(f"File exists: {file_path}")
                print(f"Download completed: {file_path}")
                break  # Exit the loop if file exists

            # Check if the timeout has been reached
            if time.time() - start_time > timeout:
                print(f"Error: File did not download in time. File does not exist at: {file_path}")
                break  # Exit the loop if timeout is reached

            # Wait for the specified check interval before checking again
            time.sleep(check_interval)

        extracted_file_path = os.path.join(downloads_folder, "ThinClient")
        try:
            # Open the zip file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # Extract all the contents to the same directory
                zip_ref.extractall(extracted_file_path)
                print(f"File extracted to {extracted_file_path}")
        except zipfile.BadZipFile:
            print(f"Error: {file_path} is not a valid zip file.")
        except Exception as e:
            print(f"Error occurred: {e}")

        bat_file_path = os.path.join(extracted_file_path, "installer-batch.bat")
        admin_password = "1432"
        # Ensure the file path is absolute
        if not os.path.isabs(bat_file_path):
            bat_file_path = os.path.abspath(bat_file_path)

        # Run the batch file with runas to elevate privileges
        command = f'runas /user:Administrator "{bat_file_path}"'

        try:
            # Start the process
            process = subprocess.Popen(command, shell=True)

            # Wait a bit for the UAC prompt to appear
            time.sleep(2)

            # Type the password into the UAC prompt (You need to ensure the UAC prompt is in focus)
            pyautogui.typewrite(admin_password)
            pyautogui.press('enter')  # Press Enter to submit the password

            # Wait for the batch file to run
            process.wait()
            subprocess.run([bat_file_path], stderr=subprocess.STDOUT, shell=True)

            # After the batch file finishes, kill the process if needed
            # Close the subprocess
            process.terminate()  # Or use process.kill() if needed to force termination

            print("Batch file process terminated.")

        except Exception as e:
            print(f"Error occurred: {e}")


        yield file_path  # Yield the file path
        try:
            if os.path.exists(file_path):
                print(f"File exists: {file_path}")
                os.remove(file_path)  # Delete the file after yielding
                # print(f"File deleted: {file_path}
            else:
                print(f"File does not exist: {file_path}")
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")
        print("Installing MTFApp ended\n")


    elif system == "Darwin":
        if architecture == "arm64":
            url = "https://monotype-app.s3.amazonaws.com/hls/releasecandidate/win/Monotype_Fonts_Headless_Sync_Service_mac_silicon_v110.zip"
        elif architecture == "x86_64":
            url =  "https://monotype-app.s3.amazonaws.com/hls/releasecandidate/win/Monotype_Fonts_Headless_Sync_Service_mac_intel_v110.zip"
    else:
        raise Exception("Unsupported OS or architecture : Please add details for Linux too as Thin client is supported in Linux")


# @pytest.mark.usefixtures('thin_client_installation')
def test_run(thin_client_installation):
    print("Start Execution")
