# Unit Conversion Automation Script
# Author: Sneha Chavan
# Description: This particular file is part of the UI page (Change Metric) it includes all the functions to access in the particular page.
# Automates switching between Metric and Imperial units in the Branson system settings using Squish.

from helper import core
from constants import names
import squish
import test


def change_to_metric_unit():
    """
    Navigates to the system settings and switches the unit of measurement to Metric.
    Steps:
    - Opens the production window
    - Navigates to system options
    - Selects the Metric radio button
    - Saves the changes and confirms
    """
    test.log("entered into metric conversion")

    core.ClickButton(squish.waitForObject(names.productionWindowItem_rectBackground_Rectangle))
    core.ClickButton(squish.waitForObject(names.uIController_imageRightMenu_Image))
    core.ClickButton(squish.waitForObject(names.uIController_systemOptionImage_Image_3))

    test.log("Selecting metric radio button")
    core.ClickButton(squish.waitForObject(names.uIController_Metric_RadioButton))

    test.log("Clicking on save button")
    core.ClickButton(squish.waitForObject(names.uIController_SAVE_BransonPrimaryButton))

    test.log("Clicking on okay button")
    core.ClickButton(squish.waitForObject(names.oK_BransonPrimaryButton))

    test.log("Finished converting into metric conversion")


def change_to_imperial_unit():
    """
    Navigates to the system settings and switches the unit of measurement to Imperial.
    Steps:
    - Opens the production window
    - Navigates to system options
    - Selects the Imperial radio button
    - Saves the changes and confirms
    """
    test.log("entered into imperial conversion")

    core.ClickButton(squish.waitForObject(names.productionWindowItem_rectBackground_Rectangle))
    core.ClickButton(squish.waitForObject(names.uIController_imageRightMenu_Image))
    core.ClickButton(squish.waitForObject(names.uIController_systemOptionImage_Image_3))

    test.log("Selecting imperial radio button")
    core.ClickButton(squish.waitForObject(names.uIController_Imperial_RadioButton))

    test.log("Clicking on save button")
    core.ClickButton(squish.waitForObject(names.uIController_SAVE_BransonPrimaryButton))

    test.log("Clicking on okay button")
    core.ClickButton(squish.waitForObject(names.oK_BransonPrimaryButton))

    test.log("Finished converting into imperial conversion")
