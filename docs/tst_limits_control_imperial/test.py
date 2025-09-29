# -*- coding: utf-8 -*-

import names
from screens import login, recipe, limits,limits_control
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
    squish.snooze(2)
    login.notification_reset()
    
def post_condition():
    login.logout()


def new_create_recipe():
    test.log("Started with creation of new recipe")
    recipe.CreateNewRecipe()
    
def test_limits_control():
    limits.limitsTab()
    squish.snooze(2)
    limits.controlTab()
    squish.snooze(2)
    limits.controlEnable()
    squish.snooze(2)
    limits_control.frequency_low_cutoff()
    limits_control.enable_frequency_low_cutoff()


class FrequencyLowCutOff:
    def test_frequency_low_cut_off_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_LOW_CUTOFF":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Limits Control: Frequency Low cut off: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        squish.snooze(2)
                        obj = waitForObject(names.recipeLabWindow_19450Hz_Text)
                        squish.snooze(2)
                        displayed_value = str(obj.text)
                        squish.snooze(2)
                        displayed_value_clean = displayed_value.replace("Hz", "").strip()
                        squish.snooze(2)
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()
                    
    def test_frequency_low_cut_off_40K_min(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "FREQUENCY_LOW_CUTOFF"                 
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Limits Control: Frequency Low cut off: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    squish.snooze(2)
                    limits_control.frequency_low_cutoff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_frequency_low_cut_off_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "FREQUENCY_LOW_CUTOFF"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Limits Control: Frequency Low cut off: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    squish.snooze(2)
                    limits_control.frequency_low_cutoff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_frequency_low_cut_off_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "FREQUENCY_LOW_CUTOFF"                 
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
                    test.startSection("Limits Control: Frequency Low cut off: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits_control.frequency_low_cutoff()
                    squish.snooze(2)
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_frequency_low_cut_off_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "FREQUENCY_LOW_CUTOFF"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Limits Control: Frequency Low cut off: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    squish.snooze(2)
                    limits_control.frequency_low_cutoff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_frequency_low_cut_off_min_minus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "FREQUENCY_LOW_CUTOFF"
                ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Limits Control: Frequency Low cut off: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits_control.frequency_low_cutoff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}") 


class PeakPowerCutOff:
    def test_peak_power_cut_off_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAK_POWER_CUTOFF":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Limits Control: Peak Power cut off: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        squish.snooze(2)
                        obj = waitForObject(names.recipeLabWindow_400W_Text)
                        squish.snooze(2)
                        displayed_value = str(obj.text)
                        squish.snooze(2)
                        displayed_value_clean = displayed_value.replace("W", "").strip()
                        squish.snooze(2)
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()
                    
    def test_peak_power_cut_off_40K_min(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "PEAK_POWER_CUTOFF"                 
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Limits Control: Peak Power cut off: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    squish.snooze(2)
                    limits_control.peakPowerCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_peak_power_cut_off_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "PEAK_POWER_CUTOFF"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Limits Control: Peak Power cut off: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    squish.snooze(2)
                    limits_control.peakPowerCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_peak_power_cut_off_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "PEAK_POWER_CUTOFF"                 
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
                    test.startSection("Limits Control: Peak Power cut off: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits_control.peakPowerCutOff()
                    squish.snooze(2)
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_peak_power_cut_off_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "PEAK_POWER_CUTOFF"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Limits Control: Peak Power: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    squish.snooze(2)
                    limits_control.peakPowerCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_peak_power_cut_off_min_minus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "PEAK_POWER_CUTOFF"
                ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Limits Control: Peak Power cut off: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits_control.peakPowerCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}")              
                    
                    
                    
                    
class FrequencyHighCutOff:
    def test_frequency_high_cut_off_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_HIGH_CUTOFF":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Limits Control: Frequency High cut off: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        squish.snooze(2)
                        obj = waitForObject(names.recipeLabWindow_20450Hz_Text)
                        squish.snooze(2)
                        displayed_value = str(obj.text)
                        squish.snooze(2)
                        displayed_value_clean = displayed_value.replace("Hz", "").strip()
                        squish.snooze(2)
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()
                    
    def test_frequency_high_cut_off_40K_min(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "FREQUENCY_HIGH_CUTOFF"                 
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Limits Control: Frequency High cut off: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    squish.snooze(2)
                    limits_control.frequencyHighCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_frequency_high_cut_off_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "FREQUENCY_HIGH_CUTOFF"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Limits Control: Frequency High cut off: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    squish.snooze(2)
                    limits_control.frequencyHighCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_frequency_high_cut_off_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "FREQUENCY_HIGH_CUTOFF"                 
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
                    test.startSection("Limits Control: Frequency High cut off: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits_control.frequencyHighCutOff()
                    squish.snooze(2)
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_frequency_high_cut_off_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "FREQUENCY_HIGH_CUTOFF"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Limits Control: Frequency High cut off: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    squish.snooze(2)
                    limits_control.frequencyHighCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_frequency_high_cut_off_min_minus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "FREQUENCY_HIGH_CUTOFF"
                ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Limits Control: Frequency Low cut off: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits_control.frequencyHighCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}") 


class EnergyCutOff:
    def test_energy_cut_off_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_CUTOFF":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Limits Control: Energy cut off: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        squish.snooze(2)
                        obj = waitForObject(names.recipeLabWindow_120000_0J_Text)
                        squish.snooze(2)
                        displayed_value = str(obj.text)
                        squish.snooze(2)
                        displayed_value_clean = displayed_value.replace(" J", "").strip()
                        squish.snooze(2)
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()
                    
    def test_energy_cut_off_40K_min(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ENERGY_CUTOFF"                 
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Limits Control: Energy cut off: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    squish.snooze(2)
                    limits_control.energyCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_energy_cut_off_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ENERGY_CUTOFF"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Limits Control: Energy cut off: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    squish.snooze(2)
                    limits_control.energyCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_energy_cut_off_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ENERGY_CUTOFF"                 
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
                    test.startSection("Limits Control: Energy cut off: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits_control.energyCutOff()
                    squish.snooze(2)
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_energy_cut_off_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ENERGY_CUTOFF"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Limits Control: Energy cut off: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    squish.snooze(2)
                    limits_control.energyCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_energy_cut_off_min_minus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ENERGY_CUTOFF"
                ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Limits Control: Energy cut off: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits_control.energyCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}") 
# uIController_loginFlick_Flickable

class GroundDetectCutOff:
    def test_ground_detect_cut_off_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "GROUND_DETECT_CUTOFF":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Limits Control: Energy cut off: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        squish.snooze(2)
                        obj = waitForObject(names.recipeLabWindow_0_001s_Text)
                        squish.snooze(2)
                        displayed_value = str(obj.text)
                        squish.snooze(2)
                        displayed_value_clean = displayed_value.replace(" s", "").strip()
                        squish.snooze(2)
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()
                    
    def test_ground_detect_cut_off_40K_min(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "GROUND_DETECT_CUTOFF"                 
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Limits Control: Energy cut off: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    squish.snooze(2)
                    limits_control.groundDetectCutOff()
                    squish.snooze(2)

                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_ground_detect_cut_off_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "GROUND_DETECT_CUTOFF"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Limits Control: Energy cut off: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    squish.snooze(2)
                    limits_control.groundDetectCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_ground_detect_cut_off_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "GROUND_DETECT_CUTOFF"                 
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
                    test.startSection("Limits Control: Energy cut off: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits_control.groundDetectCutOff()
                    squish.snooze(2)
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_ground_detect_cut_off_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "GROUND_DETECT_CUTOFF"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Limits Control: Energy cut off: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    squish.snooze(2)
                    limits_control.groundDetectCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_ground_detect_cut_off_min_minus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "GROUND_DETECT_CUTOFF"
                ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Limits Control: Energy cut off: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits_control.groundDetectCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}") 


class TimeCutOff:
    def test_time_cut_off_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_CUTOFF":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Limits Control: Time cut off: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        squish.snooze(2)
                        obj = waitForObject(names.recipeLabWindow_10_000s_Text)
                        squish.snooze(2)
                        displayed_value = str(obj.text)
                        squish.snooze(2)
                        displayed_value_clean = displayed_value.replace(" s", "").strip()
                        squish.snooze(2)
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()
                    
    def test_time_cut_off_40K_min(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "TIME_CUTOFF"                 
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Limits Control: Time cut off: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    squish.snooze(2)
                    limits_control.timeCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_time_cut_off_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "TIME_CUTOFF"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Limits Control: Time cut off: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    squish.snooze(2)
                    limits_control.timeCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_time_cut_off_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "TIME_CUTOFF"                 
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
                    test.startSection("Limits Control: Time cut off: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits_control.timeCutOff()
                    squish.snooze(2)
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_time_cut_off_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "TIME_CUTOFF"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Limits Control: Time cut off: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    squish.snooze(2)
                    limits_control.timeCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_time_cut_off_min_minus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "TIME_CUTOFF"
                ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Limits Control: Time cut off: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits_control.timeCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}") 


class AbsoluteDistanceCutOff:
    def test_absolute_distance_cut_off_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE_CUTOFF" and testData.field(row, "UNIT_TYPE") == "IMPERIAL":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Limits Control: Absolute Distance Cut off: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        squish.snooze(2)
                        obj = waitForObject(names.recipeLabWindow_0_0000in_Text)
                        squish.snooze(2)
                        displayed_value = str(obj.text)
                        squish.snooze(2)
                        displayed_value_clean = displayed_value.replace(" s", "").strip()
                        squish.snooze(2)
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value mauIController_loginFlick_Flickabletches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()
                    
    def test_absolute_distance_cut_off_40K_min(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE_CUTOFF" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"               
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Limits Control: Absolute Distance Cut off: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    squish.snooze(2)
                    limits_control.absoluteDistanceCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_absolute_distance_cut_off_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE_CUTOFF" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"                
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Limits Control: Absolute Distance Cut off: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    squish.snooze(2)
                    limits_control.absoluteDistanceCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_absolute_distance_cut_off_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE_CUTOFF" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAuIController_loginFlick_FlickableL"             
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
                    test.startSection("Limits Control: Absolute Distance Cut off: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits_control.absoluteDistanceCutOff()
                    squish.snooze(2)
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_absolute_distance_cut_off_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE_CUTOFF" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"              
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Limits Control: Absolute Distance Cut off: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    squish.snooze(2)
                    limits_control.absoluteDistanceCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popupuIController_loginFlick_Flickable did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_absolute_distance_cut_off_min_minus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE_CUTOFF" and
                testData.field(row, "UNIT_TYPE") == "IMPERIAL"
                ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Limits Control: Absolute Distance Cut off: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits_control.absoluteDistanceCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}") 

class CollapseDistanceCutOff:
    def test_collapse_distance_cut_off_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE_CUTOFF" and testData.field(row, "UNIT_TYPE") == "IMPERIAL":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Limits Control: Collapse Distance Cut off: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        squish.snooze(2)
                        obj = waitForObject(names.recipeLabWindow_0_0000in_Text_2)
                        squish.snooze(2)
                        displayed_value = str(obj.text)
                        squish.snooze(2)
                        displayed_value_clean = displayed_value.replace(" in", "").strip()
                        squish.snooze(2)
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()
                    
    def test_collapse_distance_cut_off_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE_CUTOFF" and testData.field(row, "UNIT_TYPE") == "IMPERIAL":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Limits Control: Collapse Distance Cut off: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    squish.snooze(2)
                    limits_control.collapseDistanceCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_collapse_distance_cut_off_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE_CUTOFF" and testData.field(row, "UNIT_TYPE") == "IMPERIAL":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Limits Control: Collapse Distance Cut off: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    squish.snooze(2)
                    limits_control.collapseDistanceCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_collapse_distance_cut_off_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE_CUTOFF" and testData.field(row, "UNIT_TYPE") == "IMPERIAL":
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
                    test.startSection("Limits Control: Collapse Distance Cut off: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits_control.collapseDistanceCutOff()
                    squish.snooze(2)
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_collapse_distance_cut_off_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE_CUTOFF" and testData.field(row, "UNIT_TYPE") == "IMPERIAL":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Limits Control: Collapse Distance Cut off: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    squish.snooze(2)
                    limits_control.collapseDistanceCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_collapse_distance_cut_off_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE_CUTOFF" and testData.field(row, "UNIT_TYPE") == "IMPERIAL":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Limits Control: Collapse Distance Cut off: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits_control.collapseDistanceCutOff()
                    squish.snooze(2)
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()
                    squish.snooze(2)
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}") 


def main():
    test.log("Enters into main function of weld process")
    
    startApplication("QT_UIController")
    squish.snooze(4)
    pre_condition()
    reset_notification()
    squish.snooze(3)
    new_create_recipe()
    squish.snooze(0.2)
    test_limits_control()
    
    # freq_low = FrequencyLowCutOff()
    # freq_low.test_frequency_low_cut_off_40K_Default()
    # freq_low.test_frequency_low_cut_off_40K_min()
    # freq_low.test_frequency_low_cut_off_40K_max()
    # freq_low.test_frequency_low_cut_off_40K_mid()
    # freq_low.test_frequency_low_cut_off_40K_max_plus_one()
    # freq_low.test_frequency_low_cut_off_40K_max_plus_one()
    #
    # limits_control.peakPowerCutOff()
    # limits_control.enable_peakPowerCutOff()
    #
    # peak_power = PeakPowerCutOff()
    # peak_power.test_peak_power_cut_off_40K_Default()
    # peak_power.test_peak_power_cut_off_40K_min()
    # peak_power.test_peak_power_cut_off_40K_max()
    # peak_power.test_peak_power_cut_off_40K_mid()
    # peak_power.test_peak_power_cut_off_40K_max_plus_one()
    # peak_power.test_peak_power_cut_off_min_minus_one()
    squish.snooze(0.2)

    # limits_control.frequencyHighCutOff()
    # squish.snooze(0.2)
    # limits_control.enable_frequencyHighCutOff()
    # squish.snooze(0.2)
    #
    # freq_high = FrequencyHighCutOff()
    # freq_high.test_frequency_high_cut_off_40K_Default()
    # freq_high.test_frequency_high_cut_off_40K_min()
    # freq_high.test_frequency_high_cut_off_40K_max()
    # freq_high.test_frequency_high_cut_off_40K_mid()
    # freq_high.test_frequency_high_cut_off_40K_max_plus_one()
    # freq_high.test_frequency_high_cut_off_min_minus_one()
    # core.scroll(names.recipeLabWindow_gridView_GridView)


    limits_control.energyCutOff()
    squish.snooze(0.2)
    limits_control.enable_energyCutOff()
    squish.snooze(0.2)
    
    energy = EnergyCutOff()
    energy.test_energy_cut_off_40K_Default()
    energy.test_energy_cut_off_40K_min()
    energy.test_energy_cut_off_40K_max()
    energy.test_energy_cut_off_40K_mid()
    energy.test_energy_cut_off_40K_max_plus_one()
    energy.test_energy_cut_off_min_minus_one()
    
    # core.scroll(names.recipeLabWindow_gridView_GridView)
    # core.scroll(names.recipeLabWindow_gridView_GridView)
    #
    # limits_control.groundDetectCutOff()
    # squish.snooze(0.2)
    # limits_control.enable_groundDetectCutOff()
    # squish.snooze(0.2)
    #
    #
    # ground_detect = GroundDetectCutOff()
    # ground_detect.test_ground_detect_cut_off_40K_Default()
    # ground_detect.test_ground_detect_cut_off_40K_min()
    # ground_detect.test_ground_detect_cut_off_40K_max()
    # ground_detect.test_ground_detect_cut_off_40K_mid()
    # ground_detect.test_ground_detect_cut_off_40K_max_plus_one()
    # ground_detect.test_ground_detect_cut_off_min_minus_one()
    #
    # limits_control.timeCutOff()
    # squish.snooze(0.2)
    # limits_control.enable_timeCutOff()
    # squish.snooze(0.2)
    #
    # time_cutoff = TimeCutOff()
    # time_cutoff.test_time_cut_off_40K_Default()
    # time_cutoff.test_time_cut_off_40K_min()
    # time_cutoff.test_time_cut_off_40K_max()
    # time_cutoff.test_time_cut_off_40K_mid()
    # time_cutoff.test_time_cut_off_40K_max_plus_one()
    # time_cutoff.test_time_cut_off_min_minus_one()
    #
    #
    # limits_control.absoluteDistanceCutOff()
    # squish.snooze(0.2)
    # limits_control.enable_absoluteDistanceCutOff()
    # squish.snooze(0.2)
    #
    # absolute_distance = AbsoluteDistanceCutOff()
    # absolute_distance.test_absolute_distance_cut_off_40K_Default()
    # absolute_distance.test_absolute_distance_cut_off_40K_min()
    # absolute_distance.test_absolute_distance_cut_off_40K_max()
    # absolute_distance.test_absolute_distance_cut_off_40K_mid()
    # absolute_distance.test_absolute_distance_cut_off_40K_max_plus_one()
    # absolute_distance.test_absolute_distance_cut_off_min_minus_one()
    #
    #
    # limits_control.collapseDistanceCutOff()
    # squish.snooze(0.2)
    # limits_control.enable_collapseDistanceCutOff()
    # squish.snooze(0.2)
    #
    # collapse_distance = CollapseDistanceCutOff()
    # collapse_distance.test_collapse_distance_cut_off_40K_Default()
    # collapse_distance.test_collapse_distance_cut_off_40K_min()
    # collapse_distance.test_collapse_distance_cut_off_40K_max()
    # collapse_distance.test_collapse_distance_cut_off_40K_mid()
    # collapse_distance.test_collapse_distance_cut_off_40K_max_plus_one()
    # collapse_distance.test_collapse_distance_cut_off_min_minus_one()

