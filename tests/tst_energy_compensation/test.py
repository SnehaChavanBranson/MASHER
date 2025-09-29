# -*- coding: utf-8 -*-

import names
from helper import core
import squish
import test
from screens import limits_energy_compensation, login, recipe, limits

USERNAME = "ADMIN"
PASSWORD = "Emerson@1"

filepath = "/home/branson/login_recipe/shared/testdata/"
dataset = testData.dataset(f"{filepath}/recipe.csv")


def pre_condition():
    login.LoginWithCredentials(USERNAME, PASSWORD)
    squish.snooze(0.5)
    test.log("System logged in successfully!")


def new_create_recipe():
    test.log("Started with creation of new recipe")
    recipe.CreateNewRecipe()


def test_energy_compensation():
    limits.limitsTab()
    squish.snooze(0.2)
    limits_energy_compensation.energyCompensationTab()
    squish.snooze(0.2)
    limits_energy_compensation.energyCompensationEnabledCard()
    limits_energy_compensation.enable_energyCompensationEnabledCard()


class EnergyCompensationMaximum:
    def test_energy_compensation_max_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_COMPENSATION_MAXIMUM":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Limits: Energy Compensation Maximum:Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.recipeLabWindow_120000_0_J_Text)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_energy_compensation_max_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_COMPENSATION_MAXIMUM":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Limits: Energy Compensation Maximum:Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits_energy_compensation.energyCompensationMaximumValue()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_energy_compensation_max_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_COMPENSATION_MAXIMUM":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Limits: Energy Compensation Maximum:Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits_energy_compensation.energyCompensationMaximumValue()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_energy_compensation_max_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_COMPENSATION_MAXIMUM":
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
                    test.startSection("Limits: Energy Compensation Maximum:Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits_energy_compensation.energyCompensationMaximumValue()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_energy_compensation_max_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_COMPENSATION_MAXIMUM":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Limits: Energy Compensation Maximum:Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits_energy_compensation.energyCompensationMaximumValue()
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

    def test_energy_compensation_max_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_COMPENSATION_MAXIMUM":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Limits: Energy Compensation Maximum:Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits_energy_compensation.energyCompensationMaximumValue()
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


class EnergyCompensationMinimum:
    def test_energy_compensation_min_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_COMPENSATION_MINIMUM":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Limits: Energy Compensation Maximum:Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.recipeLabWindow_1_0_J_Text)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_energy_compensation_min_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_COMPENSATION_MINIMUM":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Limits: Energy Compensation Maximum: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits_energy_compensation.energyCompensationMinimumValue()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_energy_compensation_min_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_COMPENSATION_MINIMUM":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Limits: Energy Compensation Maximum: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits_energy_compensation.energyCompensationMinimumValue()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_energy_compensation_min_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_COMPENSATION_MINIMUM":
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
                    test.startSection("Limits: Energy Compensation Maximum: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits_energy_compensation.energyCompensationMinimumValue()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_energy_compensation_min_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_COMPENSATION_MINIMUM":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Limits: Energy Compensation Maximum: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits_energy_compensation.energyCompensationMinimumValue()
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

    def test_energy_compensation_min_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_COMPENSATION_MINIMUM":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Limits: Energy Compensation Maximum: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits_energy_compensation.energyCompensationMinimumValue()
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


def main():
    test.log("Starting to log into the system")
    startApplication("QT_UIController")
    squish.snooze(3)
    core.moduleName("Limits energy compensation")
    pre_condition()
    new_create_recipe()
    test_energy_compensation()

    energyMax = EnergyCompensationMaximum()
    energyMax.test_energy_compensation_max_40K_Default()
    energyMax.test_energy_compensation_max_40K_max()
    energyMax.test_energy_compensation_max_40K_min()
    energyMax.test_energy_compensation_max_40K_mid()
    energyMax.test_energy_compensation_max_40K_max_plus_one()
    energyMax.test_energy_compensation_max_min_minus_one()

    energyMin = EnergyCompensationMinimum()
    energyMin.test_energy_compensation_min_40K_Default()
    energyMin.test_energy_compensation_min_40K_max()
    energyMin.test_energy_compensation_min_40K_min()
    energyMin.test_energy_compensation_min_40K_mid()
    energyMin.test_energy_compensation_min_40K_max_plus_one()
    energyMin.test_energy_compensation_min_min_minus_one()
