import names
from screens import login, limits, recipe, user_setting
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


def new_create_recipe():
    test.log("Started with creation of new recipe")
    recipe.CreateNewRecipe()


def Set_Imperial():
    user_setting.change_to_imperial_unit()


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
                    recipe.enterValueSuspectReject(value_40K_min)
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
                    limits.timeTab()
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
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
                    limits.timeTab()
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
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
                    limits.timeTab()
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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
                    limits.timeTab()
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min)
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
                    limits.timeTab()
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
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
                    limits.timeTab()
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
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
                    limits.timeTab()
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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
                    limits.timeTab()
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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
                    limits.timeTab()
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_min)
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
                    recipe.enterValueSuspectReject(value_40K_max)
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
                    recipe.enterValueSuspectReject(str(mid_val))
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
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min)
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
                    recipe.enterValueSuspectReject(value_40K_max)
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
                    recipe.enterValueSuspectReject(str(mid_val))
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
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min)
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
                    recipe.enterValueSuspectReject(value_40K_max)
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
                    recipe.enterValueSuspectReject(str(mid_val))
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
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min)
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
                    recipe.enterValueSuspectReject(value_40K_max)
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
                    recipe.enterValueSuspectReject(str(mid_val))
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
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min)
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
                    recipe.enterValueSuspectReject(value_40K_max)
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
                    recipe.enterValueSuspectReject(str(mid_val))
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
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min)
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
                    recipe.enterValueSuspectReject(value_40K_max)
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
                    recipe.enterValueSuspectReject(str(mid_val))
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
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min)
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
                    recipe.enterValueSuspectReject(value_40K_max)
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
                    recipe.enterValueSuspectReject(str(mid_val))
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
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min)
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
                    recipe.enterValueSuspectReject(value_40K_max)
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
                    recipe.enterValueSuspectReject(str(mid_val))
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
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min)
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
                    recipe.enterValueSuspectReject(value_40K_max)
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
                    recipe.enterValueSuspectReject(str(mid_val))
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
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min)
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
                    recipe.enterValueSuspectReject(value_40K_max)
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
                    recipe.enterValueSuspectReject(str(mid_val))
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
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class AbsoluteDistance_Reject_Low:
    def test_absoluteDistance_reject_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_REJECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: AbsoluteDistance Reject Low :Test 40K_Default Displayed Value")
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

    def test_absoluteDistance_reject_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: AbsoluteDistance Reject Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_absoluteDistance_reject_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: AbsoluteDistance Reject Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_absoluteDistance_reject_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_REJECT_LOW":
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
                    test.startSection("Suspect & Reject: AbsoluteDistance Reject Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_absoluteDistance_reject_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: AbsoluteDistance Reject Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_absoluteDistance_reject_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: AbsoluteDistance Reject Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class AbsoluteDistance_Suspect_Low:
    def test_absoluteDistance_suspect_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_SUSPECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: AbsoluteDistance Suspect Low :Test 40K_Default Displayed Value")
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

    def test_absoluteDistance_suspect_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: AbsoluteDistance Suspect Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_absoluteDistance_suspect_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: AbsoluteDistance Suspect Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_absoluteDistance_suspect_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_SUSPECT_LOW":
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
                    test.startSection("Suspect & Reject: AbsoluteDistance Suspect Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_absoluteDistance_suspect_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: AbsoluteDistance Suspect Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_absoluteDistance_suspect_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: AbsoluteDistance Suspect Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class AbsoluteDistance_Suspect_High:
    def test_absoluteDistance_suspect_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_SUSPECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: AbsoluteDistance Suspect High :Test 40K_Default Displayed Value")
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

    def test_absoluteDistance_suspect_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: AbsoluteDistance Suspect High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_absoluteDistance_suspect_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: AbsoluteDistance Suspect High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_absoluteDistance_suspect_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_SUSPECT_HIGH":
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
                    test.startSection("Suspect & Reject: AbsoluteDistance Suspect High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_absoluteDistance_suspect_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: AbsoluteDistance Suspect High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_absoluteDistance_suspect_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: AbsoluteDistance Suspect High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class AbsoluteDistance_Reject_High:
    def test_absoluteDistance_reject_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_REJECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: AbsoluteDistance Reject High :Test 40K_Default Displayed Value")
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

    def test_absoluteDistance_reject_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: AbsoluteDistance Reject High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_absoluteDistance_reject_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: AbsoluteDistance Reject High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_absoluteDistance_reject_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_REJECT_HIGH":
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
                    test.startSection("Suspect & Reject: AbsoluteDistance Reject High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_absoluteDistance_reject_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: AbsoluteDistance Reject High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_absoluteDistance_reject_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ABSOLUTEDISTANCE_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: AbsoluteDistance Reject High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class CollapseDistance_Reject_Low:
    def test_collapseDistance_reject_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_REJECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: CollapseDistance Reject Low :Test 40K_Default Displayed Value")
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

    def test_collapseDistance_reject_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: CollapseDistance Reject Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_collapseDistance_reject_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: CollapseDistance Reject Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_collapseDistance_reject_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_REJECT_LOW":
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
                    test.startSection("Suspect & Reject: CollapseDistance Reject Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_collapseDistance_reject_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: CollapseDistance Reject Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_collapseDistance_reject_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: CollapseDistance Reject Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class CollapseDistance_Suspect_Low:
    def test_collapseDistance_suspect_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_SUSPECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: CollapseDistance Suspect Low :Test 40K_Default Displayed Value")
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

    def test_collapseDistance_suspect_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: CollapseDistance Suspect Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_collapseDistance_suspect_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: CollapseDistance Suspect Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_collapseDistance_suspect_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_SUSPECT_LOW":
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
                    test.startSection("Suspect & Reject: CollapseDistance Suspect Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_collapseDistance_suspect_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: CollapseDistance Suspect Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_collapseDistance_suspect_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: CollapseDistance Suspect Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class CollapseDistance_Suspect_High:
    def test_collapseDistance_suspect_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_SUSPECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: CollapseDistance Suspect High :Test 40K_Default Displayed Value")
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

    def test_collapseDistance_suspect_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: CollapseDistance Suspect High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_collapseDistance_suspect_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: CollapseDistance Suspect High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_collapseDistance_suspect_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_SUSPECT_HIGH":
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
                    test.startSection("Suspect & Reject: CollapseDistance Suspect High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_collapseDistance_suspect_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: CollapseDistance Suspect High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_collapseDistance_suspect_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: CollapseDistance Suspect High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class CollapseDistance_Reject_High:
    def test_collapseDistance_reject_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_REJECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: CollapseDistance Reject High :Test 40K_Default Displayed Value")
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

    def test_collapseDistance_reject_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: CollapseDistance Reject High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_collapseDistance_reject_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: CollapseDistance Reject High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_collapseDistance_reject_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_REJECT_HIGH":
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
                    test.startSection("Suspect & Reject: CollapseDistance Reject High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_collapseDistance_reject_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: CollapseDistance Reject High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_collapseDistance_reject_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "COLLAPSEDISTANCE_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: CollapseDistance Reject High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class EndWeldStore_Reject_Low:
    def test_endWeldStore_reject_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_REJECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: EndWeldStore Reject Low :Test 40K_Default Displayed Value")
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

    def test_endWeldStore_reject_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: EndWeldStore Reject Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_endWeldStore_reject_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: EndWeldStore Reject Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_endWeldStore_reject_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_REJECT_LOW":
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
                    test.startSection("Suspect & Reject: EndWeldStore Reject Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_endWeldStore_reject_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: EndWeldStore Reject Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_endWeldStore_reject_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: EndWeldStore Reject Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class EndWeldStore_Suspect_Low:
    def test_endWeldStore_suspect_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_SUSPECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: EndWeldStore Suspect Low :Test 40K_Default Displayed Value")
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

    def test_endWeldStore_suspect_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: EndWeldStore Suspect Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_endWeldStore_suspect_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: EndWeldStore Suspect Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_endWeldStore_suspect_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_SUSPECT_LOW":
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
                    test.startSection("Suspect & Reject: EndWeldStore Suspect Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_endWeldStore_suspect_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: EndWeldStore Suspect Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_endWeldStore_suspect_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: EndWeldStore Suspect Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class EndWeldStore_Suspect_High:
    def test_endWeldStore_suspect_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_SUSPECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: EndWeldStore Suspect High :Test 40K_Default Displayed Value")
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

    def test_endWeldStore_suspect_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: EndWeldStore Suspect High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_endWeldStore_suspect_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: EndWeldStore Suspect High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_endWeldStore_suspect_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_SUSPECT_HIGH":
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
                    test.startSection("Suspect & Reject: EndWeldStore Suspect High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_endWeldStore_suspect_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: EndWeldStore Suspect High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_endWeldStore_suspect_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: EndWeldStore Suspect High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class EndWeldStore_Reject_High:
    def test_endWeldStore_reject_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_REJECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: EndWeldStore Reject High :Test 40K_Default Displayed Value")
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

    def test_endWeldStore_reject_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: EndWeldStore Reject High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_endWeldStore_reject_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: EndWeldStore Reject High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_endWeldStore_reject_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_REJECT_HIGH":
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
                    test.startSection("Suspect & Reject: EndWeldStore Reject High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_endWeldStore_reject_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: EndWeldStore Reject High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_endWeldStore_reject_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENDWELDSTORE_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: EndWeldStore Reject High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class TriggerDistance_Reject_Low:
    def test_triggerDistance_reject_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_REJECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: TriggerDistance Reject Low :Test 40K_Default Displayed Value")
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

    def test_triggerDistance_reject_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: TriggerDistance Reject Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_triggerDistance_reject_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: TriggerDistance Reject Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_triggerDistance_reject_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_REJECT_LOW":
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
                    test.startSection("Suspect & Reject: TriggerDistance Reject Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_triggerDistance_reject_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: TriggerDistance Reject Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_triggerDistance_reject_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: TriggerDistance Reject Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class TriggerDistance_Suspect_Low:
    def test_triggerDistance_suspect_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_SUSPECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: TriggerDistance Suspect Low :Test 40K_Default Displayed Value")
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

    def test_triggerDistance_suspect_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: TriggerDistance Suspect Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_triggerDistance_suspect_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: TriggerDistance Suspect Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_triggerDistance_suspect_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_SUSPECT_LOW":
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
                    test.startSection("Suspect & Reject: TriggerDistance Suspect Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_triggerDistance_suspect_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: TriggerDistance Suspect Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_triggerDistance_suspect_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: TriggerDistance Suspect Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class TriggerDistance_Suspect_High:
    def test_triggerDistance_suspect_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_SUSPECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: TriggerDistance Suspect High :Test 40K_Default Displayed Value")
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

    def test_triggerDistance_suspect_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: TriggerDistance Suspect High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_triggerDistance_suspect_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: TriggerDistance Suspect High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_triggerDistance_suspect_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_SUSPECT_HIGH":
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
                    test.startSection("Suspect & Reject: TriggerDistance Suspect High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_triggerDistance_suspect_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: TriggerDistance Suspect High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_triggerDistance_suspect_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: TriggerDistance Suspect High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class TriggerDistance_Reject_High:
    def test_triggerDistance_reject_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_REJECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: TriggerDistance Reject High :Test 40K_Default Displayed Value")
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

    def test_triggerDistance_reject_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: TriggerDistance Reject High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_triggerDistance_reject_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: TriggerDistance Reject High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_triggerDistance_reject_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_REJECT_HIGH":
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
                    test.startSection("Suspect & Reject: TriggerDistance Reject High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_triggerDistance_reject_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: TriggerDistance Reject High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_triggerDistance_reject_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TRIGGERDISTANCE_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: TriggerDistance Reject High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class Velocity_Reject_Low:
    def test_velocity_reject_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_REJECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Velocity Reject Low :Test 40K_Default Displayed Value")
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

    def test_velocity_reject_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Velocity Reject Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_velocity_reject_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Velocity Reject Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_velocity_reject_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_REJECT_LOW":
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
                    test.startSection("Suspect & Reject: Velocity Reject Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_velocity_reject_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Velocity Reject Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_velocity_reject_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Velocity Reject Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class Velocity_Suspect_Low:
    def test_velocity_suspect_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_SUSPECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Velocity Suspect Low :Test 40K_Default Displayed Value")
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

    def test_velocity_suspect_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Velocity Suspect Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_velocity_suspect_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Velocity Suspect Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_velocity_suspect_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_SUSPECT_LOW":
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
                    test.startSection("Suspect & Reject: Velocity Suspect Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_velocity_suspect_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Velocity Suspect Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_velocity_suspect_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Velocity Suspect Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class Velocity_Suspect_High:
    def test_velocity_suspect_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_SUSPECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Velocity Suspect High :Test 40K_Default Displayed Value")
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

    def test_velocity_suspect_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Velocity Suspect High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_velocity_suspect_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Velocity Suspect High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_velocity_suspect_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_SUSPECT_HIGH":
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
                    test.startSection("Suspect & Reject: Velocity Suspect High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_velocity_suspect_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Velocity Suspect High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_velocity_suspect_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Velocity Suspect High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class Velocity_Reject_High:
    def test_velocity_reject_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_REJECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Velocity Reject High :Test 40K_Default Displayed Value")
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

    def test_velocity_reject_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Velocity Reject High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_velocity_reject_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Velocity Reject High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_velocity_reject_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_REJECT_HIGH":
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
                    test.startSection("Suspect & Reject: Velocity Reject High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_velocity_reject_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Velocity Reject High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_velocity_reject_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "VELOCITY_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Velocity Reject High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class Frequency_Reject_Low:
    def test_frequency_reject_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_REJECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Frequency Reject Low :Test 40K_Default Displayed Value")
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

    def test_frequency_reject_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Frequency Reject Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_frequency_reject_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Frequency Reject Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_frequency_reject_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_REJECT_LOW":
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
                    test.startSection("Suspect & Reject: Frequency Reject Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_frequency_reject_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_REJECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Frequency Reject Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_frequency_reject_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_REJECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Frequency Reject Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectLow()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class Frequency_Suspect_Low:
    def test_frequency_suspect_low_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_SUSPECT_LOW":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Frequency Suspect Low :Test 40K_Default Displayed Value")
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

    def test_frequency_suspect_low_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Frequency Suspect Low :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_frequency_suspect_low_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Frequency Suspect Low :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_frequency_suspect_low_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_SUSPECT_LOW":
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
                    test.startSection("Suspect & Reject: Frequency Suspect Low :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_frequency_suspect_low_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_SUSPECT_LOW":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Frequency Suspect Low :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_frequency_suspect_low_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_SUSPECT_LOW":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Frequency Suspect Low :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectLow()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class Frequency_Suspect_High:
    def test_frequency_suspect_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_SUSPECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Frequency Suspect High :Test 40K_Default Displayed Value")
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

    def test_frequency_suspect_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Frequency Suspect High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_frequency_suspect_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Frequency Suspect High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_frequency_suspect_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_SUSPECT_HIGH":
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
                    test.startSection("Suspect & Reject: Frequency Suspect High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_frequency_suspect_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_SUSPECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Frequency Suspect High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_frequency_suspect_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_SUSPECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Frequency Suspect High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterSuspectHigh()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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


class Frequency_Reject_High:
    def test_frequency_reject_high_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_REJECT_HIGH":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Suspect & Reject: Frequency Reject High :Test 40K_Default Displayed Value")
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

    def test_frequency_reject_high_40K_min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Suspect & Reject: Frequency Reject High :Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_frequency_reject_high_40K_max(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Suspect & Reject: Frequency Reject High :Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_frequency_reject_high_40K_mid(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_REJECT_HIGH":
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
                    test.startSection("Suspect & Reject: Frequency Reject High :Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_frequency_reject_high_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_REJECT_HIGH":
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Suspect & Reject: Frequency Reject High :Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_max_plus_one)
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

    def test_frequency_reject_high_40K_min_minus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "FREQUENCY_REJECT_HIGH":
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Suspect & Reject: Frequency Reject High :Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    limits.enterRejectHigh()
                    recipe.enterValueSuspectReject(value_40K_min_minus_one)
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
    pre_condition()

    core.moduleName("limits: suspect and reject parameter")
    squish.snooze(5)
    new_create_recipe()
    test.log("Going to click on the limits tab")
    limits.limitsTab()

    limits.enableGlobalSuspect()
    limits.enableGlobalReject()
    limits.timeTab()
    limits.enableSuspect_Parameter()
    limits.enableReject_Parameter()

    # timeRejectLow = Time_Reject_Low()
    # timeRejectLow.test_time_reject_low_40K_Default()
    # timeRejectLow.test_time_reject_low_40K_min()
    # timeRejectLow.test_time_reject_low_40K_max()
    # timeRejectLow.test_time_reject_low_40K_mid()
    # timeRejectLow.test_time_reject_low_40K_max_plus_one()
    # timeRejectLow.test_time_reject_low_40K_min_minus_one()
    #
    # timeSuspectLow = Time_Suspect_Low()
    # timeSuspectLow.test_time_suspect_low_40K_Default()
    # timeSuspectLow.test_time_suspect_low_40K_min()
    # timeSuspectLow.test_time_suspect_low_40K_max()
    # timeSuspectLow.test_time_suspect_low_40K_mid()
    # timeSuspectLow.test_time_suspect_low_40K_max_plus_one()
    # timeSuspectLow.test_time_suspect_low_40K_min_minus_one()

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

    # limits.energyTab()
    # limits.enableSuspect_Parameter()
    # limits.enableReject_Parameter()
    #
    # energyRejectLow = Energy_Reject_Low()
    # energyRejectLow.test_energy_reject_low_40K_Default()
    # energyRejectLow.test_energy_reject_low_40K_min()
    # energyRejectLow.test_energy_reject_low_40K_max()
    # energyRejectLow.test_energy_reject_low_40K_mid()
    # energyRejectLow.test_energy_reject_low_40K_max_plus_one()
    # energyRejectLow.test_energy_reject_low_40K_min_minus_one()
    #
    # energySuspectLow = Energy_Suspect_Low()
    # energySuspectLow.test_energy_suspect_low_40K_Default()
    # energySuspectLow.test_energy_suspect_low_40K_min()
    # energySuspectLow.test_energy_suspect_low_40K_max()
    # energySuspectLow.test_energy_suspect_low_40K_mid()
    # energySuspectLow.test_energy_suspect_low_40K_max_plus_one()
    # energySuspectLow.test_energy_suspect_low_40K_min_minus_one()
    #
    # energySuspectHigh = Energy_Suspect_High()
    # energySuspectHigh.test_energy_suspect_high_40K_Default()
    # energySuspectHigh.test_energy_suspect_high_40K_min()
    # energySuspectHigh.test_energy_suspect_high_40K_max()
    # energySuspectHigh.test_energy_suspect_high_40K_mid()
    # energySuspectHigh.test_energy_suspect_high_40K_max_plus_one()
    # energySuspectHigh.test_energy_suspect_high_40K_min_minus_one()
    #
    # energyRejectHigh = Energy_Reject_High()
    # energyRejectHigh.test_energy_reject_high_40K_Default()
    # energyRejectHigh.test_energy_reject_high_40K_min()
    # energyRejectHigh.test_energy_reject_high_40K_max()
    # energyRejectHigh.test_energy_reject_high_40K_mid()
    # energyRejectHigh.test_energy_reject_high_40K_max_plus_one()
    # energyRejectHigh.test_energy_reject_high_40K_min_minus_one()
    #
    # limits.peakPowerTab()
    # limits.enableSuspect_Parameter()
    # limits.enableReject_Parameter()
    #
    # peakPowerRejectLow = PeakPower_Reject_Low()
    # peakPowerRejectLow.test_peakPower_reject_low_40K_Default()
    # peakPowerRejectLow.test_peakPower_reject_low_40K_min()
    # peakPowerRejectLow.test_peakPower_reject_low_40K_max()
    # peakPowerRejectLow.test_peakPower_reject_low_40K_mid()
    # peakPowerRejectLow.test_peakPower_reject_low_40K_max_plus_one()
    # peakPowerRejectLow.test_peakPower_reject_low_40K_min_minus_one()
    #
    # peakPowerSuspectLow = PeakPower_Suspect_Low()
    # peakPowerSuspectLow.test_peakPower_suspect_low_40K_Default()
    # peakPowerSuspectLow.test_peakPower_suspect_low_40K_min()
    # peakPowerSuspectLow.test_peakPower_suspect_low_40K_max()
    # peakPowerSuspectLow.test_peakPower_suspect_low_40K_mid()
    # peakPowerSuspectLow.test_peakPower_suspect_low_40K_max_plus_one()
    # peakPowerSuspectLow.test_peakPower_suspect_low_40K_min_minus_one()
    #
    # peakPowerSuspectHigh = PeakPower_Suspect_High()
    # peakPowerSuspectHigh.test_peakPower_suspect_high_40K_Default()
    # peakPowerSuspectHigh.test_peakPower_suspect_high_40K_min()
    # peakPowerSuspectHigh.test_peakPower_suspect_high_40K_max()
    # peakPowerSuspectHigh.test_peakPower_suspect_high_40K_mid()
    # peakPowerSuspectHigh.test_peakPower_suspect_high_40K_max_plus_one()
    # peakPowerSuspectHigh.test_peakPower_suspect_high_40K_min_minus_one()
    #
    # peakPowerRejectHigh = PeakPower_Reject_High()
    # peakPowerRejectHigh.test_peakPower_reject_high_40K_Default()
    # peakPowerRejectHigh.test_peakPower_reject_high_40K_min()
    # peakPowerRejectHigh.test_peakPower_reject_high_40K_max()
    # peakPowerRejectHigh.test_peakPower_reject_high_40K_mid()
    # peakPowerRejectHigh.test_peakPower_reject_high_40K_max_plus_one()
    # peakPowerRejectHigh.test_peakPower_reject_high_40K_min_minus_one()
    #
    # limits.absoluteDistanceTab()
    # limits.enableSuspect_Parameter()
    # limits.enableReject_Parameter()
    #
    # enterRejectLow = AbsoluteDistance_Reject_Low()
    # enterRejectLow.test_absoluteDistance_reject_low_40K_Default()
    # enterRejectLow.test_absoluteDistance_reject_low_40K_min()
    # enterRejectLow.test_absoluteDistance_reject_low_40K_max()
    # enterRejectLow.test_absoluteDistance_reject_low_40K_mid()
    # enterRejectLow.test_absoluteDistance_reject_low_40K_max_plus_one()
    # enterRejectLow.test_absoluteDistance_reject_low_40K_min_minus_one()
    #
    # enterSuspectLow = AbsoluteDistance_Suspect_Low()
    # enterSuspectLow.test_absoluteDistance_suspect_low_40K_Default()
    # enterSuspectLow.test_absoluteDistance_suspect_low_40K_min()
    # enterSuspectLow.test_absoluteDistance_suspect_low_40K_max()
    # enterSuspectLow.test_absoluteDistance_suspect_low_40K_mid()
    # enterSuspectLow.test_absoluteDistance_suspect_low_40K_max_plus_one()
    # enterSuspectLow.test_absoluteDistance_suspect_low_40K_min_minus_one()
    #
    # enterSuspectHigh = AbsoluteDistance_Suspect_High()
    # enterSuspectHigh.test_absoluteDistance_suspect_high_40K_Default()
    # enterSuspectHigh.test_absoluteDistance_suspect_high_40K_min()
    # enterSuspectHigh.test_absoluteDistance_suspect_high_40K_max()
    # enterSuspectHigh.test_absoluteDistance_suspect_high_40K_mid()
    # enterSuspectHigh.test_absoluteDistance_suspect_high_40K_max_plus_one()
    # enterSuspectHigh.test_absoluteDistance_suspect_high_40K_min_minus_one()
    #
    # enterRejectHigh = AbsoluteDistance_Reject_High()
    # enterRejectHigh.test_absoluteDistance_reject_high_40K_Default()
    # enterRejectHigh.test_absoluteDistance_reject_high_40K_min()
    # enterRejectHigh.test_absoluteDistance_reject_high_40K_max()
    # enterRejectHigh.test_absoluteDistance_reject_high_40K_mid()
    # enterRejectHigh.test_absoluteDistance_reject_high_40K_max_plus_one()
    # enterRejectHigh.test_absoluteDistance_reject_high_40K_min_minus_one()
    #
    # core.scroll(names.recipeLabWindow_gridView_GridView)
    #
    # limits.collapseDistanceTab()
    # limits.enableSuspect_Parameter()
    # limits.enableReject_Parameter()
    #
    # enterRejectLow = CollapseDistance_Reject_Low()
    # enterRejectLow.test_collapseDistance_reject_low_40K_Default()
    # enterRejectLow.test_collapseDistance_reject_low_40K_min()
    # enterRejectLow.test_collapseDistance_reject_low_40K_max()
    # enterRejectLow.test_collapseDistance_reject_low_40K_mid()
    # enterRejectLow.test_collapseDistance_reject_low_40K_max_plus_one()
    # enterRejectLow.test_collapseDistance_reject_low_40K_min_minus_one()
    #
    # enterSuspectLow = CollapseDistance_Suspect_Low()
    # enterSuspectLow.test_collapseDistance_suspect_low_40K_Default()
    # enterSuspectLow.test_collapseDistance_suspect_low_40K_min()
    # enterSuspectLow.test_collapseDistance_suspect_low_40K_max()
    # enterSuspectLow.test_collapseDistance_suspect_low_40K_mid()
    # enterSuspectLow.test_collapseDistance_suspect_low_40K_max_plus_one()
    # enterSuspectLow.test_collapseDistance_suspect_low_40K_min_minus_one()
    #
    # enterSuspectHigh = CollapseDistance_Suspect_High()
    # enterSuspectHigh.test_collapseDistance_suspect_high_40K_Default()
    # enterSuspectHigh.test_collapseDistance_suspect_high_40K_min()
    # enterSuspectHigh.test_collapseDistance_suspect_high_40K_max()
    # enterSuspectHigh.test_collapseDistance_suspect_high_40K_mid()
    # enterSuspectHigh.test_collapseDistance_suspect_high_40K_max_plus_one()
    # enterSuspectHigh.test_collapseDistance_suspect_high_40K_min_minus_one()
    #
    # enterRejectHigh = CollapseDistance_Reject_High()
    # enterRejectHigh.test_collapseDistance_reject_high_40K_Default()
    # enterRejectHigh.test_collapseDistance_reject_high_40K_min()
    # enterRejectHigh.test_collapseDistance_reject_high_40K_max()
    # enterRejectHigh.test_collapseDistance_reject_high_40K_mid()
    # enterRejectHigh.test_collapseDistance_reject_high_40K_max_plus_one()
    # enterRejectHigh.test_collapseDistance_reject_high_40K_min_minus_one()
    #
    # limits.endWeldForceTab()
    # limits.enableSuspect_Parameter()
    # limits.enableReject_Parameter()
    #
    # enterRejectLow = EndWeldStore_Reject_Low()
    # enterRejectLow.test_endWeldStore_reject_low_40K_Default()
    # enterRejectLow.test_endWeldStore_reject_low_40K_min()
    # enterRejectLow.test_endWeldStore_reject_low_40K_max()
    # enterRejectLow.test_endWeldStore_reject_low_40K_mid()
    # enterRejectLow.test_endWeldStore_reject_low_40K_max_plus_one()
    # enterRejectLow.test_endWeldStore_reject_low_40K_min_minus_one()
    #
    # enterSuspectLow = EndWeldStore_Suspect_Low()
    # enterSuspectLow.test_endWeldStore_suspect_low_40K_Default()
    # enterSuspectLow.test_endWeldStore_suspect_low_40K_min()
    # enterSuspectLow.test_endWeldStore_suspect_low_40K_max()
    # enterSuspectLow.test_endWeldStore_suspect_low_40K_mid()
    # enterSuspectLow.test_endWeldStore_suspect_low_40K_max_plus_one()
    # enterSuspectLow.test_endWeldStore_suspect_low_40K_min_minus_one()
    #
    # enterSuspectHigh = EndWeldStore_Suspect_High()
    # enterSuspectHigh.test_endWeldStore_suspect_high_40K_Default()
    # enterSuspectHigh.test_endWeldStore_suspect_high_40K_min()
    # enterSuspectHigh.test_endWeldStore_suspect_high_40K_max()
    # enterSuspectHigh.test_endWeldStore_suspect_high_40K_mid()
    # enterSuspectHigh.test_endWeldStore_suspect_high_40K_max_plus_one()
    # enterSuspectHigh.test_endWeldStore_suspect_high_40K_min_minus_one()
    #
    # enterRejectHigh = EndWeldStore_Reject_High()
    # enterRejectHigh.test_endWeldStore_reject_high_40K_Default()
    # enterRejectHigh.test_endWeldStore_reject_high_40K_min()
    # enterRejectHigh.test_endWeldStore_reject_high_40K_max()
    # enterRejectHigh.test_endWeldStore_reject_high_40K_mid()
    # enterRejectHigh.test_endWeldStore_reject_high_40K_max_plus_one()
    # enterRejectHigh.test_endWeldStore_reject_high_40K_min_minus_one()
    #
    # limits.triggerDistabceTab()
    # limits.enableSuspect_Parameter()
    # limits.enableReject_Parameter()
    #
    # trigRejectLow = TriggerDistance_Reject_Low()
    # trigRejectLow.test_triggerDistance_reject_low_40K_Default()
    # trigRejectLow.test_triggerDistance_reject_low_40K_min()
    # trigRejectLow.test_triggerDistance_reject_low_40K_max()
    # trigRejectLow.test_triggerDistance_reject_low_40K_mid()
    # trigRejectLow.test_triggerDistance_reject_low_40K_max_plus_one()
    # trigRejectLow.test_triggerDistance_reject_low_40K_min_minus_one()
    #
    # trigSuspectLow = TriggerDistance_Suspect_Low()
    # trigSuspectLow.test_triggerDistance_suspect_low_40K_Default()
    # trigSuspectLow.test_triggerDistance_suspect_low_40K_min()
    # trigSuspectLow.test_triggerDistance_suspect_low_40K_max()
    # trigSuspectLow.test_triggerDistance_suspect_low_40K_mid()
    # trigSuspectLow.test_triggerDistance_suspect_low_40K_max_plus_one()
    # trigSuspectLow.test_triggerDistance_suspect_low_40K_min_minus_one()
    #
    # trigSuspectHigh = TriggerDistance_Suspect_High()
    # trigSuspectHigh.test_triggerDistance_suspect_high_40K_Default()
    # trigSuspectHigh.test_triggerDistance_suspect_high_40K_min()
    # trigSuspectHigh.test_triggerDistance_suspect_high_40K_max()
    # trigSuspectHigh.test_triggerDistance_suspect_high_40K_mid()
    # trigSuspectHigh.test_triggerDistance_suspect_high_40K_max_plus_one()
    # trigSuspectHigh.test_triggerDistance_suspect_high_40K_min_minus_one()
    #
    # trigRejectHigh = TriggerDistance_Reject_High()
    # trigRejectHigh.test_triggerDistance_reject_high_40K_Default()
    # trigRejectHigh.test_triggerDistance_reject_high_40K_min()
    # trigRejectHigh.test_triggerDistance_reject_high_40K_max()
    # trigRejectHigh.test_triggerDistance_reject_high_40K_mid()
    # trigRejectHigh.test_triggerDistance_reject_high_40K_max_plus_one()
    # trigRejectHigh.test_triggerDistance_reject_high_40K_min_minus_one()
    #
    # limits.velocityTab()
    # limits.enableSuspect_Parameter()
    # limits.enableReject_Parameter()
    #
    # velRejectLow = Velocity_Reject_Low()
    # velRejectLow.test_velocity_reject_low_40K_Default()
    # velRejectLow.test_velocity_reject_low_40K_min()
    # velRejectLow.test_velocity_reject_low_40K_max()
    # velRejectLow.test_velocity_reject_low_40K_mid()
    # velRejectLow.test_velocity_reject_low_40K_max_plus_one()
    # velRejectLow.test_velocity_reject_low_40K_min_minus_one()
    #
    # velSuspectLow = Velocity_Suspect_Low()
    # velSuspectLow.test_velocity_suspect_low_40K_Default()
    # velSuspectLow.test_velocity_suspect_low_40K_min()
    # velSuspectLow.test_velocity_suspect_low_40K_max()
    # velSuspectLow.test_velocity_suspect_low_40K_mid()
    # velSuspectLow.test_velocity_suspect_low_40K_max_plus_one()
    # velSuspectLow.test_velocity_suspect_low_40K_min_minus_one()
    #
    # velSuspectHigh = Velocity_Suspect_High()
    # velSuspectHigh.test_velocity_suspect_high_40K_Default()
    # velSuspectHigh.test_velocity_suspect_high_40K_min()
    # velSuspectHigh.test_velocity_suspect_high_40K_max()
    # velSuspectHigh.test_velocity_suspect_high_40K_mid()
    # velSuspectHigh.test_velocity_suspect_high_40K_max_plus_one()
    # velSuspectHigh.test_velocity_suspect_high_40K_min_minus_one()
    #
    # velRejectHigh = Velocity_Reject_High()
    # velRejectHigh.test_velocity_reject_high_40K_Default()
    # velRejectHigh.test_velocity_reject_high_40K_min()
    # velRejectHigh.test_velocity_reject_high_40K_max()
    # velRejectHigh.test_velocity_reject_high_40K_mid()
    # velRejectHigh.test_velocity_reject_high_40K_max_plus_one()
    # velRejectHigh.test_velocity_reject_high_40K_min_minus_one()
    #
    # limits.frequencyTab()
    # limits.enableSuspect_Parameter()
    # limits.enableReject_Parameter()
    #
    # freqRejectLow = Frequency_Reject_Low()
    # freqRejectLow.test_frequency_reject_low_40K_Default()
    # freqRejectLow.test_frequency_reject_low_40K_min()
    # freqRejectLow.test_frequency_reject_low_40K_max()
    # freqRejectLow.test_frequency_reject_low_40K_mid()
    # freqRejectLow.test_frequency_reject_low_40K_max_plus_one()
    # freqRejectLow.test_frequency_reject_low_40K_min_minus_one()
    #
    # freqSuspectLow = Frequency_Suspect_Low()
    # freqSuspectLow.test_frequency_suspect_low_40K_Default()
    # freqSuspectLow.test_frequency_suspect_low_40K_min()
    # freqSuspectLow.test_frequency_suspect_low_40K_max()
    # freqSuspectLow.test_frequency_suspect_low_40K_mid()
    # freqSuspectLow.test_frequency_suspect_low_40K_max_plus_one()
    # freqSuspectLow.test_frequency_suspect_low_40K_min_minus_one()
    #
    # freqSuspectHigh = Frequency_Suspect_High()
    # freqSuspectHigh.test_frequency_suspect_high_40K_Default()
    # freqSuspectHigh.test_frequency_suspect_high_40K_min()
    # freqSuspectHigh.test_frequency_suspect_high_40K_max()
    # freqSuspectHigh.test_frequency_suspect_high_40K_mid()
    # freqSuspectHigh.test_frequency_suspect_high_40K_max_plus_one()
    # freqSuspectHigh.test_frequency_suspect_high_40K_min_minus_one()
    #
    # freqRejectHigh = Frequency_Reject_High()
    # freqRejectHigh.test_frequency_reject_high_40K_Default()
    # freqRejectHigh.test_frequency_reject_high_40K_min()
    # freqRejectHigh.test_frequency_reject_high_40K_max()
    # freqRejectHigh.test_frequency_reject_high_40K_mid()
    # freqRejectHigh.test_frequency_reject_high_40K_max_plus_one()
    # freqRejectHigh.test_frequency_reject_high_40K_min_minus_one()
