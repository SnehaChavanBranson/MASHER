""" core functions"""

import os
import subprocess
import time
import test
import squish
from constants import names

# ! Boolean Functions
def IsObjectPresent(obj: str) -> bool:
    test.log(f"Checking for presence of object : {obj}")
    return bool(squish.waitForObject(obj))

def takeScreenshot() -> None:
    squish.grabDesktopScreenshot("/home/sneha/Documents/Screenshots/trail.png")

def test_id(value) -> None:
    if isinstance(value, int):
        print(f"Valid input: {value}")
        return value
    else:
        raise ValueError("Invalid input: Only whole numbers (integers) are allowed.")
    
def VerifyPopUpMessage(obj, str) -> None:
    test.log("entered into core verify pop message")
    return squish.waitForObject(obj).text
    test.log("done with into core verify pop message")

# def IsObjectVisible(obj: str) -> bool:
    # test.log(f"Checking for object visibility : {obj}")
    # return bool(isElementVisible(obj))

def IsObjectVisible(obj: str) -> bool:
    test.log(f"Checking for object visibility: {obj}")
    try:
        # Wait for the object to exist and get the object reference
        element = waitForObject(obj)
        
        # Check if the element is visible
        return element.isVisible()
    except Exception as e:
        test.log(f"Error: {str(e)}")
        return False


def IsValueSame(actual, expected) -> bool:
    return bool(actual == expected)


def IsProcessRunning(process_name_or_id: str) -> bool:
    return True


# ! Action Functions
def GetValueFromObject(obj: str) -> str:
    try:
        actual_object = squish.waitForObject(obj)
        return actual_object.text
    except Exception as error:
        test.error(f"Exception caught while trying to get value from object due to - {error}")
    return ""


def EnterText(obj: str, text: str = "") -> None:
    enter_text = obj
    squish.waitForObject(enter_text).setProperty("text",text)



def ClickButton(obj: str) -> None:
    print(f"Click button given: {obj}")
    button = obj
    squish.mouseClick(squish.waitForObject(button))

  
def CaptureScreenshot(obj: str) -> None:
    print(f"Capturing screenshot: {obj}")
    squish.captureScreenshot(obj)
    
def screenRecordVideo() -> None:
    print("taking video for the testcase")
    test.startVideoCapture()

def screenStopVideoRecord() -> None:
    print("stopped video recording")
    test.stopVideoCapture()

def SetToggleOn(obj: str):
    print(f"Toggle on: {obj}")
    squish.check(obj)
    mouseClick(waitForObject(names.uIController_Rectangle_2), 1203, 437, Qt.LeftButton)


def SetToggleOff(obj: str):
    test.log(f"Toggle off: {obj}")
    squish.uncheck(obj)


def WaitTillObjectIsLoaded(obj: str, retry_for=30, frequency: int = 2) -> None:
    found = False
    try:
        for _ in range(retry_for):
            found = IsObjectPresent(obj)
            if found:
                test.log("Login Screen is Up")
                return None
            time.sleep(frequency)
        print("Failed to Find Login Screen")

    except Exception as error:
        print(f"Exception caught while trying to Wait for object to show up due to - {error}")


def ExecutePreConditions():  # Ensure the system is in known ideal state before execution
    pass


def StartApplication() -> None:  # Start the AUT
    # Define the target directory
    target_directory = "/home/branson/Desktop/HMI_SC/Polaris_HMI/"

    try:
        # Check if the directory exists
        if not os.path.isdir(target_directory):
            return f"Directory {target_directory} does not exist."

        # Change to the target directory
        os.chdir(target_directory)

        # Run the shell script
        subprocess.run(["./Launch_HMI.sh"], check=True)

        return "Shell script executed successfully."

    except subprocess.CalledProcessError as e:
        return f"Error occurred while executing the script: {e}"
    except PermissionError:
        return "Permission denied to execute the shell script."


def StopApplication():  # Stop the AUT
    target_directory = "/home/branson/Desktop/HMI_SC/Polaris_HMI/"

    try:
        # Check if the directory exists
        if not os.path.isdir(target_directory):
            return f"Directory {target_directory} does not exist."

        # Change to the target directory
        os.chdir(target_directory)

        # Get the process name or the application that was launched
        process_name = "Polaris_HMI"  # Replace this with your actual application name or process identifier

        # Find the PID of the running process
        result = subprocess.run(["pgrep", process_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            return f"Process '{process_name}' not found."

        # Get the PID from the output
        pid = result.stdout.decode().strip()

        # Kill the process using the PID
        os.kill(int(pid), signal.SIGTERM)
        return f"Application '{process_name}' stopped successfully."

    except Exception as e:
        return f"Error occurred while stopping the application: {e}"


def ExecutePostConditions():
    pass
