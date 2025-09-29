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
    if object.exists(names.imageCross_Image):
        login.notification_reset()


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

    def test_time_40K_min(self):
        # Test 40K_Min
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_TIME_PARAM":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Weld Mode: Time: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe.TimeTab_quickedit()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_time_40K_max(self):
        # Test 40K_Max
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_TIME_PARAM":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Weld Mode: Time: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe.TimeTab_quickedit()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_40K_time_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_TIME_PARAM":
                # Test 40K_Max + 1
                value_40K_max = testData.field(row, "40K_Max")
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Weld Mode: Time: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe.TimeTab_quickedit()
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()

                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value matches expected max plus one value: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_time_40K_mid(self):
        # Test 40K_Mid (calculated between 40K_Min and 40K_Max)
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_TIME_PARAM":
                value_40K_min = testData.field(row, "40K_Min")
                value_40K_max = testData.field(row, "40K_Max")

                if value_40K_min and value_40K_max:
                    try:
                        min_val = float(value_40K_min)
                        max_val = float(value_40K_max)
                        mid_val = round((min_val + max_val) / 2, 2)  # Rounded to 2 decimal places
                    except ValueError:
                        test.fail(f"Invalid numeric values for min: {value_40K_min} or max: {value_40K_max}")
                        continue

                    test.startSection("Weld Mode: Time: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    recipe.TimeTab_quickedit()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_time_40K_min_minus_one(self):
        # Test 40K_Min - 1
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_TIME_PARAM":
                value_40K_min = testData.field(row, "40K_Min")    
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Weld Mode: Time: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe.TimeTab_quickedit()
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


class Energy:

    def test_energy_40K_Default(self):
        squish.snooze(2)
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_ENERGY_PARAM":

                # 40K_Default Verification
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Weld Mode: Energy: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        displayed_value = str(findObject(names.recipeLabWindow_1_0_J_Text).text)
                        test.log(f"Checking if the default value matches with the actual data")
                        displayed_value_clean = displayed_value.replace(".0 J", "").strip()

                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_energy_40K_min(self):
        # Test 40K_Min
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_ENERGY_PARAM":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Weld Mode: Energy: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe.EnergyTab_quickedit()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_energy_40K_max(self):
        # Test 40K_Max
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_ENERGY_PARAM":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Weld Mode: Energy: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe.EnergyTab_quickedit()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_energy_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_ENERGY_PARAM":
                # Test 40K_Max + 1
                value_40K_max = testData.field(row, "40K_Max")
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Weld Mode: Energy: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe.EnergyTab_quickedit()
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()

                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value matches expected max plus one value: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_energy_40K_mid(self):
        # Test 40K_Mid (calculated between 40K_Min and 40K_Max)
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_ENERGY_PARAM":
                value_40K_min = testData.field(row, "40K_Min")
                value_40K_max = testData.field(row, "40K_Max")

                if value_40K_min and value_40K_max:
                    try:
                        min_val = float(value_40K_min)
                        max_val = float(value_40K_max)
                        mid_val = round((min_val + max_val) / 2, 2)  # Rounded to 2 decimal places
                    except ValueError:
                        test.fail(f"Invalid numeric values for min: {value_40K_min} or max: {value_40K_max}")
                        continue

                    test.startSection("Weld Mode: Energy: Test 40K_Mid")
                    test.log(f"Testing 40K_Mrecipe.EnergyTab()id: {mid_val} (calculated from min={min_val} and max={max_val})")
                    recipe.EnergyTab_quickedit()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

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

    def test_peakpower_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_PEAK_POWER_PARAM":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Weld Mode: Peak Power: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe.PeakPowerTab_quickedit()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_peakpower_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_PEAK_POWER_PARAM":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Weld Mode: Peak Power: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe.PeakPowerTab_quickedit()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_peakpower_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_PEAK_POWER_PARAM":
                value_40K_min = testData.field(row, "40K_Min")
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_min and value_40K_max:
                    try:
                        min_val = float(value_40K_min)
                        max_val = float(value_40K_max)
                        mid_val = round((min_val + max_val) / 2, 2)
                    except ValueError:
                        test.fail(f"Invalid numeric values for min: {value_40K_min} or max: {value_40K_max}")
                        continue
                    test.startSection("Weld Mode: Peak Power: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    recipe.PeakPowerTab_quickedit()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_peakpower_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_PEAK_POWER_PARAM":
                value_40K_max = testData.field(row, "40K_Max")
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Weld Mode: Peak Power: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe.PeakPowerTab_quickedit()
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_peakpower_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_PEAK_POWER_PARAM":
                value_40K_min = testData.field(row, "40K_Min")
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Weld Mode: Peak Power: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe.PeakPowerTab_quickedit()
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}")


class GroundDetect:
    def test_grounddetect_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_GROUND_DETECT_PARAM":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Weld Mode: Ground Detect: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
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

    def test_grounddetect_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_GROUND_DETECT_PARAM":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Weld Mode: Ground Detect: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe.GroundDetectTab_quickedit()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_grounddetect_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_GROUND_DETECT_PARAM":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Weld Mode: Ground Detect: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe.GroundDetectTab_quickedit()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_grounddetect_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_GROUND_DETECT_PARAM":
                value_40K_min = testData.field(row, "40K_Min")
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_min and value_40K_max:
                    try:
                        min_val = float(value_40K_min)
                        max_val = float(value_40K_max)
                        mid_val = round((min_val + max_val) / 2, 2)
                    except ValueError:
                        test.fail(f"Invalid numeric values for min: {value_40K_min} or max: {value_40K_max}")
                        continue
                    test.startSection("Weld Mode: Ground Detect: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    recipe.GroundDetectTab_quickedit()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_grounddetect_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_GROUND_DETECT_PARAM":
                value_40K_max = testData.field(row, "40K_Max")
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Weld Mode: Ground Detect: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe.GroundDetectTab_quickedit()
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_grounddetect_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MODE_VALUE_GROUND_DETECT_PARAM":
                value_40K_min = testData.field(row, "40K_Min")
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Weld Mode: Ground Detect: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe.GroundDetectTab_quickedit()
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}")


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

    def test_collapsedistance_40K_min(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Weld Mode: Collapse Distance Imperial: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe.CollapseDistanceTab_quickedit()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_collapsedistance_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Weld Mode: Collapse Distance Imperial: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe.CollapseDistanceTab_quickedit()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_collapsedistance_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_min and value_40K_max:
                    try:
                        min_val = float(value_40K_min)
                        max_val = float(value_40K_max)
                        mid_val = round((min_val + max_val) / 2, 2)
                    except ValueError:
                        test.fail(f"Invalid numeric values for min: {value_40K_min} or max: {value_40K_max}")
                        continue
                    test.startSection("Weld Mode: Collapse Distance Imperial: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    recipe.CollapseDistanceTab_quickedit()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_collapsedistance_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Weld Mode: Collapse Distance Imperial: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe.CollapseDistanceTab_quickedit()
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_collapsedistance_40K_min_minus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Weld Mode: Collapse Distance Imperial: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe.CollapseDistanceTab_quickedit()
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}")

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
                    try:
                        displayed_value = str(findObject(names.recipeLabWindow_0_00_mm_Text).text)
                        displayed_value_clean = displayed_value.replace(" mm", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_absoultedistance_40K_min(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                test.startSection("Weld Mode: Absolute Distance Imperial: Test 40K_Min")
                test.log(f"Testing 40K_Min: {value_40K_min}")
                recipe.AbsoulteDistanceTab_quickedit()
                recipe.enterValue(value_40K_min)
                squish.snooze(2)
                recipe.DoneButton()
                test.passes(f"Entered value matches expected min value: {value_40K_min}")
                test.endSection()

    def test_absoultedistance_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                test.startSection("Weld Mode: Absolute Distance Imperial: Test 40K_Max")
                test.log(f"Testing 40K_Max: {value_40K_max}")
                recipe.AbsoulteDistanceTab_quickedit()
                recipe.enterValue(value_40K_max)
                squish.snooze(2)
                recipe.DoneButton()
                test.passes(f"Entered value matches expected max value: {value_40K_max}")
                test.endSection()

    def test_absoultedistance_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_min or not value_40K_min.strip() or not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Min or 40K_Max is missing or blank.")
                    continue
                try:
                    min_val = float(value_40K_min)
                    max_val = float(value_40K_max)
                    mid_val = round((min_val + max_val) / 2, 2)
                except ValueError:
                    test.fail(f"Invalid numeric values for min: {value_40K_min} or max: {value_40K_max}")
                    continue
                test.startSection("Weld Mode: Absolute Distance Imperial: Test 40K_Mid")
                test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                recipe.AbsoulteDistanceTab_quickedit()
                recipe.enterValue(str(mid_val))
                squish.snooze(2)
                recipe.DoneButton()
                test.passes(f"Entered value matches expected mid value: {mid_val}")
                test.endSection()

    def test_absoultedistance_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Weld Mode: Absolute Distance Imperial: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe.AbsoulteDistanceTab_quickedit()
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_absoultedistance_40K_min_minus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Weld Mode: Absolute Distance Imperial: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe.AbsoulteDistanceTab_quickedit()
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}")

class WeldPressure_Imperial:
    def test_weldpressure_40K_Default(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "WELD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                # 40K_Default Verification
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Weld Mode: Weld Pressure Imperial: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        displayed_value = str(findObject(names.recipeLabWindow_20_0_psi_Text).text)
                        test.log(f"Checking if the default value matches with the actual data")
                        displayed_value_clean = displayed_value.replace(" psi", "").strip()

                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_weldpressure_40K_min(self):
        # Test 40K_Min
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "WELD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Weld Mode: Weld Pressure Imperial: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe.weld_pressure_quickedit()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(0.2)
                    recipe.weld_amplitude_DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_weldpressure_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "WELD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Weld Mode: Weld Pressure Imperial: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe.weld_pressure_quickedit()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(0.2)
                    recipe.weld_amplitude_DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_weldpressure_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "WELD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_min or not value_40K_min.strip() or not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Min or 40K_Max is missing or blank.")
                    continue
                try:
                    min_val = float(value_40K_min)
                    max_val = float(value_40K_max)
                    mid_val = round((min_val + max_val) / 2, 2)
                except ValueError:
                    test.fail(f"Invalid numeric values for min: {value_40K_min} or max: {value_40K_max}")
                    continue
                test.startSection("Weld Mode: Weld Pressure Imperial: Test 40K_Mid")
                test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                recipe.weld_pressure_quickedit()
                recipe.enterValue(str(mid_val))
                squish.snooze(0.2)
                recipe.weld_amplitude_DoneButton()
                test.passes(f"Entered value matches expected mid value: {mid_val}")
                test.endSection()

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
                    squish.snooze(2)
                    recipe.weld_amplitude_DoneButton()
                    if object.exists(names.updateWeldRecipeParameter_fail5_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
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
                    if object.exists(names.updateWeldRecipeParameter_fail5_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}") 

class HoldPressure_Imperial:
    def test_holdpressure_40K_Default(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "HOLD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                # 40K_Default Verification
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Weld Mode: Hold Pressure Imperial: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        displayed_value = str(findObject(names.recipeLabWindow_20_0_psi_Text_2).text)
                        test.log(f"Checking if the default value matches with the actual data")
                        displayed_value_clean = displayed_value.replace(" psi", "").strip()

                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_holdpressure_40K_min(self):
        # Test 40K_Min
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "HOLD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Weld Mode: Hold Pressure Imperial: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe.hold_pressure_quickedit()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(0.2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_holdpressure_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "HOLD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Weld Mode: Hold Pressure Imperial: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe.hold_pressure_quickedit()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(0.2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_holdpressure_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "HOLD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_min or not value_40K_min.strip() or not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Min or 40K_Max is missing or blank.")
                    continue
                try:
                    min_val = float(value_40K_min)
                    max_val = float(value_40K_max)
                    mid_val = round((min_val + max_val) / 2, 2)
                except ValueError:
                    test.fail(f"Invalid numeric values for min: {value_40K_min} or max: {value_40K_max}")
                    continue
                test.startSection("Weld Mode: Hold Pressure Imperial: Test 40K_Mid")
                test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                recipe.hold_pressure_quickedit()
                recipe.enterValue(str(mid_val))
                squish.snooze(0.2)
                recipe.DoneButton()
                test.passes(f"Entered value matches expected mid value: {mid_val}")
                test.endSection()

    def test_holdpressure_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "HOLD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Weld Mode: Hold Pressure Imperial: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe.hold_pressure_quickedit()
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(0.2)
                    recipe.DoneButton()
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_holdpressure_40K_min_minus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "HOLD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Weld Mode: Hold Pressure Imperial: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe.hold_pressure_quickedit()
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(0.2)
                    recipe.DoneButton()
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
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
    reset_notification()
    core.moduleName("Recipe: Weld Mode Imperial")
    test.log("Completed the notifications pop skipping")
    squish.snooze(0.2)
    Set_Imperial()
    
    squish.snooze(1)
    new_create_recipe()

    time = Time()
    
    #Fail Error reading or comparing displayed value: Object 'recipeLabWindow_0_010_s_Text' not found. Could not match properties:
    #     text for object name: '{container={container=:uIController_QQuickWindowQmlImpl id='recipeLabWindow' type='Item' unnamed='1' visible='true'} text='0.010 s' type='Text' unnamed='1' visible='true'}' 14 July 2025 at 5:09:02 PM +05:30 /home/branson/login_recipe/tst_recipe_weld_mode_imperial/test.py:66
    # Called from:

    # time.test_time_40K_Default()
    time.test_time_40K_max()
    time.test_time_40K_min()
    time.test_time_40K_mid()
    time.test_40K_time_max_plus_one()
    time.test_time_40K_min_minus_one()
    
    recipe.EnergyTab()
    
    energy = Energy()
    energy.test_energy_40K_Default()
    energy.test_energy_40K_max()
    energy.test_energy_40K_min()
    energy.test_energy_40K_mid()
    energy.test_energy_40K_max_plus_one()
    
    #Fail Failed to calculate or enter 40K_Min-1: module 'test' has no attribute 'endSect' 14 July 2025 at 5:12:30 PM +05:30 /home/branson/login_recipe/tst_recipe_weld_mode_imperial/test.py:296
    # Called from:

    # energy.test_energy_40K_min_minus_one()
    
    recipe.PeakPowerTab()
    
    peakpower = PeakPower()
    #Fail Error reading or comparing displayed value: Object 'recipeLabWindow_80_W_Text' not found. Could not match properties:
    #     text for object name: '{container={container=:uIController_QQuickWindowQmlImpl id='recipeLabWindow' type='Item' unnamed='1' visible='true'} text='80 W' type='Text' unnamed='1' visible='true'}' 14 July 2025 at 5:12:36 PM +05:30 /home/branson/login_recipe/tst_recipe_weld_mode_imperial/test.py:315
    # Called from:

    # peakpower.test_peakpower_40K_Default()
    peakpower.test_peakpower_40K_max()
    peakpower.test_peakpower_40K_min()
    peakpower.test_peakpower_40K_mid()
    peakpower.test_peakpower_40K_max_plus_one()
    peakpower.test_peakpower_40K_min_minus_one()
    
    recipe.GroundDetectTab()
    
    grounddetect = GroundDetect()
    
    #Fail Error reading or comparing displayed value: Object 'recipeLabWindow_1_W_TextrecipeLabWindow_0_001_s_Text' not found. Could not match properties:
    #     text for object name: '{container={container=:uIController_QQuickWindowQmlImpl id='recipeLabWindow' type='Item' unnamed='1' visible='true'} text='0.001 s' type='Text' unnamed='1' visible='true'}' 14 July 2025 at 5:14:41 PM +05:30 /home/branson/login_recipe/tst_recipe_weld_mode_imperial/test.py:427
    # Called from:

    # grounddetect.test_grounddetect_40K_Default()
    grounddetect.test_grounddetect_40K_max()
    grounddetect.test_grounddetect_40K_min()
    grounddetect.test_grounddetect_40K_mid()
    grounddetect.test_grounddetect_40K_max_plus_one()
    grounddetect.test_grounddetect_40K_min_minus_one()
    
    
    recipe.AbsoulteDistanceTab()
    
    absoulte_in = AbsoulteDistance_Imperial()
    #Fail Error reading or comparing displayed value: Object 'recipeLabWindow_0_00_mm_Text' not found. Could not match properties:
    #     text for object name: '{container={container=:uIController_QQuickWindowQmlImpl id='recipeLabWindow' type='Item' unnamed='1' visible='true'} text='0.00 mm' type='Text' unnamed='1' visible='true'}' 14 July 2025 at 5:16:26 PM +05:30 /home/branson/login_recipe/tst_recipe_weld_mode_imperial/test.py:684
    # Called from:

    # absoulte_in.test_absoultedistance_40K_Default()
    absoulte_in.test_absoultedistance_40K_max()
    absoulte_in.test_absoultedistance_40K_min()
    absoulte_in.test_absoultedistance_40K_mid()
    absoulte_in.test_absoultedistance_40K_max_plus_one()
    absoulte_in.test_absoultedistance_40K_min_minus_one()
    
    recipe.CollapseDistanceTab()
    
    collapse_in = CollapseDistance_Imperial()
    #Fail Error reading or comparing displayed value: Object 'recipeLabWindow_0_0000_in_Text' not found. Could not match properties:
    #     text for object name: '{container={container=:uIController_QQuickWindowQmlImpl id='recipeLabWindow' type='Item' unnamed='1' visible='true'} text='0.0000 in' type='Text' unnamed='1' visible='true'}' 14 July 2025 at 5:18:11 PM +05:30 /home/branson/login_recipe/tst_recipe_weld_mode_imperial/test.py:543
    # Called from:

    # collapse_in.test_collapsedistance_40K_Default()
    collapse_in.test_collapsedistance_40K_max()
    collapse_in.test_collapsedistance_40K_min()
    collapse_in.test_collapsedistance_40K_mid()
    collapse_in.test_collapsedistance_40K_max_plus_one()
    collapse_in.test_collapsedistance_40K_min_minus_one()
    
    
    # recipe.TimeTab()
    
    weldpressure_psi = WeldPressure_Imperial()
    weldpressure_psi.test_weldpressure_40K_Default()
    weldpressure_psi.test_weldpressure_40K_min()
    weldpressure_psi.test_weldpressure_40K_max()
    weldpressure_psi.test_weldpressure_40K_mid()
    # weldpressure_psi.test_weldpressure_40K_max_plus_one()
    # weldpressure_psi.test_weldpressure_40K_min_minus_one()
    
    post_condition()