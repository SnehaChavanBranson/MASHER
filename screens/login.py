import test
import squish
import time
from helper.core import *
from helper import core
# from constants.objects import *
from constants import names
from helper.helper import CheckIfValueIsNotEmpty
import test


# def WaitTillLoginScreenIsUp(retry_for=30, frequency: int = 2):
#     WaitTillObjectIsLoaded(LOGIN_PAGE_OBJECTS["Area"], retry_for, frequency)

#
# def EnterUsername(username: str = "") -> None:
#     # test.log(f"Entering Username as - {username}")
#     EnterText(names.UserName_TextField, username)
#     time.sleep(0.2)

def startApp():
    squish.startApplication("QT_UIController")

def autoLogin():
    # ClickButton(squish.waitForObject(names.uIController_imageLeftMenu_Image))
    # ClickButton(squish.waitForObject(names.uIController_SYSTEM_Text))
    # ClickButton(squish.waitForObject(names.systemWindow_Image))
    # ClickButton(squish.waitForObject(names.configurationTabBar_BransonTabButton))
    # ClickButton(squish.waitForObject(names.configurationTabBar_BransonTabButton_3))
    # ClickButton(squish.waitForObject(names.sysConfgGenWindow_authCheckCombobox_BransonComboBox))
    # ClickButton(squish.waitForObject(names.sysConfgGenWindow_authCheckCombobox_BransonComboBox))
    # ClickButton(squish.waitForObject(names.sysConfgGenWindow_authCheckCombobox_BransonComboBox))
    # ClickButton(squish.waitForObject(names.sysConfgGenWindow_authCheckCombobox_BransonComboBox))
    # ClickButton(squish.waitForObject(names.sysConfgGenWindow_authCheckCombobox_BransonComboBox))
    # ClickButton(squish.waitForObject(names.sysConfgGenWindow_authCheckCombobox_BransonComboBox))
    # ClickButton(squish.waitForObject(names.sysConfgGenWindow_authCheckCombobox_BransonComboBox))
    # ClickButton(squish.waitForObject(names.off_Text))
    # ClickButton(squish.waitForObject(names.sysConfgGenWindow_SAVE_BransonPrimaryButton))
    # ClickButton(squish.waitForObject(names.oK_BransonPrimaryButton))

# def login_r(username:str = "", password: str = "") -> None:
#     test.log("entered username")
#     core.EnterText(names.loginFlick_textFildUserName_TextField, username)
#     squish.keyPress("<Tab>")
#     squish.keyRelease("<Tab>")
#     core.EnterText(names.loginFlick_textFildPassword_TextField, password)
#     test.log("entered password")
#     squish.keyPress("<Tab>")
#     squish.keyRelease("<Tab>")
#     ClickButton(names.loginFlick_loginButton_Button)
#     test.log("clicked on login")

    # core.EnterText(names.loginFlick_textFildUserName_TextField, username)
    # time.sleep(5)
    # squish.keyPress("<Tab>")
    #
    # squish.keyPress("<Tab>")
    # ClickButton(squish.waitForObject(names.loginFlick_loginButton_Button))
    # time.sleep(5)
    # core.EnterText(names.loginFlick_textFildUserName_TextField, "<Tab>")
    #

    # squish.type(names.loginFlick_textFildUserName_TextField, "<Tab>")
    # ClickButton(squish.waitForObject(names.loginFlick_Branson_Polaris_Text))
    # core.EnterText(names.loginFlick_textFildPassword_TextField, password)
    # time.sleep(5)
    # # squish.type(names.loginFlick_textFildUserName_TextField, "<Tab>")
    # # ClickButton(squish.waitForObject(names.loginFlick_Enter_Username_Text))
    # squish.keyPress("<Alt+Tab>")
    # ClickButton(squish.waitForObject(names.loginFlick_loginButton_Button))
    # EnterText(squish.waitForObject(names.loginFlick_textFildUserName_TextField), "admin")
    # ClickButton(squish.waitForObject(names.uIController_loginFlick_Flickable))
    # EnterText(squish.waitForObject(names.loginFlick_textFildPassword_TextField), "Emerson@1")
    # ClickButton(squish.waitForObject(names.uIController_loginFlick_Flickable))
    # ClickButton(squish.waitForObject(names.loginFlick_loginButton_Button))
# def EnterPassword(password: str = "") -> None:
#     # test.log(f"Entering Password as - {password}")
#     EnterText(names.Password_TextField, password)
#     time.sleep(0.2)
#     # type(waitForObject(names.loginFlick_textFildPassword_TextField), "<Tab>")
#
#
# def ClickLoginButton() -> None:
#     # test.log("Clicking on the login button:")
#     login_obj = squish.waitForObject(names.loginFlick_loginButton_Button)
#     ClickButton(login_obj)
#
# def ClickOutside() -> None:
#     test.log("Entered to clicking outside")
#     # outside = squish.waitForObject(names.uIController_loginFlick_Flickable)
#     ClickButton(squish.waitForObject(names.uIController_loginFlick_Flickable))

def WaitTillLandingPageIsLoaded():
    test.log("Entered to dashboard")
    pass


def CheckIfUsernameIsEmpty() -> None:
    pass


def CheckIfPasswordIsEmpty() -> None:
    pass


def GetUsernameFromTextbox() -> str:
    return GetValueFromObject(LOGIN_PAGE_OBJECTS["UsernameInput"])




# def EnterText(objectName, text: str) -> None:
#     obj = squish.waitForObject(objectName)
#     ClickButton(obj)
#     type(obj, text)

# def ClickButton(objectName) -> None:
#     obj = squish.waitForObject(objectName)
#     ClickButton(obj)

def EnterUsername(username: str) -> None:
    squish.snooze(2)
    EnterText(names.loginFlick_textFildUserName_TextField, username)

def EnterPassword(password: str) -> None:
    squish.snooze(2)
    EnterText(names.Password_TextField, password)

def PressTab() -> None:
    squish.snooze(2)
    EnterText(names.loginFlick_textFildUserName_TextField, "<Tab>")

def ClickOutside() -> None:
    squish.snooze(2)
    ClickButton(names.uIController_loginFlick_Flickable)

def ClickLoginButton() -> None:
    squish.snooze(4)
    ClickButton(names.login_button_obj)
    squish.snooze(5)



def LoginWithCredentials(username="", password="") -> None:
    try:
        EnterUsername(username)
        # squish.keyPress("<Tab>")
        # squish.keyRelease("<Tab>")
        EnterPassword(password)
        # squish.keyPress("<Tab>")
        # squish.keyRelease("<Tab>")
        time.sleep(2)
        time.sleep(2)
        #ClickLoginButton()
        # EnterText(names.loginFlick_textFildUserName_TextField, "<Tab>")
        ClickLoginButton()
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
    test.log("Clicking on the pop up okay button")
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

def logout():
    test.log("Starting to logout from the system")
    ClickButton(names.uIController_imageRightMenu_Image)
    squish.snooze(0.2)
    ClickButton(names.logout_icon)
    squish.snooze(0.2)
    object_name = names.are_you_sure_want_to_logout_Text
    obj = squish.waitForObject(object_name)
    actual_text = str(obj.text)
    pop_up = "Are you sure want to logout?"
    test.compare(actual_text, pop_up)
    squish.snooze(0.2)
    ClickButton(names.yes_BransonPrimaryButton)
    squish.snooze(0.2)
    test.log("Completed logout from the system")
    
def notification_reset():
    ClickButton(names.uIController_imageAlarmNotification_Image)
    ClickButton(names.reset_All_BransonPrimaryButton)
    ClickButton(names.uIController_backGround_Rectangle)
    # ClickButton(names.uIController_imageLeftMenu_Image)
    # ClickButton(names.uIController_RECIPES_Text)
    
def add_new_profile():
    pass

def CheckLoggedInUserName():
    pass
