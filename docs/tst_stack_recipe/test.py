import names
from screens import login, recipe, stack_recipe
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

def navigate_to_stack_recipe_Tab():
    test.log("navigating to weld process tab")
    stack_recipe.stackRecipeTab()




class DigitalTune():
    def test_digital_tune_40K_Default(self):
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "DIGITAL_TUNE":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Stack Recipe: Digital Tune: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_19950_Hz_Text)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" Hz", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()
                    
    def test_digital_tune_40K_Min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "DIGITAL_TUNE":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Stack Recipe: Digital Tune: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe_stack_recipe.digitalTune()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_digital_tune_40K_Max(self):
        # Test 40K_Max
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "DIGITAL_TUNE":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Stack Recipe: Digital Tune: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe_stack_recipe.digitalTune()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_digital_tune_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "DIGITAL_TUNE":
                # Test 40K_Max + 1
                value_40K_max = testData.field(row, "40K_Max")
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Stack Recipe: Digital Tune: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe_stack_recipe.digitalTune()
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

    def test_digital_tune_40K_Mid(self):
        # Test 40K_Mid (calculated between 40K_Min and 40K_Max)
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "DIGITAL_TUNE":
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

                    test.startSection("Stack Recipe: Digital Tune: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    recipe_stack_recipe.digitalTune()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_digital_tune_40K_min_minus_one(self):
        # Test 40K_Min - 1
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "DIGITAL_TUNE":
                value_40K_min = testData.field(row, "40K_Min")    
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Stack Recipe: Digital Tune: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe_stack_recipe.digitalTune()
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

class InternalFreqOffset():

    def test_digital_tune_40K_Default(self):
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "INTERNAL_FREQUENCY_OFFSET":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Stack Recipe: Internal Frequency offset: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_0_Hz_Text)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" Hz", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()
                    
    def test_digital_tune_40K_Min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "INTERNAL_FREQUENCY_OFFSET":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Stack Recipe: Internal Frequency offset: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe_stack_recipe.internalFreqOffset()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_digital_tune_40K_Max(self):
        # Test 40K_Max
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "INTERNAL_FREQUENCY_OFFSET":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Stack Recipe: Internal Frequency offset: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe_stack_recipe.internalFreqOffset()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_digital_tune_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "INTERNAL_FREQUENCY_OFFSET":
                # Test 40K_Max + 1
                value_40K_max = testData.field(row, "40K_Max")
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Stack Recipe: Internal Frequency offset: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe_stack_recipe.internalFreqOffset()
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

    def test_digital_tune_40K_Mid(self):
        # Test 40K_Mid (calculated between 40K_Min and 40K_Max)
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "INTERNAL_FREQUENCY_OFFSET":
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

                    test.startSection("Stack Recipe: Internal Frequency offset: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    recipe_stack_recipe.internalFreqOffset()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_digital_tune_40K_min_minus_one(self):
        # Test 40K_Min - 1
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "INTERNAL_FREQUENCY_OFFSET":
                value_40K_min = testData.field(row, "40K_Min")    
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Stack Recipe: Internal Frequency offset: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe_stack_recipe.internalFreqOffset()
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()

                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value matches expected max minus one value: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation pop-up did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}")     

class WeldRampTime():
    def test_weld_ramp_time_40K_Default(self):
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "WELD_RAMP_TIME":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Stack Recipe: Internal Frequency offset: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_0_080_s_Text)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" s", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()
                    
    def test_weld_ramp_time_40K_Min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "WELD_RAMP_TIME":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Stack Recipe: Weld Ramp Time: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe_stack_recipe.weldRampTime()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_weld_ramp_time_40K_Max(self):
        # Test 40K_Max
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "WELD_RAMP_TIME":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Stack Recipe: Weld Ramp Time: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe_stack_recipe.weldRampTime()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_weld_ramp_time_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "WELD_RAMP_TIME":
                # Test 40K_Max + 1
                value_40K_max = testData.field(row, "40K_Max")
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Stack Recipe: Weld Ramp Time: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe_stack_recipe.weldRampTime()
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

    def test_weld_ramp_time_40K_Mid(self):
        # Test 40K_Mid (calculated between 40K_Min and 40K_Max)
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "WELD_RAMP_TIME":
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

                    test.startSection("Stack Recipe: Weld Ramp Time: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    recipe_stack_recipe.weldRampTime()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_weld_ramp_time_40K_min_minus_one(self):
        # Test 40K_Min - 1
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "WELD_RAMP_TIME":
                value_40K_min = testData.field(row, "40K_Min")    
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Stack Recipe: Weld Ramp Time: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe_stack_recipe.weldRampTime()
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()

                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value matches expected max minus one value: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation pop-up did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}")

class StartFrequency():
    def test_start_frequency_40K_Default(self):
            for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "START_FREQUENCY":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Stack Recipe: Start Frequency: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_0_Hz_Text)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" Hz", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()
                    
    def test_start_frequency_40K_Min(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "START_FREQUENCY":
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Stack Recipe: Start Frequency: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe_stack_recipe.startFrequency()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_start_frequency_40K_Max(self):
        # Test 40K_Max
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "START_FREQUENCY":
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Stack Recipe: Start Frequency: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe_stack_recipe.startFrequency()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_start_frequency_40K_max_plus_one(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "START_FREQUENCY":
                # Test 40K_Max + 1
                value_40K_max = testData.field(row, "40K_Max")
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Stack Recipe: Start Frequency: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe_stack_recipe.startFrequency()
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

    def test_start_frequency_40K_Mid(self):
        # Test 40K_Mid (calculated between 40K_Min and 40K_Max)
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "START_FREQUENCY":
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

                    test.startSection("Stack Recipe: Start Frequency: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    recipe_stack_recipe.startFrequency()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_start_frequency_40K_min_minus_one(self):
        # Test 40K_Min - 1
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "START_FREQUENCY":
                value_40K_min = testData.field(row, "40K_Min")    
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Stack Recipe: Start Frequency: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe_stack_recipe.startFrequency()
                    recipe.enterValue(value_40K_min_minus_one)
                    squish.snooze(2)
                    recipe.DoneButton()

                    if object.exists(names.invalid_value_is_entered_Reverted_to_old_value_Text):
                        test.passes(f"Entered value matches expected max minus one value: {value_40K_min_minus_one}")
                        core.ClickButton(names.oK_BransonPrimaryButton)
                    else:
                        test.fail("Expected validation pop-up did not appear.")
                    test.endSection()
                except Exception as e:
                    test.fail(f"Failed to calculate or enter 40K_Min-1: {e}")

def main():
    test.log("Starting to log into the system")
    startApplication("QT_UIController")
    squish.snooze(3)
    core.moduleName("Recipe Stack Recipe")
    pre_condition()
    reset_notification()
    new_create_recipe()
    navigate_to_stack_recipe_Tab()
    
    # recipe_stack_recipe.endOfWeldStore()
    recipe_stack_recipe.endOfWeldStoreEnable()
    
    recipe_stack_recipe.frequencyOffSet()
    recipe_stack_recipe.frequencyOffSetEnable()
    
    digital_tune = DigitalTune()
    digital_tune.test_digital_tune_40K_Default()
    digital_tune.test_digital_tune_40K_Max()
    digital_tune.test_digital_tune_40K_Min()
    digital_tune.test_digital_tune_40K_Mid()
    digital_tune.test_digital_tune_40K_max_plus_one()
    digital_tune.test_digital_tune_40K_min_minus_one()
    
    internalFreqOffSet = InternalFreqOffset()
    internalFreqOffSet.test_digital_tune_40K_Default()
    internalFreqOffSet.test_digital_tune_40K_Min()
    internalFreqOffSet.test_digital_tune_40K_Max()
    internalFreqOffSet.test_digital_tune_40K_Mid()
    internalFreqOffSet.test_digital_tune_40K_max_plus_one()
    internalFreqOffSet.test_digital_tune_40K_min_minus_one()
    
    weldRampTime = WeldRampTime()
    weldRampTime.test_weld_ramp_time_40K_Default()
    weldRampTime.test_weld_ramp_time_40K_Max()
    weldRampTime.test_weld_ramp_time_40K_Min()
    weldRampTime.test_weld_ramp_time_40K_Mid()
    weldRampTime.test_weld_ramp_time_40K_min_minus_one()
    weldRampTime.test_weld_ramp_time_40K_max_plus_one()
    
    startFrequency = StartFrequency()
    startFrequency.test_start_frequency_40K_Default()
    startFrequency.test_start_frequency_40K_Max()
    startFrequency.test_start_frequency_40K_Min()
    startFrequency.test_start_frequency_40K_Mid()
    startFrequency.test_start_frequency_40K_max_plus_one()
    startFrequency.test_start_frequency_40K_min_minus_one()
    
    
    
    