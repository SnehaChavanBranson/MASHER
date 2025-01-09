# Author - Sneha Chavan
# Created Date - <Agreed upon Date format>
# Updated Date - <Agreed upon Date format>
# Last Review Date - <Agreed upon Date format>
# Defects logged - <List of all Defect IDs active or inactive>
# Active Defects - <List of all active defects>

import squish
import test

EXPECTED_BUILD_NAME = ""
USERNAME = ""
PASSWORD = ""
VALUE_ACTUATOR = "Actuator"
SUPPORTED_FEATURE_VALUE = "Others"
CONTROLLER_SOFTWARE_VERSION = ""
ACTUATOR_SOFTWARE_VERSION = ""
SUPERVISORY_SOFTWARE_VERSION = ""
POWER_CONTROLLER_SOFTWARE_VERSION = ""


def main() -> None:
    test.log(
        """Step 1: Description*Record the Build Name of the software loaded onto machine."""
    )

    build_name = GetBuildName()

    test.log(
        """Expected Results:The Build Name is the same as intended for verification test."""
    )
    CheckIfBuildNameIsSame(build_name, EXPECTED_BUILD_NAME)

    test.log("""Step 2: Description*Login to the UI""")
    Login(username=USERNAME, password=PASSWORD)
    WaitTillLandingPageIsLoaded()

    test.log("""Expected Results:User login is successful.""")
    CheckLoggedInUserName(USERNAME)

    test.log(
        """Step 3.1: Description*On the UIController software of HMI:
    Navigate to Left menu -> SYSTEM --> INFORMATION"""
    )
    OpenMenuItem(LEFT_MENU_OBJECT, ["SYSTEM", "INFORMATION"])

    test.log(
        """Expected Results: Information tab on the Configuration tab of System screen shall be displayed successfully."""
    )
    CheckPresenceOfInformationTab()

    test.log("""Step 3.2: Description*Check the Model value""")
    model_value = GetInformationTabModelValue()

    test.log("""Expected Results: Model shall have value as Actuator Type""")
    CheckIfValueIsSame(model_value, VALUE_ACTUATOR)

    test.log(
        """Step 3.3: Description*On the UIController software of HMI: Navigate to Left menu -> SYSTEM --> INFORMATION -->System Feature"""
    )
    OpenMenuItem(LEFT_MENU_OBJECT, ["SYSTEM", "INFORMATION", "System Feature"])

    test.log(
        """Expected Results: Information tab on the Configuration tab of System screen shall be displayed successfully."""
    )
    CheckPresenceOfInformationTab()

    test.log("""Step 3.4: Description*Check the other supported features.""")
    supported_features = GetSupportedFeaturesInInformationTab()

    test.log("""Expected Results: Model shall have value as Others""")
    CheckIfValueIsSame(supported_features, SUPPORTED_FEATURE_VALUE)

    test.log("""Step 4: Description*Navigate to Left menu -> SYSTEM -> INFORMATION""")
    OpenMenuItem(LEFT_MENU_OBJECT, ["SYSTEM", "INFORMATION"])

    test.log(
        """Expected Results: Machine Details tab in the INFORMATION page is displayed."""
    )
    CheckPresenceOfMachineDetailsTab()

    test.log(
        """Step 5: Description*Record UI Controller Software Version, as displayed by the UI."""
    )
    controller_version = GetControllerSoftwareVersion()
    get_stream = GetApplicationBuildStream()

    test.log(
        """Expected Results:
    • If the version under test is from the Main Stream,
    recorded version number consists of four groups of digits separated by "."
    • If the version under test is from the Integration Stream,
    recorded version number consists of three groups of digits separated by "."
    • Recorded version number corresponds to software build intended for test."""
    )

    CheckStreamVersionDigitGroup(get_stream)
    CheckIfValueIsSame(controller_version, CONTROLLER_SOFTWARE_VERSION)

    test.log(
        """Step 6: Description*Record Actuator Controller Software Version, as displayed by the UI."""
    )
    actuator_version = GetActuatorSoftwareVersion()

    test.log(
        """Expected Results:
    • If the version under test is from the Main Stream,
    recorded version number consists of four groups of digits separated by "."
    • If the version under test is from the Integration Stream,
    recorded version number consists of three groups of digits separated by "."
    • Recorded version number corresponds to software build intended for test."""
    )

    CheckStreamVersionDigitGroup(get_stream)
    CheckIfValueIsSame(actuator_version, ACTUATOR_SOFTWARE_VERSION)

    test.log(
        """Step 7: Description*Record Supervisory Controller Software Version, as displayed by the UI."""
    )
    supervisory_version = GetSupervisorySoftwareVersion()

    test.log(
        """Expected Results:
    • If the version under test is from the Main Stream,
    recorded version number consists of four groups of digits separated by "."
    • If the version under test is from the Integration Stream,
    recorded version number consists of three groups of digits separated by "."""
    )
    CheckStreamVersionDigitGroup(get_stream)
    CheckIfValueIsSame(supervisory_version, SUPERVISORY_SOFTWARE_VERSION)

    test.log(
        """Step 8: Description*Record Power Controller Software Version, as displayed by the UI."""
    )
    power_controller_version = GetPowerControllerSoftwareVersion()

    test.log(
        """Expected Results:
    • If the version under test is from the Main Stream,
    recorded version number consists of four groups of digits separated by "."
    • If the version under test is from the Integration Stream,
    recorded version number consists of three groups of digits separated by "."
    • Recorded version number corresponds to software build intended for test."""
    )

    CheckStreamVersionDigitGroup(get_stream)
    CheckIfValueIsSame(power_controller_version, POWER_CONTROLLER_SOFTWARE_VERSION)

    test.log(
        """Step 9: Description*• Navigate from Dashboard to Left menu -> SYSTEM -> CONFIGURATION -> GENERAL
    • Record MACHINE NAME"""
    )

    OpenMenuItem(LEFT_MENU_OBJECT, ["SYSTEM", "CONFIGURATION", "GENERAL"])
    machine_name = GetMachineName()

    test.log("""Expected Results: MACHINE NAME is recorded.""")
    CheckIfValueIsNotEmpty(machine_name)

    test.log(
        """Step 10: Description*• Navigate from Dashboard to Left menu -> SYSTEM -> INFORMATION -> Event Log"""
    )

    OpenMenuItem(LEFT_MENU_OBJECT, ["SYSTEM", "INFORMATION", "Event Log"])

    test.log(
        """Expected Results: Events named "SOFTWARE VERSION CHANGE" show values in the 'To' column that identical to values recorded in steps 4, 5, and 6."""
    )
    CheckEventLogValues(controller_version)
    CheckEventLogValues(actuator_version)
    CheckEventLogValues(supervisory_version)
    CheckEventLogValues(power_controller_version)


if __name__ == "__main__":
    ExecutePreConditions()  # Ensure the system is in known ideal state before execution
    StartApplication()  # Start the AUT
    main()  # The main body corresponding to the Testcase.
    StopApplication()  # Stop the AUT
    ExecutePostConditions()  # Ensure the system is reverted to known ideal state post execution
