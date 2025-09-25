# -*- coding: utf-8 -*-
from helper import core
from constants import names
import squish
import test

"""_summary_            
This module contains functions to interact with the control tab and its options in the recipe lab window.
Each function logs its action and performs a button click using Squish.
"""


def controlTab():
    """Clicks on the control tab in the recipe tab bar.

    Logs the action and performs a button click using Squish.
    """
    test.log("Clicking on control tab")
    core.ClickButton(squish.waitForObject(names.subrecipeTabBar_BransonTabButton))


def controlCard():
    """Clicks on the control card in the recipe lab window.

    Logs the action and performs a button click using Squish.
    """
    test.log("Clicking on the control card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_CONTROL_Text))


def enableControl():
    """Enables the control card switch in the recipe lab window.

    Logs the action and performs a button click using Squish.
    """
    test.log("Enable control card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_controlSwitch_BransonSwitch))


def frequency_low_cutoff():
    """Clicks on the frequency low cutoff option in the recipe lab window.

    Logs the action and performs a button click using Squish.
    """
    test.log("Clicking on frequency low cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_FREQUENCY_LOW_CUTOFF_Text))


def enable_frequency_low_cutoff():
    """Enables the frequency low cutoff switch in the recipe lab window.

    Logs the action and performs a button click using Squish.
    """
    test.log("Enable frequency low cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_switchControl_BransonSwitch))


def peakPowerCutOff():
    """Clicks on the peak power cutoff option in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("Clicking on the weld limits tab: control: peak power cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_PEAK_POWER_CUTOFF_Text))


def enable_peakPowerCutOff():
    """Enables the peak power cutoff switch in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("enable peak power cut off")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_switchControl_BransonSwitch_2))


def frequencyHighCutOff():
    """Clicks on the frequency high cutoff option in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("Clicking on the weld limits tab: control: FREQUENCY HIGH cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_FREQUENCY_HIGH_CUTOFF_Text))


def enable_frequencyHighCutOff():
    """Enables the frequency high cutoff switch in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("enable FREQUENCY HIGH cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_switchControl_BransonSwitch_3))


def energyCutOff():
    """Clicks on the energy cutoff option in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("Clicking on the weld limits tab: control: energy cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_ENERGY_CUTOFF_Text))


def enable_energyCutOff():
    """Enables the energy cutoff switch in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("enable energy cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_switchControl_BransonSwitch_4))


def groundDetectCutOff():
    """Clicks on the ground detect cutoff option in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("Clicking on the weld limits tab: control: ground detect cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_GROUND_DETECT_CUTOFF_Text))


def enable_groundDetectCutOff():
    """Enables the ground detect cutoff switch in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("enable ground detect  cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_switchControl_BransonSwitch_5))


def timeCutOff():
    """Clicks on the time cutoff option in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("Clicking on the weld limits tab: control: time cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_TIME_CUTOFF_Text))


def enable_timeCutOff():
    """Enables the time cutoff switch in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("enable time cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_switchControl_BransonSwitch_6))


def absoluteDistanceCutOff():
    """Clicks on the absolute distance cutoff option in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("Clicking on the weld limits tab: control: absolute distance cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_ABSOLUTE_DISTANCE_CUTOFF_Text))


def enable_absoluteDistanceCutOff():
    """Enables the absolute distance cutoff switch in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("enable absolute distance cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_switchControl_BransonSwitch_2))


def collapseDistanceCutOff():
    """Clicks on the collapse distance cutoff option in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("Clicking on the weld limits tab: control: collapse distance cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_COLLAPSE_DISTANCE_CUTOFF_Text))


def enable_collapseDistanceCutOff():
    """Enables the collapse distance cutoff switch in the weld limits tab.

    Logs the action and performs a button click using Squish.
    """
    test.log("enable collapse distance cutoff")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_switchControl_BransonSwitch))
