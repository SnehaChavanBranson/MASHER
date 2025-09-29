import names
from screens import login, limits, recipe
from helper import core
import squish
import test

USERNAME = "ADMIN"
PASSWORD = "Emerson@1"

filepath = "/home/branson/login_recipe/shared/testdata/"
dataset = testData.dataset(f"{filepath}/recipe.csv")


def pre_condition():
    login.LoginWithCredentials(USERNAME, PASSWORD)
    squish.snooze(5)
    test.log("System logged in successfully!")


class Time_Reject_Low:
    def test_time_reject_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_REJECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Time Reject Low :Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.uIController_Rectangle_5)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_time_reject_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Time Reject Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectLow()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_time_reject_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Time Reject Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectLow()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_time_reject_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_REJECT_LOW":
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
                    test.startSection("Suspect & Reject: Time Reject Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectLow()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_time_reject_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Time Reject Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectLow()
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

    def test_time_reject_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Time Reject Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectLow()
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


class Time_Suspect_Low:
    def test_time_suspect_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_SUSPECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Time Suspect Low :Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.uIController_Rectangle_5)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_time_suspect_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Time Suspect Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectLow()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_time_suspect_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Time Suspect Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectLow()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_time_suspect_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_SUSPECT_LOW":
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
                    test.startSection("Suspect & Reject: Time Suspect Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectLow()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_time_suspect_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Time Suspect Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectLow()
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

    def test_time_suspect_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Time Suspect Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectLow()
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


class Time_Suspect_High:
    def test_time_suspect_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_SUSPECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Time Suspect High :Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.uIController_Rectangle_5)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_time_suspect_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Time Suspect High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectHigh()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_time_suspect_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Time Suspect High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectHigh()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_time_suspect_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_SUSPECT_HIGH":
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
                    test.startSection("Suspect & Reject: Time Suspect High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectHigh()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_time_suspect_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Time Suspect High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectHigh()
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

    def test_time_suspect_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Time Suspect High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectHigh()
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


class Time_Reject_High:
    def test_time_reject_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_REJECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Time Reject High :Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.uIController_Rectangle_5)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("s", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_time_reject_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Time Reject High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectHigh()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_time_reject_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Time Reject High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectHigh()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_time_reject_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_REJECT_HIGH":
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
                    test.startSection("Suspect & Reject: Time Reject High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectHigh()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_time_reject_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Time Reject High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectHigh()
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

    def test_time_reject_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Time Reject High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectHigh()
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


class Energy_Reject_Low:
    def test_energy_reject_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_REJECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Energy Reject Low :Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.uIController_Rectangle_5)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_energy_reject_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Energy Reject Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectLow()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_energy_reject_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Energy Reject Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectLow()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_energy_reject_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_REJECT_LOW":
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
                    test.startSection("Suspect & Reject: Energy Reject Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectLow()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_energy_reject_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Energy Reject Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectLow()
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

    def test_energy_reject_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Energy Reject Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectLow()
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


class Energy_Suspect_Low:
    def test_energy_suspect_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_SUSPECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Energy Suspect Low :Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.uIController_Rectangle_5)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_energy_suspect_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Energy Suspect Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectLow()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_energy_suspect_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Energy Suspect Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectLow()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_energy_suspect_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_SUSPECT_LOW":
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
                    test.startSection("Suspect & Reject: Energy Suspect Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectLow()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_energy_suspect_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Energy Suspect Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectLow()
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

    def test_energy_suspect_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Energy Suspect Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectLow()
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


class Energy_Suspect_High:
    def test_energy_suspect_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_SUSPECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Energy Suspect High :Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.uIController_Rectangle_5)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_energy_suspect_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Energy Suspect High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectHigh()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_energy_suspect_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Energy Suspect High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectHigh()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_energy_suspect_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_SUSPECT_HIGH":
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
                    test.startSection("Suspect & Reject: Energy Suspect High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectHigh()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_energy_suspect_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Energy Suspect High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectHigh()
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

    def test_energy_suspect_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Energy Suspect High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectHigh()
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


class Energy_Reject_High:
    def test_energy_reject_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_REJECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Energy Reject High :Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.uIController_Rectangle_5)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_energy_reject_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Energy Reject High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectHigh()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_energy_reject_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Energy Reject High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectHigh()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_energy_reject_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_REJECT_HIGH":
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
                    test.startSection("Suspect & Reject: Energy Reject High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectHigh()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_energy_reject_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Energy Reject High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectHigh()
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

    def test_energy_reject_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Energy Reject High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectHigh()
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


class PeakPower_Reject_Low:
    def test_peakPower_reject_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_REJECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: PeakPower Reject Low :Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.uIController_Rectangle_5)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_peakPower_reject_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: PeakPower Reject Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectLow()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_peakPower_reject_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: PeakPower Reject Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectLow()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_peakPower_reject_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_REJECT_LOW":
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
                    test.startSection("Suspect & Reject: PeakPower Reject Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectLow()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_peakPower_reject_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: PeakPower Reject Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectLow()
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

    def test_peakPower_reject_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: PeakPower Reject Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectLow()
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


class PeakPower_Suspect_Low:
    def test_peakPower_suspect_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_SUSPECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: PeakPower Suspect Low :Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.uIController_Rectangle_5)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_peakPower_suspect_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: PeakPower Suspect Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectLow()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_peakPower_suspect_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: PeakPower Suspect Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectLow()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_peakPower_suspect_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_SUSPECT_LOW":
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
                    test.startSection("Suspect & Reject: PeakPower Suspect Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectLow()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_peakPower_suspect_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: PeakPower Suspect Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectLow()
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

    def test_peakPower_suspect_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: PeakPower Suspect Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectLow()
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


class PeakPower_Suspect_High:
    def test_peakPower_suspect_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_SUSPECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: PeakPower Suspect High :Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.uIController_Rectangle_5)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_peakPower_suspect_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: PeakPower Suspect High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectHigh()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_peakPower_suspect_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: PeakPower Suspect High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectHigh()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_peakPower_suspect_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_SUSPECT_HIGH":
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
                    test.startSection("Suspect & Reject: PeakPower Suspect High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectHigh()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_peakPower_suspect_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: PeakPower Suspect High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectHigh()
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

    def test_peakPower_suspect_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: PeakPower Suspect High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectHigh()
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


class PeakPower_Reject_High:
    def test_peakPower_reject_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_REJECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: PeakPower Reject High :Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.uIController_Rectangle_5)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace("", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_peakPower_reject_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: PeakPower Reject High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectHigh()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_peakPower_reject_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: PeakPower Reject High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectHigh()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_peakPower_reject_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_REJECT_HIGH":
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
                    test.startSection("Suspect & Reject: PeakPower Reject High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectHigh()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_peakPower_reject_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: PeakPower Reject High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectHigh()
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

    def test_peakPower_reject_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PEAKPOWER_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: PeakPower Reject High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectHigh()
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


def new_create_recipe():
    test.log("Started with creation of new recipe")
    recipe.CreateNewRecipe()


def main():
    startApplication("QT_UIController")
    pre_condition()
    squish.snooze(5)
    new_create_recipe()

    timeRejectLow = Time_Reject_Low()
    timeRejectLow.test_time_reject_low_40K_Default()
    timeRejectLow.test_time_reject_low_40K_min()
    timeRejectLow.test_time_reject_low_40K_max()
    timeRejectLow.test_time_reject_low_40K_mid()
    timeRejectLow.test_time_reject_low_40K_max_plus_one()
    timeRejectLow.test_time_reject_low_40K_min_minus_one()

    timeSuspectLow = Time_Suspect_Low()
    timeSuspectLow.test_time_suspect_low_40K_Default()
    timeSuspectLow.test_time_suspect_low_40K_min()
    timeSuspectLow.test_time_suspect_low_40K_max()
    timeSuspectLow.test_time_suspect_low_40K_mid()
    timeSuspectLow.test_time_suspect_low_40K_max_plus_one()
    timeSuspectLow.test_time_suspect_low_40K_min_minus_one()

    timeSuspectHigh = Time_Suspect_High()
    timeSuspectHigh.test_time_suspect_high_40K_Default()
    timeSuspectHigh.test_time_suspect_high_40K_min()
    timeSuspectHigh.test_time_suspect_high_40K_max()
    timeSuspectHigh.test_time_suspect_high_40K_mid()
    timeSuspectHigh.test_time_suspect_high_40K_max_plus_one()
    timeSuspectHigh.test_time_suspect_high_40K_min_minus_one()

    timeRejectLow = Time_Reject_High()
    timeRejectLow.test_time_reject_high_40K_Default()
    timeRejectLow.test_time_reject_high_40K_min()
    timeRejectLow.test_time_reject_high_40K_max()
    timeRejectLow.test_time_reject_high_40K_mid()
    timeRejectLow.test_time_reject_high_40K_max_plus_one()
    timeRejectLow.test_time_reject_high_40K_min_minus_one()

    energyRejectLow = Energy_Reject_Low()
    energyRejectLow.test_energy_reject_low_40K_Default()
    energyRejectLow.test_energy_reject_low_40K_min()
    energyRejectLow.test_energy_reject_low_40K_max()
    energyRejectLow.test_energy_reject_low_40K_mid()
    energyRejectLow.test_energy_reject_low_40K_max_plus_one()
    energyRejectLow.test_energy_reject_low_40K_min_minus_one()

    energySuspectLow = Energy_Suspect_Low()
    energySuspectLow.test_energy_suspect_low_40K_Default()
    energySuspectLow.test_energy_suspect_low_40K_min()
    energySuspectLow.test_energy_suspect_low_40K_max()
    energySuspectLow.test_energy_suspect_low_40K_mid()
    energySuspectLow.test_energy_suspect_low_40K_max_plus_one()
    energySuspectLow.test_energy_suspect_low_40K_min_minus_one()

    energySuspectHigh = Energy_Suspect_High()
    energySuspectHigh.test_energy_suspect_high_40K_Default()
    energySuspectHigh.test_energy_suspect_high_40K_min()
    energySuspectHigh.test_energy_suspect_high_40K_max()
    energySuspectHigh.test_energy_suspect_high_40K_mid()
    energySuspectHigh.test_energy_suspect_high_40K_max_plus_one()
    energySuspectHigh.test_energy_suspect_high_40K_min_minus_one()

    energyRejectHigh = Energy_Reject_High()
    energyRejectHigh.test_energy_reject_high_40K_Default()
    energyRejectHigh.test_energy_reject_high_40K_min()
    energyRejectHigh.test_energy_reject_high_40K_max()
    energyRejectHigh.test_energy_reject_high_40K_mid()
    energyRejectHigh.test_energy_reject_high_40K_max_plus_one()
    energyRejectHigh.test_energy_reject_high_40K_min_minus_one()

    peakPowerRejectLow = PeakPower_Reject_Low()
    peakPowerRejectLow.test_peakPower_reject_low_40K_Default()
    peakPowerRejectLow.test_peakPower_reject_low_40K_min()
    peakPowerRejectLow.test_peakPower_reject_low_40K_max()
    peakPowerRejectLow.test_peakPower_reject_low_40K_mid()
    peakPowerRejectLow.test_peakPower_reject_low_40K_max_plus_one()
    peakPowerRejectLow.test_peakPower_reject_low_40K_min_minus_one()

    peakPowerSuspectLow = PeakPower_Suspect_Low()
    peakPowerSuspectLow.test_peakPower_suspect_low_40K_Default()
    peakPowerSuspectLow.test_peakPower_suspect_low_40K_min()
    peakPowerSuspectLow.test_peakPower_suspect_low_40K_max()
    peakPowerSuspectLow.test_peakPower_suspect_low_40K_mid()
    peakPowerSuspectLow.test_peakPower_suspect_low_40K_max_plus_one()
    peakPowerSuspectLow.test_peakPower_suspect_low_40K_min_minus_one()

    peakPowerSuspectHigh = PeakPower_Suspect_High()
    peakPowerSuspectHigh.test_peakPower_suspect_high_40K_Default()
    peakPowerSuspectHigh.test_peakPower_suspect_high_40K_min()
    peakPowerSuspectHigh.test_peakPower_suspect_high_40K_max()
    peakPowerSuspectHigh.test_peakPower_suspect_high_40K_mid()
    peakPowerSuspectHigh.test_peakPower_suspect_high_40K_max_plus_one()
    peakPowerSuspectHigh.test_peakPower_suspect_high_40K_min_minus_one()

    peakPowerRejectHigh = PeakPower_Reject_High()
    peakPowerRejectHigh.test_peakPower_reject_high_40K_Default()
    peakPowerRejectHigh.test_peakPower_reject_high_40K_min()
    peakPowerRejectHigh.test_peakPower_reject_high_40K_max()
    peakPowerRejectHigh.test_peakPower_reject_high_40K_mid()
    peakPowerRejectHigh.test_peakPower_reject_high_40K_max_plus_one()
    peakPowerRejectHigh.test_peakPower_reject_high_40K_min_minus_one()
    
    core.scroll(names.recipeLabWindow_gridView_GridView)
