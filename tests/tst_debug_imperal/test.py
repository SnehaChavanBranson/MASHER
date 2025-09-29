# -*- coding: utf-8 -*-

import names
from screens import login, recipe, user_setting
import squish
from helper import core

USERNAME = "ADMIN"
PASSWORD = "Emerson@1"

filepath = "/home/branson/login_recipe/shared/testdata/"
dataset = testData.dataset(f"{filepath}/recipe.csv")


def pre_condition():
    login.LoginWithCredentials(USERNAME, PASSWORD)
    test.log("System logged in successfully!")
    # if object.exists(names.imageCross_Image):
    #     login.notification_reset()


def reset_notification():
    squish.snooze(0.2)
    login.notification_reset()


def Set_Imperial():
    user_setting.change_to_imperial_unit()

    
def post_condition():
    login.logout()


def new_create_recipe():
    test.log("Started with creation of new recipe")
    recipe.CreateNewRecipe()



class Time:
    def test_time_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_TIME_PARAM":

                # 40K_Default Verification
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Weld Mode: Time: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        displayed_value = str(findObject(names.recipeLabWindow_0_010_s_Text).text)
                        test.log(f"Checking if the default value matches with the actual data")
                        displayed_value_clean = displayed_value.replace(" s", "").strip()

                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()
class Energy:
        def test_energy_40K_min_minus_one(self):
        # Test 40K_Min - 1
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_ENERGY_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Weld Mode: Energy: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe.EnergyTab_quickedit()
                        recipe.enterValue(value_40K_min_minus_one)
                        squish.snooze(2)
                        recipe.DoneButton()
    
                        if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                            test.passes(f"Entered value matches expected max minus one value: {value_40K_min_minus_one}")
                            core.ClickButton(names.oK_BransonPrimaryButton)
                        else:
                            test.fail("Expected validation popup did not appear.")
                        test.endSection()
    
                    except Exception as e:
                        test.fail(f"Failed to calculate or enter 40K_Min-1: {e}")


class PeakPower:
    def test_peakpower_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_PEAK_POWER_PARAM":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Weld Mode: Peak Power: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    squish.snooze(2)
                    try:
                        displayed_value = str(findObject(names.recipeLabWindow_80_W_Text).text)
                        displayed_value_clean = displayed_value.replace(" W", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

class GroundDetect:
    def test_grounddetect_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_GROUND_DETECT_PARAM":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Weld Mode: Ground Detect: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    squish.snooze(2)
                    try:
                        displayed_value = str(findObject(names.recipeLabWindow_1_W_TextrecipeLabWindow_0_001_s_Text).text)
                        displayed_value_clean = displayed_value.replace(" s", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

class AbsoulteDistance_Imperial:
    def test_absoultedistance_40K_Default(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Weld Mode: Absolute Distance Imperial: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    squish.snooze(2)
                    try:
                        displayed_value = str(findObject(names.recipeLabWindow_0_0000_in_Text).text)
                        displayed_value_clean = displayed_value.replace(" in", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

class CollapseDistance_Imperial:
    def test_collapsedistance_40K_Default(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Weld Mode: Collapse Distance Imperial: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    squish.snooze(2)
                    try:
                        displayed_value = str(findObject(names.recipeLabWindow_0_0000_in_Text).text)
                        displayed_value_clean = displayed_value.replace(" in", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSec    # mouseClick(waitForObject(names.recipeTabBar_BransonTabButton), 39, 17, Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)tion()


class WeldPressure_Imperial:
        
        def test_weldpressure_40K_max_plus_one(self):
            for row in dataset:
                if (
                    testData.field(row, "EXECUTION") == "TRUE" and
                    testData.field(row, "Param_ID") == "WELD PRESSURE" and
                    testData.field(row, "UNIT_TYPE") == "IMPERIAL"
                ):
                    value_40K_max = testData.field(row, "40K_Max")
                    if not value_40K_max or not value_40K_max.strip():
                        test.log("Skipping row: 40K_Max value is missing or blank.")
                        continue
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Weld Mode: Weld Pressure Imperial: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe.weld_pressure_quickedit()
                        recipe.enterValue(value_40K_max_plus_one)
                        squish.snooze(0.2)
                        recipe.weld_amplitude_DoneButton()
                        squish.snooze(2)
                        if object.exists(names.updateWeldRecipeParameter_fail5_Text):
                            test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                            core.ClickButton(names.oK_BransonPrimaryButton)
                        else:
                            test.endSection()
                    except Exception as e:
                        test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

        def test_weldpressure_40K_min_minus_one(self):
            for row in dataset:
                if (
                    testData.field(row, "EXECUTION") == "TRUE" and
                    testData.field(row, "Param_ID") == "WELD PRESSURE" and
                    testData.field(row, "UNIT_TYPE") == "IMPERIAL"
                ):
                    value_40K_min = testData.field(row, "40K_Min")
                    if not value_40K_min or not value_40K_min.strip():
                        test.log("Skipping row: 40K_Min value is missing or blank.")
                        continue
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Weld Mode: Weld Pressure Imperial: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe.weld_pressure_quickedit()
                        recipe.enterValue(value_40K_min_minus_one)
                        squish.snooze(0.2)
                        recipe.weld_amplitude_DoneButton()
                        squish.snooze(2)
                        if object.exists(names.updateWeldRecipeParameter_fail5_Text):
                            test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                            core.ClickButton(names.oK_BransonPrimaryButton)
                        else:
                            test.fail("Expected validation popup did not appear.")
                        test.endSection()
                    except Exception as e:
                        test.fail(f"Failed to calculate or enter 40K_Min-1: {e}") 
                                                  
def main():
    test.log("Starting to log into the system")
    startApplication("QT_UIController")
    pre_condition()
    # reset_notification()
    core.moduleName("Recipe: Recipe Imperial")
    test.log("Completed the notifications pop skipping")
    squish.snooze(0.2)
    Set_Imperial()
    
    squish.snooze(1)
    new_create_recipe()
    
    time = Time()
    
    time.test_time_40K_Default()
    
    recipe.EnergyTab()
    
    energy = Energy()
    energy.test_energy_40K_min_minus_one()
    
    
    recipe.PeakPowerTab()
    
    peakpower = PeakPower()
    peakpower.test_peakpower_40K_Default()
    
    
    recipe.GroundDetectTab()
    
    grounddetect = GroundDetect()
    grounddetect.test_grounddetect_40K_Default()
    
    recipe.AbsoulteDistanceTab()
    
    absoulte_in = AbsoulteDistance_Imperial()
    absoulte_in.test_absoultedistance_40K_Default()
    
    recipe.CollapseDistanceTab()
    
    collapse_in = CollapseDistance_Imperial()
    collapse_in.test_collapsedistance_40K_Default()
    
    weldpressure_psi = WeldPressure_Imperial()
    weldpressure_psi.test_weldpressure_40K_max_plus_one()
    weldpressure_psi.test_weldpressure_40K_min_minus_one()
    
    
    
    
    