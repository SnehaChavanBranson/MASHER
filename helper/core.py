""" core functions"""

import time
import squish


# ! Boolean Functions
def IsObjectPresent(obj: str) -> bool:
    test.log(f"Checking for presence of object : {obj}")
    return bool(squish.waitForObject(obj))


def IsObjectVisible(obj: str) -> bool:
    test.log(f"Checking for object visibility : {obj}")
    return bool(squish.isElementVisible(obj))


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
    test.log(f"Input for the placeholder")
    squish.type(obj, "")


def ClickButton(obj: str) -> None:
    test.log(f"Click button given: {obj}")
    squish.clickButton(obj)


def CaptureScreenshot(obj: str) -> None:
    test.log(f"Capturing screenshot: {obj}")
    squish.captureScreenshot(obj)


def SetToggleOn(obj: str):
    test.log(f"Toggle on: {obj}")
    squish.check(obj)


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
        test.fail("Failed to Find Login Screen")

    except Exception as error:
        test.error(f"Exception caught while trying to Wait for object to show up due to - {error}")
