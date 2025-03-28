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
    EnterText(names.UserName_TextField, username)
    time.sleep(0.5)


def EnterPassword(password: str = "") -> None:
    test.log(f"Entering Password as - {password}")
    EnterText(names.Password_TextField, password)
    time.sleep(0.5)


def ClickLoginButton() -> None:
    test.log("Clicking on the login button:")
    login_obj = squish.waitForObject(names.login_button_obj)
    ClickButton(login_obj)


def WaitTillLandingPageIsLoaded():
    test.log("Entered to dashboard")
    pass


def CheckIfUsernameIsEmpty() -> None:
    pass


def CheckIfPasswordIsEmpty() -> None:
    pass


def GetUsernameFromTextbox() -> str:
    return GetValueFromObject(LOGIN_PAGE_OBJECTS["UsernameInput"])


def LoginWithCredentials(username="", password="") -> None:
    try:
        EnterUsername(username)
        EnterPassword(password)
        ClickLogin()
    except Exception as error:
        test.fail(f"Exception caught while trying to Perform Login with username - {username} and Password - {password} due to - {error}")


def UserLocked():
    squish.clickButton(names.uIController_OK_BransonPrimaryButton)


def CheckIfPasswordIsNotEmpty() -> None:
    CheckIfValueIsNotEmpty(LOGIN_PAGE_OBJECTS["PasswordInput"])


def AlertsButtonClick() -> None:
    if IsObjectVisible(names.reset_All_BransonPrimaryButton):
        ClickButton(squish.waitForObject(names.reset_All_BransonPrimaryButton))
        ClickBUttton(squish.waitForObject(names.imageCross_Image))
    else:
        test.log("showing an alert box which is not being cancelled")


def CheckIfLoginPageIsLoaded() -> None:
    if IsObjectPresent(LOGIN_PAGE_OBJECTS["Area"]):
        test.passes("")
    else:
        test.fail("")


def CheckLoggedInUserName():
    pass


def ClickOkayPopUp() -> None:
    test.log("Clicking on the pop up okay button:")
    pop_up_okay = squish.waitForObject(names.uIController_OK_BransonPrimaryButton)
    ClickButton(pop_up_okay)


def VerifyInvalidCredsMessage() -> None:
    verify_msg = squish.waitForObject(names.uIController_Invalid_Username_or_Password_Text)
    actual_text = verify_msg.text
    expected_text = "Invalid Username or Password"

    if actual_text == expected_text:
        test.passes("Text verification passed!")
    else:
        test.fail(f"Text verification failed. Expected: '{expected_text}', but found: '{actual_text}'")
    pass


def VerifyPopEmptyPassword() -> None:
    verify_msg = squish.waitForObject(names.uIController_Password_is_Empty_Text)
    actual_text = verify_msg.text
    expected_text = "Password is Empty"

    if actual_text == expected_text:
        test.passes("Text verification passed!")
    else:
        test.fail(f"Text verification failed. Expected: '{expected_text}', but found: '{actual_text}'")
    pass


def VerifyPopEmptyUsername() -> None:
    verify_msg = squish.waitForObject(names.uIController_User_Name_is_Empty_Text)
    actual_text = verify_msg.text
    expected_text = "User Name is Empty"

    if actual_text == expected_text:
        test.passes("Text verification passed!")
    else:
        test.fail(f"Text verification failed. Expected: '{expected_text}', but found: '{actual_text}'")
    pass


def CheckLoggedInUserName():
    pass
