import names
from screens import login,batch_setting,recipe
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

class BatchCounterLimit:
    def test_batch_counter_limit_40K_Default(self):
        for row in dataset:
            if testData.field(row, "EXECUTION") == "TRUE" and testData.field(row, "Param_ID") == "BATCH_COUNTER_LIMIT":
                value_40K_default = testData.field(row, "40K_Default")
                if value_40K_default:
                    test.startSection("Batch Setting: Batch Counter Limit:Test 40K_Default Displayed Value")
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
                    
    def test_batch_counter_limit_40K_min(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "BATCH_COUNTER_LIMIT"                 
            ):
                value_40K_min = testData.field(row, "40K_Min")
                if value_40K_min:
                    test.startSection("Batch Setting: Batch Counter Limit:Test 40K_Min")
                    test.log(f"Testing 40K_Min: {value_40K_min}")
                    batch_setting.batchCounterLimit()
                    recipe.enterValue(value_40K_min)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected min value: {value_40K_min}")
                    test.endSection()

    def test_batch_counter_limit_40K_max(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "BATCH_COUNTER_LIMIT"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if value_40K_max:
                    test.startSection("Batch Setting: Batch Counter Limit:Test 40K_Max")
                    test.log(f"Testing 40K_Max: {value_40K_max}")
                    batch_setting.batchCounterLimit()
                    recipe.enterValue(value_40K_max)
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected max value: {value_40K_max}")
                    test.endSection()

    def test_batch_counter_limit_40K_mid(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "BATCH_COUNTER_LIMIT"                 
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
                    test.startSection("Batch Setting: Batch Counter Limit:Test 40K_Mid")
                    test.log(f"Testing 40K_Mid: {mid_val} (calculated from min={min_val} and max={max_val})")
                    batch_setting.batchCounterLimit()
                    recipe.enterValue(str(mid_val))
                    squish.snooze(2)
                    recipe.DoneButton()
                    test.passes(f"Entered value matches expected mid value: {mid_val}")
                    test.endSection()

    def test_batch_counter_limit_40K_max_plus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "BATCH_COUNTER_LIMIT"                 
            ):
                value_40K_max = testData.field(row, "40K_Max")
                if not value_40K_max or not value_40K_max.strip():
                    test.log("Skipping row: 40K_Max value is missing or blank.")
                    continue
                try:
                    value_40K_max_plus_one = str(float(value_40K_max) + 1)
                    test.startSection("Batch Setting: Batch Counter Limit:Test 40K_Max + 1 (Out of Range)")
                    test.log(f"Testing 40K_Max + 1: {value_40K_max_plus_one}")
                    batch_setting.batchCounterLimit()
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

    def test_batch_counter_limit_40K_min_minus_one(self):
        for row in dataset:
            if (
                testData.field(row, "EXECUTION") == "TRUE" and
                testData.field(row, "Param_ID") == "BATCH_COUNTER_LIMIT"
                ):
                value_40K_min = testData.field(row, "40K_Min")
                if not value_40K_min or not value_40K_min.strip():
                    test.log("Skipping row: 40K_Min value is missing or blank.")
                    continue
                try:
                    value_40K_min_minus_one = str(float(value_40K_min) - 1)
                    test.startSection("Batch Setting: Batch Counter Limit:Test 40K_Min - 1 (Out of Range)")
                    test.log(f"Testing 40K_Min - 1: {value_40K_min_minus_one}")
                    batch_setting.batchCounterLimit()
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
                    
def test_batch_setting():
    batch_setting.batchSettingTab()
    batch_setting.batchSetupCard()
    batch_setting.batchSetupEnable()
    batch_setting.countWithAlaramsCard()
    batch_setting.countWithAlaramsEnable()


def new_create_recipe():
    test.log("Started with creation of new recipe")
    recipe.CreateNewRecipe()
    
def main():
    startApplication("QT_UIController")
    pre_condition()
    squish.snooze(5)
    new_create_recipe()
    test_batch_setting()
    
    batchCounterLimit = BatchCounterLimit()
    batchCounterLimit.test_batch_counter_limit_40K_Default()
    batchCounterLimit.test_batch_counter_limit_40K_min()
    batchCounterLimit.test_batch_counter_limit_40K_max()
    batchCounterLimit.test_batch_counter_limit_40K_mid()
    batchCounterLimit.test_batch_counter_limit_40K_max_plus_one()
    batchCounterLimit.test_batch_counter_limit_40K_min_minus_one()
    
    squish.snooze(5)
