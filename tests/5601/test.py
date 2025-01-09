# Author - Sneha Chavan
# Created Date - 27/12/2024
# Updated Date - <Agreed upon Date format>
# Last Review Date - <Agreed upon Date format>
# Defects logged - <List of all Defect IDs active or inactive>
# Active Defects - <List of all active defects>

import squish
import test

EXPECTED_UIController = "Username"
PASSWORD = "Password"


def main() -> None:
    test.log("""Step 2.1 Description* On the UIController software of HMI""")
    test.log("Navigate to Left MENU -> SYSTEM --> INFORMATION")
    NavigateToInformation()
    test.log("""Expected Results: Information tab on the Configuration tab of System screen shall be displayed successfully.""")
    CheckUIControllerVersion(ACTUAL_UIController, EXPECTED_UIController)

    test.log("""Step 2.2 Description* Check the Model value""")
    test.log("""Expected Results: Model shall have value as Actuator Type""")
    # NOT VALID TESTCASE

    test.log("""Step 2.3 Description* On the UIController software of HMI:""")
    test.log("Navigate to Left menu -> SYSTEM --> INFORMATION >System Feature")
    test.log("""Expected Results: Information tab on the Configuration tab of System screen shall be displayed successfully.""")

    test.log("""Step 2.4 Description*""")
    test.log("Check the other supported features.")
    test.log("""Expected Results: Model shall have value as Others""")


if __name__ == "__main__":
    ExecutePreConditions()  # Ensure the system is in known ideal state before execution
    StartApplication()  # Start the AUT
    main()  # The main body corresponding to the Testcase.
    StopApplication()  # Stop the AUT
    ExecutePostConditions()  # Ensure the system is reverted to known ideal state post execution
