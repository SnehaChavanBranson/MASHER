from helper.core import IsObjectPresent, WaitTillObjectIsLoaded
import squish
from constants import names
import test

def WaitTillDashboardIsLoaded():
    WaitTillObjectIsLoaded("")
    IsObjectPresent(squish.waitForObject(names.productionWindowItem_Item))
    test.passes("Logged in successfully")
    test.log("Dashboard is visible")


def CheckIfDashboardIsVisible():
    if IsObjectPresent(""):
        test.passes("")
    else:
        test.fail("")