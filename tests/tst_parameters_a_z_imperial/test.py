import names
from screens import login, recipe, recipe_parameters, user_setting, common
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
    
def Set_Imperial():
    user_setting.change_to_imperial_unit()
    
def navigate_To_ParamsTab():
    test.log("navigating to parameters a-z tab")
    recipe_parameters.paramseters_a_z()

class AfterBurst_Delay:
    def test_afterburst_delay_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "AFTER_BURST_DELAY_PARAM":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Afterburst Delay: Test 40K_Default Displayed Value")
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
                    test.startSection("Afterburst Delay: Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    recipe_parameters.params_afterBurstDelay()
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
                    test.startSection("Afterburst Delay: Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    recipe_parameters.params_afterBurstDelay()
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
                    test.startSection("Afterburst Delay: Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    recipe_parameters.params_afterBurstDelay()
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

                    test.startSection("Afterburst Delay: Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    recipe_parameters.params_afterBurstDelay()
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
                    test.startSection("Afterburst Delay: Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    recipe_parameters.params_afterBurstDelay()
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
                        test.startSection("Afterburst Delay: Test 40K_Default Displayed Value")
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
                        test.startSection("Afterburst Delay: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_parameters.params_afterBurstTime()
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
                        test.startSection("Afterburst Delay: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_parameters.params_afterBurstTime()
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
                        test.startSection("Afterburst Delay: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_parameters.params_afterBurstTime()
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
    
                        test.startSection("Afterburst Delay: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_parameters.params_afterBurstTime()
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
                        test.startSection("Afterburst Delay: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_parameters.params_afterBurstTime()
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
                        test.startSection("Afterburst Amplitude: Test 40K_Default Displayed Value")
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
                        test.startSection("Afterburst Amplitude: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_parameters.params_afterBurstAmplitude()
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
                        test.startSection("Afterburst Amplitude: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_parameters.params_afterBurstAmplitude()
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
                        test.startSection("Afterburst Amplitude: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_parameters.params_afterBurstAmplitude()
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
    
                        test.startSection("Afterburst Amplitude: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_parameters.params_afterBurstAmplitude()
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
                        test.startSection("Afterburst Amplitude: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_parameters.params_afterBurstAmplitude()
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

class Actuator:
    
    def test_actuator_distance_40K_Default(self):
        pass
    
    def test_actuator_distance_40K_Min(self):
        pass
    
    def test_actuator_distance_40K_Max(self):
        pass
    
    def test_actuator_distance_40K_Mid(self):
        pass
    
    def test_actuator_distance_40K_max_plus_one(self):
        pass
    
    def test_actuator_distance_40K_min_minus_one(self):
        pass
    
class Pretrigger_Amplitude:
    def test_pretrigger_amplitude_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_AMPLITUDE_PARAM":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Pretrigger Amplitude: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_10_Text_3)
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
                        test.startSection("Pretrigger Amplitude: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_parameters.params_pretriggerAmplitude()
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
                        test.startSection("Pretrigger Amplitude: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_parameters.params_pretriggerAmplitude()
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
    
                        test.startSection("Pretrigger Amplitude: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_parameters.params_pretriggerAmplitude()
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
                        test.startSection("Pretrigger Amplitude: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_parameters.params_pretriggerAmplitude()
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
                        test.startSection("Pretrigger Amplitude: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_parameters.params_pretriggerAmplitude()
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
                        test.startSection("Pretrigger Distance: Test 40K_Default Displayed Value")
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
                        test.startSection("Pretrigger Distance: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_parameters.params_pretriggerDistance()
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
                        test.startSection("Pretrigger Distance: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_parameters.params_pretriggerDistance()
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
    
                        test.startSection("Pretrigger Distance: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_parameters.params_pretriggerDistance()
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
                        test.startSection("Pretrigger Distance: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_parameters.params_pretriggerDistance()
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
                        test.startSection("Pretrigger Distance: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_parameters.params_pretriggerDistance()
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
                        test.startSection("Pretrigger Time: Test 40K_Default Displayed Value")
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
                        test.startSection("Pretrigger Time: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_parameters.params_pretriggerTime()
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
                        test.startSection("Pretrigger Time: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_parameters.params_pretriggerTime()
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
    
                        test.startSection("Pretrigger Time: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_parameters.params_pretriggerTime()
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
                        test.startSection("Pretrigger Time: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_parameters.params_pretriggerTime()
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
                        test.startSection("Pretrigger Time: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_parameters.params_pretriggerTime()
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
                        

class EnergyBrakeTime:
    
    def test_energy_brake_time_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_BRAKE_TIME_PARAM":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Energy brake Time: Test 40K_Default Displayed Value")
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
    
    def test_energy_brake_time_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_BRAKE_TIME_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")
                    if value_40K_min:
                        test.startSection("Energy brake Time: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_parameters.energyBrakeTime()
                        recipe.enterValue(value_40K_min)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected min value: {value_40K_min}")
                        test.endSection()
    
    def test_energy_brake_time_40K_Max(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_BRAKE_TIME_PARAM":
                    value_40K_max = testData.field(row, "40K_Max")
                    if value_40K_max:
                        test.startSection("Energy brake Time: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_parameters.energyBrakeTime()
                        recipe.enterValue(value_40K_max)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected max value: {value_40K_max}")
                        test.endSection()
    
    def test_energy_brake_time_40K_Mid(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_BRAKE_TIME_PARAM":
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
    
                        test.startSection("Energy brake Time: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_parameters.energyBrakeTime()
                        recipe.enterValue(str(mid_val))
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected mid value: {mid_val}")
                        test.endSection()
    
    def test_energy_brake_time_40K_max_plus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_BRAKE_TIME_PARAM" :
                    # Test 40K_Max + 1
                    value_40K_max = testData.field(row, "40K_Max")
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Energy brake Time: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_parameters.energyBrakeTime()
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
    
    def test_energy_brake_time_40K_min_minus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_BRAKE_TIME_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")    
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Energy brake Time: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_parameters.energyBrakeTime()
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


class EnergyBrakeAmplitude:
    
    def test_energy_brake_amplitude_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_BRAKE_AMPLITUDE_PARAM":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Energy brake Amplitude: Test 40K_Default Displayed Value")
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
    
    def test_energy_brake_amplitude_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_BRAKE_AMPLITUDE_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")
                    if value_40K_min:
                        test.startSection("Energy brake Amplitude: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_parameters.energyBrakeAmplitude()
                        recipe.enterValue(value_40K_min)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected min value: {value_40K_min}")
                        test.endSection()
    
    def test_energy_brake_amplitude_40K_Max(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_BRAKE_AMPLITUDE_PARAM":
                    value_40K_max = testData.field(row, "40K_Max")
                    if value_40K_max:
                        test.startSection("Energy brake Amplitude: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_parameters.energyBrakeAmplitude()
                        recipe.enterValue(value_40K_max)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected max value: {value_40K_max}")
                        test.endSection()
    
    def test_energy_brake_amplitude_40K_Mid(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_BRAKE_AMPLITUDE_PARAM":
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
    
                        test.startSection("Energy brake Amplitude: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_parameters.energyBrakeAmplitude()
                        recipe.enterValue(str(mid_val))
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected mid value: {mid_val}")
                        test.endSection()
    
    def test_energy_brake_amplitude_40K_max_plus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_BRAKE_AMPLITUDE_PARAM" :
                    # Test 40K_Max + 1
                    value_40K_max = testData.field(row, "40K_Max")
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Energy brake Amplitude: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_parameters.energyBrakeAmplitude()
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
    
    def test_energy_brake_amplitude_40K_min_minus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "ENERGY_BRAKE_AMPLITUDE_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")    
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Energy brake Amplitude: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_parameters.energyBrakeAmplitude()
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

class MaxTimeout:
    
    def test_max_timeout_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MAX_WELD_TIMEOUT_PARAM":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Max Timeout: Test 40K_Default Displayed Value")
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
    
    def test_max_timeout_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MAX_WELD_TIMEOUT_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")
                    if value_40K_min:
                        test.startSection("Max Timeout: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_parameters.maxTimeout()
                        recipe.enterValue(value_40K_min)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected min value: {value_40K_min}")
                        test.endSection()
    
    def test_max_timeout_40K_Max(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MAX_WELD_TIMEOUT_PARAM":
                    value_40K_max = testData.field(row, "40K_Max")
                    if value_40K_max:
                        test.startSection("Max Timeout: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_parameters.maxTimeout()
                        recipe.enterValue(value_40K_max)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected max value: {value_40K_max}")
                        test.endSection()
    
    def test_max_timeout_40K_Mid(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MAX_WELD_TIMEOUT_PARAM":
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
    
                        test.startSection("Max Timeout: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_parameters.maxTimeout()
                        recipe.enterValue(str(mid_val))
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected mid value: {mid_val}")
                        test.endSection()
    
    def test_max_timeout_40K_max_plus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MAX_WELD_TIMEOUT_PARAM" :
                    # Test 40K_Max + 1
                    value_40K_max = testData.field(row, "40K_Max")
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Max Timeout: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_parameters.maxTimeout()
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
    
    def test_max_timeout_40K_min_minus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "MAX_WELD_TIMEOUT_PARAM":
                    value_40K_min = testData.field(row, "40K_Min")    
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Max Timeout: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_parameters.maxTimeout()
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

class RapidTraverseDistance:
    
    def test_rapid_traverse_distance_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "RAPID_TRAVERSE_DISTANCE":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Rapid Traverse Distance: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_0_0000_in_Text)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" in", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()

    def test_rapid_traverse_distance_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "RAPID_TRAVERSE_DISTANCE":
                    value_40K_min = testData.field(row, "40K_Min")
                    if value_40K_min:
                        test.startSection("Rapid Traverse Distance: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_parameters.rapidTraverseDistance()
                        recipe.enterValue(value_40K_min)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected min value: {value_40K_min}")
                        test.endSection()
    
    def test_rapid_traverse_distance_40K_Max(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "RAPID_TRAVERSE_DISTANCE":
                    value_40K_max = testData.field(row, "40K_Max")
                    if value_40K_max:
                        test.startSection("Rapid Traverse Distance: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_parameters.rapidTraverseDistance()
                        recipe.enterValue(value_40K_max)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected max value: {value_40K_max}")
                        test.endSection()
    
    def test_rapid_traverse_distance_40K_Mid(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "RAPID_TRAVERSE_DISTANCE":
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
    
                        test.startSection("Rapid Traverse Distance: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_parameters.rapidTraverseDistance()
                        recipe.enterValue(str(mid_val))
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected mid value: {mid_val}")
                        test.endSection()
    
    def test_rapid_traverse_distance_40K_max_plus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "RAPID_TRAVERSE_DISTANCE" :
                    # Test 40K_Max + 1
                    value_40K_max = testData.field(row, "40K_Max")
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Rapid Traverse Distance: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_parameters.rapidTraverseDistance()
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
    
    def test_rapid_traverse_distance_40K_min_minus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "RAPID_TRAVERSE_DISTANCE":
                    value_40K_min = testData.field(row, "40K_Min")    
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Rapid Traverse Distance: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_parameters.rapidTraverseDistance()
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

class TriggerDistance:
    
    def test_trigger_distance_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Trigger Distance: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_0_0000_in_Text_2)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" in", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()

    def test_trigger_distance_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
                    value_40K_min = testData.field(row, "40K_Min")
                    if value_40K_min:
                        test.startSection("Trigger Distance: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_parameters.triggerDistance()
                        recipe.enterValue(value_40K_min)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected min value: {value_40K_min}")
                        test.endSection()
    
    def test_trigger_distance_40K_Max(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
                    value_40K_max = testData.field(row, "40K_Max")
                    if value_40K_max:
                        test.startSection("Trigger Distance: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_parameters.triggerDistance()
                        recipe.enterValue(value_40K_max)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected max value: {value_40K_max}")
                        test.endSection()
    
    def test_trigger_distance_40K_Mid(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
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
    
                        test.startSection("Trigger Distance: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_parameters.triggerDistance()
                        recipe.enterValue(str(mid_val))
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected mid value: {mid_val}")
                        test.endSection()
    
    def test_trigger_distance_40K_max_plus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE" :
                    # Test 40K_Max + 1
                    value_40K_max = testData.field(row, "40K_Max")
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Trigger Distance: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_parameters.triggerDistance()
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
    
    def test_trigger_distance_40K_min_minus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
                    value_40K_min = testData.field(row, "40K_Min")    
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Trigger Distance: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_parameters.triggerDistance()
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


class TriggerForce:
    
    def test_trigger_force_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Trigger Force: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject()
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" in", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()

    def test_trigger_force_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
                    value_40K_min = testData.field(row, "40K_Min")
                    if value_40K_min:
                        test.startSection("Trigger Force: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_parameters.triggerDistance()
                        recipe.enterValue(value_40K_min)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected min value: {value_40K_min}")
                        test.endSection()
    
    def test_trigger_force_40K_Max(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
                    value_40K_max = testData.field(row, "40K_Max")
                    if value_40K_max:
                        test.startSection("Trigger Force: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_parameters.triggerDistance()
                        recipe.enterValue(value_40K_max)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected max value: {value_40K_max}")
                        test.endSection()
    
    def test_trigger_force_40K_Mid(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
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
    
                        test.startSection("Trigger Force: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_parameters.triggerDistance()
                        recipe.enterValue(str(mid_val))
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected mid value: {mid_val}")
                        test.endSection()
    
    def test_trigger_force_40K_max_plus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE" :
                    # Test 40K_Max + 1
                    value_40K_max = testData.field(row, "40K_Max")
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Trigger Force: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_parameters.triggerDistance()
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
    
    def test_trigger_force_40K_min_minus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "IMPERIAL" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
                    value_40K_min = testData.field(row, "40K_Min")    
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Trigger Force: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_parameters.triggerDistance()
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
                        
class TimeSeekPeriod:
    
    def test_time_seek_period_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME SEEK PERIOD":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Time Seek Period: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_1_000_min_Text)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" min", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()

    def test_time_seek_period_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME SEEK PERIOD":
                    value_40K_min = testData.field(row, "40K_Min")
                    if value_40K_min:
                        test.startSection("Time Seek Period: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_parameters.timeSeekPeriod()
                        recipe.enterValue(value_40K_min)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected min value: {value_40K_min}")
                        test.endSection()
    
    def test_time_seek_period_40K_Max(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME SEEK PERIOD":
                    value_40K_max = testData.field(row, "40K_Max")
                    if value_40K_max:
                        test.startSection("Time Seek Period: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_parameters.timeSeekPeriod()
                        recipe.enterValue(value_40K_max)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected max value: {value_40K_max}")
                        test.endSection()
    
    def test_time_seek_period_40K_Mid(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME SEEK PERIOD":
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
    
                        test.startSection("Time Seek Period: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_parameters.timeSeekPeriod()
                        recipe.enterValue(str(mid_val))
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected mid value: {mid_val}")
                        test.endSection()
    
    def test_time_seek_period_40K_max_plus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME SEEK PERIOD" :
                    # Test 40K_Max + 1
                    value_40K_max = testData.field(row, "40K_Max")
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Time Seek Period: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_parameters.timeSeekPeriod()
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
    
    def test_time_seek_period_40K_min_minus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "TIME SEEK PERIOD":
                    value_40K_min = testData.field(row, "40K_Min")    
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Time Seek Period: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_parameters.timeSeekPeriod()
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


class ScrubAmplitude:
    
    def test_scrub_amplitude_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "SCRUB AMPLITUDE":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Time Seek Period: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_100_Text)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" %", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()

    def test_scrub_amplitude_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "SCRUB AMPLITUDE":
                    value_40K_min = testData.field(row, "40K_Min")
                    if value_40K_min:
                        test.startSection("Time Seek Period: Test 40K_Min")
                        test.log(f"Testing 40K_Min: {value_40K_min}")
                        recipe_parameters.scrubAmplitude()
                        recipe.enterValue(value_40K_min)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected min value: {value_40K_min}")
                        test.endSection()
    
    def test_scrub_amplitude_40K_Max(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "SCRUB AMPLITUDE":
                    value_40K_max = testData.field(row, "40K_Max")
                    if value_40K_max:
                        test.startSection("Time Seek Period: Test 40K_Max")
                        test.log(f"Testing 40K_Max: {value_40K_max}")
                        recipe_parameters.scrubAmplitude()
                        recipe.enterValue(value_40K_max)
                        squish.snooze(0.2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected max value: {value_40K_max}")
                        test.endSection()
    
    def test_scrub_amplitude_40K_Mid(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "SCRUB AMPLITUDE":
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
    
                        test.startSection("Time Seek Period: Test 40K_Mid")
                        test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                        recipe_parameters.scrubAmplitude()
                        recipe.enterValue(str(mid_val))
                        squish.snooze(2)
                        recipe.DoneButton()
                        test.passes(f"Entered value matches expected mid value: {mid_val}")
                        test.endSection()
    
    def test_scrub_amplitude_40K_max_plus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "SCRUB AMPLITUDE" :
                    # Test 40K_Max + 1
                    value_40K_max = testData.field(row, "40K_Max")
                    try:
                        value_40K_max_plus_one = str(float(value_40K_max) + 1)
                        test.startSection("Time Seek Period: Test 40K_Max + 1 (Out of Range)")
                        test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                        recipe_parameters.scrubAmplitude()
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
    
    def test_scrub_amplitude_40K_min_minus_one(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "SCRUB AMPLITUDE":
                    value_40K_min = testData.field(row, "40K_Min")    
                    try:
                        value_40K_min_minus_one = str(float(value_40K_min) - 1)
                        test.startSection("Time Seek Period: Test 40K_Min - 1 (Out of Range)")
                        test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                        recipe_parameters.scrubAmplitude()
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
    core.moduleName("Recipe Parameters A-Z")
    pre_condition()
    reset_notification()
    Set_Imperial()
    new_create_recipe()
    
    navigate_To_ParamsTab()
    core.scroll(names.recipeLabWindow_infoScrollRec_Flickable)
    core.scroll(names.recipeLabWindow_infoScrollRec_Flickable)
    core.scroll(names.recipeLabWindow_infoScrollRec_Flickable)
    core.scroll(names.recipeLabWindow_infoScrollRec_Flickable)
    # common.scroll_params()
    # common.scroll_params()
    # common.scroll_params()
    # recipe_parameters.params_afterBurstcard()
    # recipe_parameters.params_afterBurstEnable()
    #
    # afterburst = AfterBurst_Delay()
    # afterburst.test_afterburst_delay_40K_Default()
    # afterburst.test_afterburst_delay_40K_Min()
    # afterburst.test_afterburst_delay_40K_Max()
    # afterburst.test_afterburst_delay_40K_Mid()
    # afterburst.test_afterburst_delay_40K_max_plus_one()
    # afterburst.test_afterburst_delay_40K_min_minus_one()
    #
    # afterburst = AfterBurst_Time()
    # afterburst.test_afterburst_time_40K_Default()
    # afterburst.test_afterburst_time_40K_Min()
    # afterburst.test_afterburst_time_40K_Max()
    # afterburst.test_afterburst_time_40K_Mid()
    # afterburst.test_afterburst_time_40K_max_plus_one()
    # afterburst.test_afterburst_time_40K_min_minus_one()
    #
    # afterburst = AfterBurst_Amplitude()
    # afterburst.test_afterburst_amplitude_40K_Default()
    # afterburst.test_afterburst_amplitude_40K_Min()
    # afterburst.test_afterburst_amplitude_40K_Max()
    # afterburst.test_afterburst_amplitude_40K_Mid()
    # afterburst.test_afterburst_amplitude_40K_max_plus_one()
    # afterburst.test_afterburst_amplitude_40K_min_minus_one()
    #
    # recipe_parameters.perform_scroll_actions()
    #
    # recipe_parameters.energyBraking()
    # recipe_parameters.energyBrakingEnable()
    #
    # energyBrakeTime = EnergyBrakeTime()
    # energyBrakeTime.test_energy_brake_time_40K_Max()
    # energyBrakeTime.test_energy_brake_time_40K_Min()
    # energyBrakeTime.test_energy_brake_time_40K_Mid()
    # energyBrakeTime.test_energy_brake_time_40K_min_minus_one()
    # energyBrakeTime.test_energy_brake_time_40K_max_plus_one()
    #
    # energyBrakeAmplitude = EnergyBrakeAmplitude()
    # energyBrakeAmplitude.test_energy_brake_amplitude_40K_Max()
    # energyBrakeAmplitude.test_energy_brake_amplitude_40K_Min()
    # energyBrakeAmplitude.test_energy_brake_amplitude_40K_Mid()
    # energyBrakeAmplitude.test_energy_brake_amplitude_40K_min_minus_one()
    # energyBrakeAmplitude.test_energy_brake_amplitude_40K_max_plus_one()
    #
    # recipe_parameters.perform_scroll_actions()
    # recipe_parameters.perform_scroll_actions()
    #
    # recipe_parameters.extraCooling()
    # recipe_parameters.extraCoolingEnable()
    #
    #
    # maxTimeout = MaxTimeout()
    # maxTimeout.test_max_timeout_40K_Min()
    # maxTimeout.test_max_timeout_40K_Max()
    # maxTimeout.test_max_timeout_40K_Mid()
    # maxTimeout.test_max_timeout_40K_max_plus_one()
    # maxTimeout.test_max_timeout_40K_min_minus_one()
    #
    # recipe_parameters.perform_scroll_actions()
    #
    # recipe_parameters.preWeldSeek()
    # recipe_parameters.preWeldSeekEnable()
    #
    # recipe_parameters.postWeldSeek()
    # recipe_parameters.postWeldSeekEnable()
    #
    recipe_parameters.params_pretrigger()
    recipe_parameters.params_pretriggerEnable()
    #
    # pretrigger_amplitude = Pretrigger_Amplitude()
    # pretrigger_amplitude.test_pretrigger_amplitude_40K_Default()
    # pretrigger_amplitude.test_pretrigger_amplitude_40K_Min()
    # pretrigger_amplitude.test_pretrigger_amplitude_40K_Max()
    # pretrigger_amplitude.test_pretrigger_amplitude_40K_Mid()
    # pretrigger_amplitude.test_pretrigger_amplitude_40K_max_plus_one()
    # pretrigger_amplitude.test_pretrigger_amplitude_40K_min_minus_one()
    #
    # # recipe_parameters.perform_scroll_actions()
    #
    # recipe_parameters.params_pretriggerStart()
    # recipe_parameters.params_pretriggerDistanceSelected()
    #
    # pretrigger_distance = Pretrigger_Distance()
    # pretrigger_distance.test_pretrigger_distance_40K_Default()    
    # pretrigger_distance.test_pretrigger_distance_40K_Min()
    # pretrigger_distance.test_pretrigger_distance_40K_Max()
    # pretrigger_distance.test_pretrigger_distance_40K_Mid()
    # pretrigger_distance.test_pretrigger_distance_40K_max_plus_one()
    # pretrigger_distance.test_pretrigger_distance_40K_min_minus_one()
    
    recipe_parameters.params_pretriggerStart()
    recipe_parameters.params_pretriggerTimeSelected()
    
    pretrigger_time = Pretrigger_Time()
    # pretrigger_time.test_pretrigger_time_40K_Default()    
    pretrigger_time.test_pretrigger_time_40K_Min()
    # pretrigger_time.test_pretrigger_time_40K_Max()
    # pretrigger_time.test_pretrigger_time_40K_Mid()
    # pretrigger_time.test_pretrigger_time_40K_max_plus_one()
    # pretrigger_time.test_pretrigger_time_40K_min_minus_one()
    
    core.scroll(names.recipeLabWindow_infoScrollRec_Flickable)
    
    
    # recipe_parameters.perform_scroll_actions()
    # recipe_parameters.perform_scroll_actions()
    
    # rapidTraverseDistance = RapidTraverseDistance()
    #
    # recipe_parameters.rapidTravserse()
    # recipe_parameters.rapidTraverseEnable()
    # rapidTraverseDistance.test_rapid_traverse_distance_40K_Default()
    # rapidTraverseDistance.test_rapid_traverse_distance_40K_Max()
    # rapidTraverseDistance.test_rapid_traverse_distance_40K_Min()
    # rapidTraverseDistance.test_rapid_traverse_distance_40K_Mid()
    # rapidTraverseDistance.test_rapid_traverse_distance_40K_max_plus_one()
    # rapidTraverseDistance.test_rapid_traverse_distance_40K_min_minus_one()
    #
    # recipe_parameters.triggerLost()
    # recipe_parameters.triggerLostEnable()
    #
    # recipe_parameters.externalAmplitudeSetting()
    #
    # recipe_parameters.triggerType()
    # recipe_parameters.triggerTypeDistanceSelected()
    #
    # recipe_parameters.perform_scroll_actions()
    #
    # triggerDistance = TriggerDistance()
    # triggerDistance.test_trigger_distance_40K_Default()
    # triggerDistance.test_trigger_distance_40K_Max()
    # triggerDistance.test_trigger_distance_40K_Min()
    # triggerDistance.test_trigger_distance_40K_Mid()
    # triggerDistance.test_trigger_distance_40K_max_plus_one()
    # triggerDistance.test_trigger_distance_40K_min_minus_one()
    #
    #
    # recipe_parameters.timeSeek()
    #
    # timeSeekPeriod = TimeSeekPeriod()
    # timeSeekPeriod.test_time_seek_period_40K_Default()
    # timeSeekPeriod.test_time_seek_period_40K_Max()
    # timeSeekPeriod.test_time_seek_period_40K_Min()
    # timeSeekPeriod.test_time_seek_period_40K_Mid()
    # timeSeekPeriod.test_time_seek_period_40K_max_plus_one()
    # timeSeekPeriod.test_time_seek_period_40K_min_minus_one()
    #
    # scrubAmplitude = ScrubAmplitude()
    # scrubAmplitude.test_scrub_amplitude_40K_Default()
    # scrubAmplitude.test_scrub_amplitude_40K_Max()
    # scrubAmplitude.test_scrub_amplitude_40K_Min()
    # scrubAmplitude.test_scrub_amplitude_40K_Mid()
    # scrubAmplitude.test_scrub_amplitude_40K_max_plus_one()
    # scrubAmplitude.test_scrub_amplitude_40K_min_minus_one()
    
    
    