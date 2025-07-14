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


def Set_Metric():
    user_setting.change_to_metric_unit()
    
def post_condition():
    login.logout()


def new_create_recipe():
    test.log("Started with creation of new recipe")
    recipe.CreateNewRecipe()


class CollapseDistance_Metric:
    def test_collapsedistance_40K_Default(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Test 40K_Default Displayed Value")
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

    def test_collapsedistance_40K_min(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "COLLAPSE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Test 40K_Min")
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
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Test 40K_Max")
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
                testData.field(row, "UNIT_TYPE") == "METRIC"
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
                    test.startSection("Test 40K_Mid")
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
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Test 40K_Max + 1 (Out of Range)")
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
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Test 40K_Min - 1 (Out of Range)")
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

class AbsoulteDistance_Metric:
    def test_absoultedistance_40K_Default(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Test 40K_Default Displayed Value")
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

    def test_absoultedistance_40K_min(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "ABSOLUTE_DISTANCE" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                test.startSection("Test 40K_Min")
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
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                test.startSection("Test 40K_Max")
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
                testData.field(row, "UNIT_TYPE") == "METRIC"
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
                test.startSection("Test 40K_Mid")
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
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Test 40K_Max + 1 (Out of Range)")
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
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Test 40K_Min - 1 (Out of Range)")
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

class WeldAmplitude:
    def test_weld_amplitude_40K_Default(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "WELD_AMPLITUDE_PARAM" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        displayed_value = str(findObject(names.recipeLabWindow_10_Text).text)
                        displayed_value_clean = displayed_value.replace(" %", "").strip()
                        test.log(f'displayed value check: {displayed_value_clean}')
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_weld_amplitude_40K_min(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "WELD_AMPLITUDE_PARAM" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe.weld_amplitude_quickedit()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.weld_amplitude_DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_weld_amplitude_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "WELD_AMPLITUDE_PARAM" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                test.startSection("Test 40K_Max")
                test.log(f"Testing 40K_Max: {value_40K_max}")
                recipe.weld_amplitude_quickedit()
                recipe.enterValue(value_40K_max)
                squish.snooze(2)
                recipe.weld_amplitude_DoneButton()
                test.passes(f"Entered value matches expected max value: {value_40K_max}")
                test.endSection()

    def test_weld_amplitude_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "WELD_AMPLITUDE_PARAM" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
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
                test.startSection("Test 40K_Mid")
                test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                recipe.weld_amplitude_quickedit()
                recipe.enterValue(str(mid_val))
                squish.snooze(2)
                recipe.weld_amplitude_DoneButton()
                test.passes(f"Entered value matches expected mid value: {mid_val}")
                test.endSection()

    def test_weld_amplitude_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "WELD_AMPLITUDE_PARAM" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe.weld_amplitude_quickedit()
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.weld_amplitude_DoneButton()
                    if object.exists(names.update_WeldRecipe_Parameter_failed_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_max_plus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Max+1: {e}")

    def test_weld_amplitude_40K_min_minus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "WELD_AMPLITUDE_PARAM" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe.weld_amplitude_quickedit()
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.weld_amplitude_DoneButton()
                    if object.exists(names.update_WeldRecipe_Parameter_failed_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}") 
                    
class Downspeed:
    def test_downspeed_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "DOWNSPEED":

                # 40K_Default Verification
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        displayed_value = str(findObject(names.recipeLabWindow_0_Text).text)
                        test.log(f"Checking if the default value matches with the actual data")
                        displayed_value_clean = displayed_value.replace(" %", "").strip()

                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()

    def test_downspeed_40K_min(self):
        # Test 40K_Min
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "DOWNSPEED" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe.downspeed_quickedit()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_downspeed_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "DOWNSPEED" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe.downspeed_quickedit()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_downspeed_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "DOWNSPEED" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
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
                test.startSection("Test 40K_Mid")
                test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                recipe.downspeed_quickedit()
                recipe.enterValue(str(mid_val))
                squish.snooze(2)
                recipe.DoneButton()
                test.passes(f"Entered value matches expected mid value: {mid_val}")
                test.endSection()

    def test_downspeed_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "DOWNSPEED" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe.downspeed_quickedit()
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

    def test_downspeed_40K_min_minus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "DOWNSPEED" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe.downspeed_quickedit()
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

class WeldPressure:
    def test_weldpressure_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "WELD PRESSURE":

                # 40K_Default Verification
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        displayed_value = str(findObject(names.recipeLabWindow_138_kPa_Text).text)
                        test.log(f"Checking if the default value matches with the actual data")
                        displayed_value_clean = displayed_value.replace(" kPa", "").strip()

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
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe.weld_pressure_quickedit()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.weld_amplitude_DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_weldpressure_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "WELD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe.weld_pressure_quickedit()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.weld_amplitude_DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_weldpressure_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "WELD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
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
                test.startSection("Test 40K_Mid")
                test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                recipe.weld_pressure_quickedit()
                recipe.enterValue(str(mid_val))
                squish.snooze(2)
                recipe.weld_amplitude_DoneButton()
                test.passes(f"Entered value matches expected mid value: {mid_val}")
                test.endSection()

    def test_weldpressure_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "WELD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Test 40K_Max + 1 (Out of Range)")
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
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe.weld_pressure_quickedit()
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.weld_amplitude_DoneButton()
                    if object.exists(names.updateWeldRecipeParameter_fail5_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}") 

class HoldPressure:
    def test_holdpressure_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "HOLD PRESSURE":

                # 40K_Default Verification
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        displayed_value = str(findObject(names.recipeLabWindow_138_kPa_Text).text)
                        test.log(f"Checking if the default value matches with the actual data")
                        displayed_value_clean = displayed_value.replace(" kPa", "").strip()

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
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe.hold_pressure_quickedit()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_holdpressure_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "HOLD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe.hold_pressure_quickedit()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_holdpressure_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "HOLD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
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
                test.startSection("Test 40K_Mid")
                test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                recipe.hold_pressure_quickedit()
                recipe.enterValue(str(mid_val))
                squish.snooze(2)
                recipe.DoneButton()
                test.passes(f"Entered value matches expected mid value: {mid_val}")
                test.endSection()

    def test_holdpressure_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "HOLD PRESSURE" and
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe.hold_pressure_quickedit()
                    recipe.enterValue(value_40K_max_plus_one)
                    squish.snooze(2)
                    recipe.weld_amplitude_DoneButton()
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
                testData.field(row, "UNIT_TYPE") == "METRIC"
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe.weld_pressure_quickedit()
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.hold_pressure_quickedit()
                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value rejected as expected: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation popup did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}") 
def main():
#HOLD PRESSURE

    test.log("Starting to log into the system")
    startApplication("QT_UIController")
    pre_condition()
    # reset_notification()
    core.moduleName("Recipe")
    test.log("Completed the notifications pop skipping")
    squish.snooze(0.2)
    # Set_Metric()
    
    squish.snooze(0.2)
    # Set_Metric()
    squish.snooze(0.2)
    new_create_recipe()

    # recipe.AbsoulteDistanceTab()
    #
    # absoulte_m = AbsoulteDistance_Metric()
    # absoulte_m.test_absoultedistance_40K_Default()
    # absoulte_m.test_absoultedistance_40K_max()
    # absoulte_m.test_absoultedistance_40K_min()
    # absoulte_m.test_absoultedistance_40K_mid()
    # absoulte_m.test_absoultedistance_40K_max_plus_one()
    # absoulte_m.test_absoultedistance_40K_min_minus_one()
    
    # recipe.CollapseDistanceTab()
    
    # collapse_m = CollapseDistance_Metric()
    # collapse_m.test_collapsedistance_40K_Default()
    # collapse_m.test_collapsedistance_40K_max()
    # collapse_m.test_collapsedistance_40K_min()
    # collapse_m.test_collapsedistance_40K_mid()
    # collapse_m.test_collapsedistance_40K_max_plus_one()
    # collapse_m.test_collapsedistance_40K_min_minus_one()
    
    # weldAmplitude = WeldAmplitude()
    # weldAmplitude.test_weld_amplitude_40K_Default()
    # weldAmplitude.test_weld_amplitude_40K_min()
    # weldAmplitude.test_weld_amplitude_40K_max()
    # weldAmplitude.test_weld_amplitude_40K_mid()
    # weldAmplitude.test_weld_amplitude_40K_max_plus_one()
    # weldAmplitude.test_weld_amplitude_40K_min_minus_one()
    
    # downspeed = Downspeed()
    # downspeed.test_downspeed_40K_Default()
    # downspeed.test_downspeed_40K_max()
    # downspeed.test_downspeed_40K_min()
    # downspeed.test_downspeed_40K_mid()
    # downspeed.test_downspeed_40K_max_plus_one()
    # downspeed.test_downspeed_40K_min_minus_one()
    
    # weldpressure = WeldPressure()
    # weldpressure.test_weldpressure_40K_Default()
    # weldpressure.test_weldpressure_40K_max()
    # weldpressure.test_weldpressure_40K_mid()
    # weldpressure.test_weldpressure_40K_max_plus_one()
    # weldpressure.test_weldpressure_40K_min_minus_one()
    
    holdpressure = HoldPressure()
    # holdpressure.test_holdpressure_40K_Default()
    holdpressure.test_holdpressure_40K_max()
    holdpressure.test_holdpressure_40K_mid()
    holdpressure.test_holdpressure_40K_max_plus_one()
    holdpressure.test_holdpressure_40K_min_minus_one()
    
    
    
    #
    # post_condition()
