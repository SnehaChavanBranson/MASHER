# -*- coding: utf-8 -*-
import names
from screens import login
from helper import core
import test
import squish

def pre_condition():
    test.log("Started with executing Pre Conditions")
    login.startApp()
    test.log("Completed with executing Pre Conditions")

def post_condition():
    test.log("Started with executing Post Conditions")
    login.logout()
    test.log("Completed with executing Post Conditions")

def test_positive_scenario():
    pass

def test_empty_password():
    pass


def main():
    pre_condition()
    moduleName("Login")
    dataset = testData.dataset("login_data.csv")
    test.log("starting the login testcases")
    
    for row in dataset:
        if testData.field(row, "Status") == "TRUE":
            
            test.startSection("testcase")
            username = testData.field(row, "Username")
            login.EnterUsername(username)
            
            squish.snooze(0.5)
            password = testData.field(row, "Password")
            squish.snooze(0.5)
            object_name = testData.field(row, "Object") 
            message = testData.field(row,"Message") 
             
            login.EnterUsername(username)
            test.log(f'entered username "{username}"')
            squish.snooze(0.5)
            login.EnterPassword(password)
            test.log(f'entered password "{password}"')
            squish.snooze(0.5)
            login.ClickLoginButton()
            
            
            if object_name:
                obj = squish.waitForObject(getattr(names,object_name))
                actual_text = str(obj.text)
                test.compare(actual_text, message)
                if object.exists(names.uIController_OK_BransonPrimaryButton):
                    login.ClickOkayPopUp()
            else:
                test.log("no pop up appeared proceeding normally")
            test.endSection()
            
            if object.exists(names.imageCross_Image):
                    core.ClickButton(names.imageCross_Image)
            
    post_condition()
