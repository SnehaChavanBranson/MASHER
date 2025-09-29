# -*- coding: utf-8 -*-
import names
from screens import login
from helper import core
import squish
import test

dataset = testData.dataset("login_data.csv")

def pre_condition():
    test.log("Started with executing Pre Conditions")
    login.startApp()
    test.log("Completed with executing Pre Conditions")

def post_condition():
    test.log("Started with executing Post Conditions")
    login.logout()
    test.log("Completed with executing Post Conditions")

def run_login_test_case(username, password, object_name, expected_message):
    test.log(f'Entered username: "{username}"')
    login.EnterUsername(username)
    squish.snooze(0.5)

    test.log(f'Entered password: "{password}"')
    login.EnterPassword(password)
    squish.snooze(0.5)

    login.ClickLoginButton()
    squish.snooze(0.5)

    if object_name:
        try:
            ui_obj = squish.waitForObject(getattr(names, object_name))
            actual_text = str(ui_obj.text).strip()
            test.log(f"Expected message: {expected_message}")
            test.compare(actual_text, expected_message)
        except LookupError:
            test.fail(f"Could not find object with symbolic name: {object_name}")
        except Exception as e:
            test.fail(f"Error while validating object: {e}")

        # Handle expected popup if there any
        if object.exists(names.uIController_OK_BransonPrimaryButton):
            login.ClickOkayPopUp()
    else:
        test.log("No popup or validation object expected.")

    if object.exists(names.imageCross_Image):
        core.ClickButton(names.imageCross_Image)

def main():
    pre_condition()
    core.moduleName("Login")
    test.log("Starting login test cases")

    for row in dataset:
        if testData.field(row, "Status").strip().upper() == "TRUE":
            username = testData.field(row, "Username")
            password = testData.field(row, "Password")
            object_name = testData.field(row, "Object")
            expected_msg = testData.field(row, "Message")

            test_case_id = f"Login Test - User: {username or 'EMPTY'}, Pass: {'***' if password else 'EMPTY'}"
            test.startSection(test_case_id)
            run_login_test_case(username, password, object_name, expected_msg)
            test.endSection()

    post_condition()
