# -*- coding: utf-8 -*-
import squish
from screens import login, dashboard
from helper import core

USERNAME = "ADMIN"
PASSWORD = "Branson@2"
EMPTY_PASSWORD = ""
EMPTY_USERNAME = ""
INCORRECT_USERNAME = "branson"
INCORRECT_PASSWORD = "emerson@1"

def CheckIfALertsbox():
    login.AlertsButtonClick()
        
def test_positive_scenario():
    """
        This testcase is for login positive test case scenario:
        
        Description* Login with the Executive/Admin user with below credentials:
        Username : ADMIN
        Password: Branson@2
    """
    test.startSection("test case 1: positive test scenario with valid credentials")
    snooze(2)
    test.log(f'Step 1: Enter username {USERNAME}')
    login.EnterUsername(USERNAME)
    test.log(f'Step 2: Enter password {PASSWORD}')
    login.EnterPassword(PASSWORD)
    test.log("Step 3: Click on Login button.")
    login.ClickLoginButton()
    dashboard.WaitTillDashboardIsLoaded()
    test.log("Expected Result: Admin user with valid credentials shall get logged in to the system")
    snooze(2)
    test.endSection()
    
def test_password_empty():
    test.startSection("test case 2: password empty")
    snooze(2)
    login.EnterUsername(USERNAME)
    test.log("entered into enter username")
    login.EnterPassword(EMPTY_PASSWORD)
    login.ClickLoginButton()
    login.VerifyPopEmptyPassword()
    login.ClickOkayPopUp()
    snooze(2)
    test.endSection()
    
def test_username_empty():
    test.startSection("test case 3: username empty")
    snooze(2)
    login.EnterUsername(EMPTY_USERNAME)
    test.log("entered empty username.")
    login.EnterPassword(PASSWORD)
    login.ClickLoginButton()
    login.VerifyPopEmptyUsername()
    login.ClickOkayPopUp()
    snooze(2)
    test.endSection()

def test_incorrect_username():
    test.startSection("test case 4: incorrect username")
    snooze(2)
    login.EnterUsername(INCORRECT_USERNAME)
    test.log("entered incorrect username.")
    login.EnterPassword(PASSWORD)
    login.ClickLoginButton()
    login.VerifyInvalidCredsMessage()
    login.ClickOkayPopUp()
    snooze(2)
    test.endSection()

def test_incorrect_password():
    test.startSection("test case 5: incorrect password")
    snooze(2)
    login.EnterUsername(USERNAME)
    test.log("entered incorrect password.")
    login.EnterPassword(INCORRECT_PASSWORD)
    login.ClickLoginButton()
    login.VerifyInvalidCredsMessage()
    login.ClickOkayPopUp()
    snooze(2)
    test.endSection()

def test_incorrect_credentials():
    test.startSection("test case 6: incorrect credentials")
    snooze(2)
    test.log("entered incorrect username and password.")
    login.EnterUsername(INCORRECT_USERNAME)
    login.EnterPassword(INCORRECT_PASSWORD)
    login.ClickLoginButton()
    login.VerifyInvalidCredsMessage()
    login.ClickOkayPopUp()
    snooze(2)
    test.endSection()
    
def main():
    test.log("enter main")
    startApplication("QT_UIController")
    test_username_empty()
    # test_password_empty()
    test_incorrect_username()
    # test_incorrect_password()
    # test_incorrect_credentials()
    test_positive_scenario()
    
    
    
    
    
