# Author - Sneha Chavan
# Created Date - <Agreed upon Date format>
# Updated Date - <Agreed upon Date format>
# Last Review Date - <Agreed upon Date format>
# Defects logged - <List of all Defect IDs active or inactive>
# Active Defects - <List of all active defects>

import squish
import test

from helper.helper import CheckIfApplicationIsRunning, CheckIfValueIsSame
from screens.dashboard import CheckIfDashboardIsVisible, WaitTillDashboardIsLoaded
from screens.login import (
    CheckIfLoginPageIsLoaded,
    CheckIfPasswordIsNotEmpty,
    ClickLogin,
    EnterPassword,
    EnterUsername,
    GetUsernameFromTextbox,
    WaitTillLoginScreenIsUp,
)

USERNAME = "Username"
PASSWORD = "Password"


def main() -> None:

    test.log("""Step 1.1 Description* Power up the system""")
    test.log("This will be checked as part of Expected results")

    test.log("""Expected Results: System shall powered up and Booting procedure shall start onto the system.""")
    CheckIfApplicationIsRunning()

    test.log("""Step 1.2 Description* Wait for the login screen to display on the UI""")
    WaitTillLoginScreenIsUp()

    test.log("""Expected Results: Login screen shall be displayed on the UI after successful power up & booting of the system.""")
    CheckIfLoginPageIsLoaded()

    test.log("""Step 1.3 Description* On the login screen, Enter Username: Username""")
    EnterUsername(USERNAME)

    test.log("""Expected Results UI shall accept the username provided.""")
    entered_username = GetUsernameFromTextbox()
    CheckIfValueIsSame(entered_username, USERNAME)

    test.log("""Step 1.4 Description* On the login screen, Enter Password: Password""")
    EnterPassword(PASSWORD)

    test.log("""Expected Results UI shall accept the password provided.""")
    CheckIfPasswordIsNotEmpty()

    test.log("""Step 1.5 Description* Tap on the login button""")
    ClickLogin()
    WaitTillDashboardIsLoaded()

    test.log("""Expected Results Login shall be successful and UI shall be navigated to the Dashboard Screen.""")
    CheckIfDashboardIsVisible()


if __name__ == "__main__":
    ExecutePreConditions()  # Ensure the system is in known ideal state before execution
    StartApplication()  # Start the AUT
    main()  # The main body corresponding to the Testcase.
    StopApplication()  # Stop the AUT
    ExecutePostConditions()  # Ensure the system is reverted to known ideal state post execution
