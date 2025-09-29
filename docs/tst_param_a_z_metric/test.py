import names
from screens import login, recipe, recipe_parameters, user_setting
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
    
def Set_Metric():
    user_setting.change_to_metric_unit()
    
def navigate_To_ParamsTab():
    test.log("navigating to parameters a-z tab")
    recipe_parameters.paramseters_a_z()


class Pretrigger_Distance:
    def test_pretrigger_distance_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_DISTANCE_PARAM" and testData.field(row, "UNIT_TYPE") == "METRIC":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Pretrigger Distance: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_3_17_mm_Text)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" mm", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()
    
    def test_pretrigger_distance_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_DISTANCE_PARAM" and testData.field(row, "UNIT_TYPE") == "METRIC":
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
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_DISTANCE_PARAM" and testData.field(row, "UNIT_TYPE") == "METRIC":
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
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_DISTANCE_PARAM" and testData.field(row, "UNIT_TYPE") == "METRIC":
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
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_DISTANCE_PARAM" and testData.field(row, "UNIT_TYPE") == "METRIC":
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
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "PRE_TRIGGER_DISTANCE_PARAM" and testData.field(row, "UNIT_TYPE") == "METRIC":
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
                        
class RapidTraverseDistance:
    
    def test_rapid_traverse_distance_40K_Default(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "METRIC" and testData.field(row, "Param_ID") == "RAPID_TRAVERSE_DISTANCE":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Rapid Traverse Distance: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_0_00_mm_Text)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" mm", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()

    def test_rapid_traverse_distance_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "METRIC" and testData.field(row, "Param_ID") == "RAPID_TRAVERSE_DISTANCE":
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
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "METRIC" and testData.field(row, "Param_ID") == "RAPID_TRAVERSE_DISTANCE":
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
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "METRIC" and testData.field(row, "Param_ID") == "RAPID_TRAVERSE_DISTANCE":
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
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "METRIC" and testData.field(row, "Param_ID") == "RAPID_TRAVERSE_DISTANCE" :
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
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "METRIC" and testData.field(row, "Param_ID") == "RAPID_TRAVERSE_DISTANCE":
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
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "METRIC" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
                    value_40K_default = testData.field(row, "40K_Default")
                    if value_40K_default:
                        test.startSection("Trigger Distance: Test 40K_Default Displayed Value")
                        test.log(f"Testing 40K_Default: {value_40K_default}")
                        try:
                            obj = waitForObject(names.recipeLabWindow_0_00_mm_Text_2)
                            displayed_value = str(obj.text)
                            displayed_value_clean = displayed_value.replace(" mm", "").strip()
                            if displayed_value_clean == value_40K_default.strip():
                                test.passes(f"Displayed value matches expected default: {displayed_value_clean}")
                            else:
                                test.fail(f'Expected "{value_40K_default}" but got "{displayed_value}" in UI')
                        except Exception as e:
                            test.fail(f"Error reading or comparing displayed value: {e}")
                        test.endSection()

    def test_trigger_distance_40K_Min(self):
        for row in dataset:
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "METRIC" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
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
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "METRIC" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
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
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "METRIC" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
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
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "METRIC" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE" :
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
                if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "UNIT_TYPE") == "METRIC" and testData.field(row, "Param_ID") == "TRIGGER_DISTANCE":
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

def main():
    test.log("Starting to log into the system")
    startApplication("QT_UIController")
    squish.snooze(7)
    core.moduleName("Recipe Parameters A-Z")
    pre_condition()
    reset_notification()
    Set_Metric()
    new_create_recipe()
    
    navigate_To_ParamsTab()    

    recipe_parameters.perform_scroll_actions()
    recipe_parameters.perform_scroll_actions()
    recipe_parameters.perform_scroll_actions()
    
    recipe_parameters.params_pretrigger()
    recipe_parameters.params_pretriggerEnable()
    
    recipe_parameters.params_pretriggerStart()
    recipe_parameters.params_pretriggerDistanceSelected()
    
    pretrigger_distance = Pretrigger_Distance()
    pretrigger_distance.test_pretrigger_distance_40K_Default()    
    pretrigger_distance.test_pretrigger_distance_40K_Min()
    pretrigger_distance.test_pretrigger_distance_40K_Max()
    pretrigger_distance.test_pretrigger_distance_40K_Mid()
    pretrigger_distance.test_pretrigger_distance_40K_max_plus_one()
    pretrigger_distance.test_pretrigger_distance_40K_min_minus_one()
    
    recipe_parameters.perform_scroll_actions()
    
    rapidTraverseDistance = RapidTraverseDistance()
    
    recipe_parameters.rapidTravserse()
    recipe_parameters.rapidTraverseEnable()
    rapidTraverseDistance.test_rapid_traverse_distance_40K_Default()
    rapidTraverseDistance.test_rapid_traverse_distance_40K_Max()
    rapidTraverseDistance.test_rapid_traverse_distance_40K_Min()
    rapidTraverseDistance.test_rapid_traverse_distance_40K_Mid()
    rapidTraverseDistance.test_rapid_traverse_distance_40K_max_plus_one()
    rapidTraverseDistance.test_rapid_traverse_distance_40K_min_minus_one()
    
    recipe_parameters.triggerType()
    recipe_parameters.triggerTypeDistanceSelected()
    
    recipe_parameters.perform_scroll_actions()
    
    triggerDistance = TriggerDistance()
    triggerDistance.test_trigger_distance_40K_Default()
    triggerDistance.test_trigger_distance_40K_Max()
    triggerDistance.test_trigger_distance_40K_Min()
    triggerDistance.test_trigger_distance_40K_Mid()
    triggerDistance.test_trigger_distance_40K_max_plus_one()
    triggerDistance.test_trigger_distance_40K_min_minus_one()
    
    
    
    
    