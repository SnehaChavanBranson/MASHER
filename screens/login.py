import test
import squish
import time
from helper.core import *
from constants.objects import *
from helper.helper import CheckIfValueIsNotEmpty


def WaitTillLoginScreenIsUp(retry_for=30, frequency: int = 2):
    WaitTillObjectIsLoaded(LOGIN_PAGE_OBJECTS["Area"], retry_for, frequency)


def EnterUsername(username: str = "") -> None:
    test.log(f"Entering Username as - {username}")
    EnterText(LOGIN_PAGE_OBJECTS["UsernameInput"], username)
    time.sleep(0.5)


def EnterPassword(password: str = "") -> None:
    test.log(f"Entering Password as - {password}")
    EnterText(LOGIN_PAGE_OBJECTS["PasswordInput"], password)
    time.sleep(0.5)


def ClickLogin() -> None:
    test.log("Clicking on the login button:")
    ClickButton(LOGIN_PAGE_OBJECTS["Button"])


def GetUsernameFromTextbox() -> str:
    return GetValueFromObject(LOGIN_PAGE_OBJECTS["UsernameInput"])


def LoginWithCredentials(username="", password="") -> None:
    try:
        EnterUsername(username)
        EnterPassword(password)
        ClickLogin()
    except Exception as error:
        test.error(f"Exception caught while trying to Perform Login with username - {username} and Password - {password} due to - {error}")


def CheckIfPasswordIsNotEmpty() -> None:
    CheckIfValueIsNotEmpty(LOGIN_PAGE_OBJECTS["PasswordInput"])


def CheckIfLoginPageIsLoaded() -> None:
    if IsObjectPresent(LOGIN_PAGE_OBJECTS["Area"]):
        test.passes("")
    else:
        test.fail("")


def CheckLoggedInUserName():
    pass
