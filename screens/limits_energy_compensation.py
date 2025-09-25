from constants import names
import squish
import test
from helper import core

def energyCompensationTab() -> None:
    test.log("Clicked on energy compensation")
    core.ClickButton(squish.waitForObject(names.subrecipeTabBar_BransonTabButton_3))

def energyCompensationEnabledCard() -> None:
    test.log("Clicked on energy Compensation Enabled Card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_ENERGY_COMPENSATION_ENABLED_Text))

def enable_energyCompensationEnabledCard() -> None:
    test.log("Clicked on enabling energy Compensation Enabled Card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_energyEnableSwitch_BransonSwitch))


def energyCompensationMinimumValue() -> None:
    test.log("Clicked on energy Compensation Minimum Value")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_ENERGY_COMPENSATION_MINIMUM_VALUE_Text))

def energyCompensationMaximumValue() -> None:
    test.log("Clicked on energy Compensation Maximum Value")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_ENERGY_COMPENSATION_MAXIMUM_VALUE_Text))
