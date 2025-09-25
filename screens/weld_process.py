# Weld Process Automation Script
# Author: Sneha Chavan
# Description: Automates UI interactions for Pretrigger and Afterburst tabs in the Weld Process screen using Squish.

# --- Pretrigger Tab Functions ---


def weldProcessTab():
    """
    Navigates to the Weld Process tab in the recipe screen.
    """
    test.log("Clicking on the weld process tab")
    core.ClickButton(squish.waitForObject(names.recipeTabBar_BransonTabButton_6))
    test.log("Finished clicking on the weld process tab")


def pretriggerTab():
    """
    Opens the Pretrigger card inside the Weld Process tab.
    """
    test.log("Clicking on the weld process: pretrigger card")
    core.ClickButton(squish.waitForObject(names.subrecipeTabBar_BransonTabButton_2))
    test.log("Finished clicking on the weld process: pretrigger card")


def pretriggerEnable():
    """
    Enables the Pretrigger feature in the Weld Process tab.
    """
    test.log("Clicking on the weld process: pretrigger enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_pretriggerEnableSwitch_BransonSwitch))
    test.log("Finished on the weld process: pretrigger enable")


def pretriggerDisable():
    """
    Disables the Pretrigger feature in the Weld Process tab.
    """
    test.log("Clicking on the weld process: pretrigger disable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_pretriggerEnableSwitch_BransonSwitch))
    test.log("Finished on the weld process: pretrigger disable")


def pretriggerAmplitudeEnterValue():
    """
    Clicks on the Pretrigger Amplitude field to enter a value.
    """
    test.log("Clicking on the weld process: pretrigger amplitude value to be entered")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_PRETRIGGER_AMPLITUDE_Text))
    test.log("Finished on the weld process: pretrigger amplitude value has been entered")


def pretriggerDistanceEnterValue():
    """
    Clicks on the Pretrigger Distance field to enter a value.
    """
    test.log("Clicking on the weld process: pretrigger distance value to be entered")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_PRETRIGGER_DISTANCE_Text))
    test.log("Finished on the weld process: pretrigger distance value has been entered")


def pretriggerTimeEnterValue():
    """
    Clicks on the Pretrigger Time field to enter a value.
    """
    test.log("Clicking on the weld process: pretrigger time value to be entered")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_PRETRIGGER_TIME_Text))
    test.log("Finished on the weld process: pretrigger time value has been entered")


def pretriggerStart_auto_radioButton():
    """
    Selects the 'Auto' radio button for Pretrigger start condition.
    """
    test.log("Clicking on the weld process: pretrigger start auto selected")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_radioButtonAuto_BransonRadioButton))


def pretriggerStart_distance_radioButton():
    """
    Selects the 'Distance' radio button for Pretrigger start condition.
    """
    test.log("Clicking on the weld process: pretrigger start distance selected")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_radioButtonDistance_BransonRadioButton))


def pretriggerStart_time_radioButton():
    """
    Selects the 'Time' radio button for Pretrigger start condition.
    """
    test.log("Clicking on the weld process: pretrigger start time selected")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_radioButtonTime_BransonRadioButton))


# --- Afterburst Tab Functions ---


def afterBurstTab():
    """
    Opens the Afterburst card inside the Weld Process tab.
    """
    test.log("Clicking on the afterburst tab")
    core.ClickButton(squish.waitForObject(names.subrecipeTabBar_BransonTabButton))
    test.log("Finished clicking on the afterburst tab")


def afterBurstEnable():
    """
    Enables the Afterburst feature in the Weld Process tab.
    """
    test.log("Clicking on the afterburst tab enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_afterburstSwitch_BransonSwitch))
    test.log("Finished clicking on afterburst tab enable")


def aftertriggerDisable():
    """
    Disables the Afterburst feature in the Weld Process tab.
    """
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_afterburstSwitch_BransonSwitch))


def afterburstDelayEnterValue():
    """
    Clicks on the Afterburst Delay field to enter a value and confirms with Done.
    """
    test.log("Clicking on the weld process: afterburst delay value to be entered")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_AFTERBURST_DELAY_Text))
    test.log("Finished on the weld process: afterburst delay value has been entered")
    recipe.DoneButton()


def afterburstTimeEnterValue():
    """
    Clicks on the Afterburst Time field to enter a value.
    """
    test.log("Clicking on the weld process: afterburst time value to be entered")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_AFTERBURST_TIME_Text))
    test.log("Finished on the weld process: afterburst time value has been entered")


def afterburstAmplitudeEnterValue():
    """
    Clicks on the Afterburst Amplitude field to enter a value.
    """
    test.log("Clicking on the weld process: afterburst amplitude value to be entered")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_AFTERBURST_AMPLITUDE_Text))
    test.log("Finished on the weld process: afterburst amplitude value has been entered")


def VerifyDisabledParams():
    """
    Placeholder for future implementation to verify disabled parameters.
    """
    pass
