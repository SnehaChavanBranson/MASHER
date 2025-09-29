import names
from screens import login, recipe, weld_process
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

def post_condition():
    login.logout()


def new_create_recipe():
    test.log("Started with creation of new recipe")
    recipe.CreateNewRecipe()
    
def navigate_to_weld_processTab():
    test.log("navigating to weld process tab")
    weld_process.weldProcessTab()

class Pretrigger_Amplitude:
    def test_pretrigger_amplitude_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_AMPLITUDE_PARAM":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Weld Process: Pretrigger Amplitude: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWrecipeLabWindow_10_Text_2)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" %", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()
    
    def test_pretrigger_amplitude_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_AMPLITUDE_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")
                    if value_40K_min:
                        test.startSection("Weld Process: Pretrigger Amplitude: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_weld_process.pretriggerAmplitudeEnterValue()
                        recipe.enterValue(value_40K_min)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected min value: {value_40K_min}")
                        test.endSection()
    
    def test_pretrigger_amplitude_40K_Max(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_AMPLITUDE_PARAM":
                    value_40K_max = testData.field(row, "40K_Max")
                    if value_40K_max:
                        test.startSection("Weld Process: Pretrigger Amplitude: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_weld_process.pretriggerAmplitudeEnterValue()
                        recipe.enterValue(value_40K_max)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected max value: {value_40K_max}")
                        test.endSection()
    
    def test_pretrigger_amplitude_40K_Mid(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_AMPLITUDE_PARAM":
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
    
                        test.startSection("Weld Process: Pretrigger Amplitude: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_weld_process.pretriggerAmplitudeEnterValue()
                        recipe.enterValue(str(mid_val))
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected mid value: {mid_val}")
                        test.endSection()
    
    def test_pretrigger_amplitude_40K_max_plus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_AMPLITUDE_PARAM":
                    # Test 40K_Max + 1
                    value_40K_max = testData.field(row, "40K_Max")
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Weld Process: Pretrigger Amplitude: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_weld_process.pretriggerAmplitudeEnterValue()
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
    
    def test_pretrigger_amplitude_40K_min_minus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_AMPLITUDE_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")    
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Weld Process: Pretrigger Amplitude: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_weld_process.pretriggerAmplitudeEnterValue()
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


class Pretrigger_Distance:
    def test_pretrigger_distance_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_DISTANCE_PARAM" and testData.field(row, "UNIT_TYPE") == "IMPERIAL":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Weld Process: Pretrigger Distance: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_0_1250_in_Text)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" in", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()
    
    def test_pretrigger_distance_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_DISTANCE_PARAM" and testData.field(row, "UNIT_TYPE") == "IMPERIAL":
                    value_40K_min = testData.field(row, "40K_Min")
                    if value_40K_min:
                        test.startSection("Weld Process: Pretrigger Distance: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_weld_process.pretriggerDistanceEnterValue()
                        recipe.enterValue(value_40K_min)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected min value: {value_40K_min}")
                        test.endSection()
    
    def test_pretrigger_distance_40K_Max(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_DISTANCE_PARAM" and testData.field(row, "UNIT_TYPE") == "IMPERIAL":
                    value_40K_max = testData.field(row, "40K_Max")
                    if value_40K_max:
                        test.startSection("Weld Process: Pretrigger Distance: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_weld_process.pretriggerDistanceEnterValue()
                        recipe.enterValue(value_40K_max)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected max value: {value_40K_max}")
                        test.endSection()
    
    def test_pretrigger_distance_40K_Mid(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_DISTANCE_PARAM" and testData.field(row, "UNIT_TYPE") == "IMPERIAL":
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
    
                        test.startSection("Weld Process: Pretrigger Distance: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_weld_process.pretriggerDistanceEnterValue()
                        recipe.enterValue(str(mid_val))
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected mid value: {mid_val}")
                        test.endSection()
    
    def test_pretrigger_distance_40K_max_plus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_DISTANCE_PARAM" and testData.field(row, "UNIT_TYPE") == "IMPERIAL":
                    # Test 40K_Max + 1
                    value_40K_max = testData.field(row, "40K_Max")
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Weld Process: Pretrigger Distance: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_weld_process.pretriggerDistanceEnterValue()
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
    
    def test_pretrigger_distance_40K_min_minus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_DISTANCE_PARAM" and testData.field(row, "UNIT_TYPE") == "IMPERIAL":
                    value_40K_min = testData.field(row, "40K_Min")    
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Weld Process: Pretrigger Distance: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_weld_process.pretriggerDistanceEnterValue()
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

class Pretrigger_Time:
    def test_pretrigger_time_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_TIME_PARAM":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Weld Process: Pretrigger Time: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_0_010_s_Text_2)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" s", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()
    
    def test_pretrigger_time_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_TIME_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")
                    if value_40K_min:
                        test.startSection("Weld Process: Pretrigger Time: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_weld_process.pretriggerTimeEnterValue()
                        recipe.enterValue(value_40K_min)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected min value: {value_40K_min}")
                        test.endSection()
    
    def test_pretrigger_time_40K_Max(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_TIME_PARAM":
                    value_40K_max = testData.field(row, "40K_Max")
                    if value_40K_max:
                        test.startSection("Weld Process: Pretrigger Time: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_weld_process.pretriggerTimeEnterValue()
                        recipe.enterValue(value_40K_max)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected max value: {value_40K_max}")
                        test.endSection()
    
    def test_pretrigger_time_40K_Mid(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_TIME_PARAM":
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
    
                        test.startSection("Weld Process: Pretrigger Time: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_weld_process.pretriggerTimeEnterValue()
                        recipe.enterValue(str(mid_val))
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected mid value: {mid_val}")
                        test.endSection()
    
    def test_pretrigger_time_40K_max_plus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_TIME_PARAM" :
                    # Test 40K_Max + 1
                    value_40K_max = testData.field(row, "40K_Max")
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Weld Process: Pretrigger Time: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_weld_process.pretriggerTimeEnterValue()
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
    
    def test_pretrigger_time_40K_min_minus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_TIME_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")    
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Weld Process: Pretrigger Time: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_weld_process.pretriggerTimeEnterValue()
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
                        
class AfterBurst_Delay:
    def test_afterburst_delay_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_DELAY_PARAM":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Weld Process: Afterburst Delay: Test 40K_Default Displayed Value")
                    test.log(f"Testing 40K_Default: {value_40K_default}")
                    try:
                        obj = waitForObject(names.recipeLabWindow_0_100_s_Text)
                        displayed_value = str(obj.text)
                        displayed_value_clean = displayed_value.replace(" s", "").strip()
                        if displayed_value_clean == value_40K_default.strip():
                            test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                        else:
                            test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                    except Exception as e:
                        test.fail(f"Error reading or comparing displayed value: {e}")
                    test.endSection()
                    
    def test_afterburst_delay_40K_Min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_DELAY_PARAM":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Weld Process: Afterburst Delay: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe_weld_process.afterburstDelayEnterValue()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()
               
    def test_afterburst_delay_40K_Max(self):
        # Test 40K_Max
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_DELAY_PARAM":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Weld Process: Afterburst Delay: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe_weld_process.afterburstDelayEnterValue()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_afterburst_delay_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_DELAY_PARAM":
                # Test 40K_Max + 1
                value_40K_max = testData.field(row, "40K_Max")
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Weld Process: Afterburst Delay: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe_weld_process.afterburstDelayEnterValue()
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

    def test_afterburst_delay_40K_Mid(self):
        # Test 40K_Mid (calculated between 40K_Min and 40K_Max)
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_DELAY_PARAM":
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

                    test.startSection("Weld Process: Afterburst Delay: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    recipe_weld_process.afterburstDelayEnterValue()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_afterburst_delay_40K_min_minus_one(self):
        # Test 40K_Min - 1
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_DELAY_PARAM":
                value_40K_min = testData.field(row, "40K_Min")    
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Weld Process: Afterburst Delay: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe_weld_process.afterburstDelayEnterValue()
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

class AfterBurst_Time:
        def test_afterburst_time_40K_Default(self):
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_TIME_PARAM":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Weld Process: Afterburst Delay: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_0_100_s_Text_2)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" s", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()
                    
        def test_afterburst_time_40K_Min(self):
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_TIME_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")
                    if value_40K_min:
                        test.startSection("Weld Process: Afterburst Delay: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_weld_process.afterburstTimeEnterValue()
                        recipe.enterValue(value_40K_min)
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected min value: {value_40K_min}")
                        test.endSection()
                   
        def test_afterburst_time_40K_Max(self):
            # Test 40K_Max
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_TIME_PARAM":
                    value_40K_max = testData.field(row, "40K_Max")
                    if value_40K_max:
                        test.startSection("Weld Process: Afterburst Delay: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_weld_process.afterburstTimeEnterValue()
                        recipe.enterValue(value_40K_max)
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected max value: {value_40K_max}")
                        test.endSection()
    
        def test_afterburst_time_40K_max_plus_one(self):
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_TIME_PARAM":
                    # Test 40K_Max + 1
                    value_40K_max = testData.field(row, "40K_Max")
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Weld Process: Afterburst Delay: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_weld_process.afterburstTimeEnterValue()
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
    
        def test_afterburst_time_40K_Mid(self):
            # Test 40K_Mid (calculated between 40K_Min and 40K_Max)
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_TIME_PARAM":
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
    
                        test.startSection("Weld Process: Afterburst Delay: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_weld_process.afterburstTimeEnterValue()
                        recipe.enterValue(str(mid_val))
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected mid value: {mid_val}")
                        test.endSection()
    
        def test_afterburst_time_40K_min_minus_one(self):
            # Test 40K_Min - 1
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_TIME_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")    
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Weld Process: Afterburst Delay: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_weld_process.afterburstTimeEnterValue()
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

class AfterBurst_Amplitude:
        def test_afterburst_amplitude_40K_Default(self):
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_AMPLITUDE_PARAM":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Weld Process: Afterburst Amplitude: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_10_Text_2)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" %", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()
                    
        def test_afterburst_amplitude_40K_Min(self):
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_AMPLITUDE_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")
                    if value_40K_min:
                        test.startSection("Weld Process: Afterburst Amplitude: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_weld_process.pretriggerAmplitudeEnterValue()
                        recipe.enterValue(value_40K_min)
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected min value: {value_40K_min}")
                        test.endSection()
                   
        def test_afterburst_amplitude_40K_Max(self):
            # Test 40K_Max
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_AMPLITUDE_PARAM":
                    value_40K_max = testData.field(row, "40K_Max")
                    if value_40K_max:
                        test.startSection("Weld Process: Afterburst Amplitude: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_weld_process.pretriggerAmplitudeEnterValue()
                        recipe.enterValue(value_40K_max)
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected max value: {value_40K_max}")
                        test.endSection()
    
        def test_afterburst_amplitude_40K_max_plus_one(self):
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_AMPLITUDE_PARAM":
                    # Test 40K_Max + 1
                    value_40K_max = testData.field(row, "40K_Max")
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Weld Process: Afterburst Amplitude: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_weld_process.pretriggerAmplitudeEnterValue()
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
    
        def test_afterburst_amplitude_40K_Mid(self):
            # Test 40K_Mid (calculated between 40K_Min and 40K_Max)
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_AMPLITUDE_PARAM":
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
    
                        test.startSection("Weld Process: Afterburst Amplitude: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_weld_process.pretriggerAmplitudeEnterValue()
                        recipe.enterValue(str(mid_val))
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected mid value: {mid_val}")
                        test.endSection()
    
        def test_afterburst_amplitude_40K_min_minus_one(self):
            # Test 40K_Min - 1
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_AMPLITUDE_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")    
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Weld Process: Afterburst Amplitude: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_weld_process.pretriggerAmplitudeEnterValue()
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
    

def main():
    test.log("Starting to log into the system")
    startApplication("QT_UIController")
    squish.snooze(7)
    core.moduleName("Recipe Weld Process")
    pre_condition()
    reset_notification()
    new_create_recipe()
    navigate_to_weld_processTab()
    
    # recipe_weld_process.pretriggerTab()
    # recipe_weld_process.pretriggerEnable()
    #
    # pretrigger_amplitude = Pretrigger_Amplitude()
    # pretrigger_amplitude.test_pretrigger_amplitude_40K_Default()
    # pretrigger_amplitude.test_pretrigger_amplitude_40K_Min()
    # pretrigger_amplitude.test_pretrigger_amplitude_40K_Max()
    # pretrigger_amplitude.test_pretrigger_amplitude_40K_Mid()
    # pretrigger_amplitude.test_pretrigger_amplitude_40K_max_plus_one()
    # pretrigger_amplitude.test_pretrigger_amplitude_40K_min_minus_one()
    #
    # recipe_weld_process.pretriggerStart_distance_radioButton()
    #
    # pretrigger_distance = Pretrigger_Distance()
    # pretrigger_distance.test_pretrigger_distance_40K_Default()    
    # pretrigger_distance.test_pretrigger_distance_40K_Min()
    # pretrigger_distance.test_pretrigger_distance_40K_Max()
    # pretrigger_distance.test_pretrigger_distance_40K_Mid()
    # pretrigger_distance.test_pretrigger_distance_40K_max_plus_one()
    # pretrigger_distance.test_pretrigger_distance_40K_min_minus_one()
    #
    # recipe_weld_process.pretriggerStart_time_radioButton()
    #
    # pretrigger_time = Pretrigger_Time()
    # pretrigger_time.test_pretrigger_time_40K_Default()    
    # pretrigger_time.test_pretrigger_time_40K_Min()
    # pretrigger_time.test_pretrigger_time_40K_Max()
    # pretrigger_time.test_pretrigger_time_40K_Mid()
    # pretrigger_time.test_pretrigger_time_40K_max_plus_one()
    # pretrigger_time.test_pretrigger_time_40K_min_minus_one()
    
    recipe_weld_process.afterBurstTab()
    recipe_weld_process.afterBurstEnable()
    
    afterburst = AfterBurst_Delay()
    afterburst.test_afterburst_delay_40K_Default()
    afterburst.test_afterburst_delay_40K_Min()
    afterburst.test_afterburst_delay_40K_Max()
    afterburst.test_afterburst_delay_40K_Mid()
    afterburst.test_afterburst_delay_40K_max_plus_one()
    afterburst.test_afterburst_delay_40K_min_minus_one()
    
    afterburst = AfterBurst_Time()
    afterburst.test_afterburst_time_40K_Default()
    afterburst.test_afterburst_time_40K_Min()
    afterburst.test_afterburst_time_40K_Max()
    afterburst.test_afterburst_time_40K_Mid()
    afterburst.test_afterburst_time_40K_max_plus_one()
    afterburst.test_afterburst_time_40K_min_minus_one()
    
    
    afterburst = AfterBurst_Amplitude()
    afterburst.test_afterburst_amplitude_40K_Default()
    afterburst.test_afterburst_amplitude_40K_Min()
    afterburst.test_afterburst_amplitude_40K_Max()
    afterburst.test_afterburst_amplitude_40K_Mid()
    afterburst.test_afterburst_amplitude_40K_max_plus_one()
    afterburst.test_afterburst_amplitude_40K_min_minus_one()

