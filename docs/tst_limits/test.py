import names
from screens import login, recipe, limits
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
    
def test_limits():
    limits.limitsTab()
    squish.snooze(2)
    limits.globalSuspectEnable()
    squish.snooze(2)
    limits.globalRejectEnable()
    squish.snooze(2)
    limits.timeTabEnterValue()

def test_limits_control():
    limits.limitsTab()
    squish.snooze(3)
    limits.controlTab()
    squish.snooze(2)
    limits.controlEnable()
    squish.snooze(2)
    
def main():
    test.log("Enters into main function of weld process")
    
    startApplication("QT_UIController")
    squish.snooze(7)
    pre_condition()
    # reset_notification()
    new_create_recipe()
    squish.snooze(3)
    test_limits()

