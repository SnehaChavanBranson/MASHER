from helper.core import IsObjectPresent, WaitTillObjectIsLoaded


def WaitTillDashboardIsLoaded():
    WaitTillObjectIsLoaded("")


def CheckIfDashboardIsVisible():
    if IsObjectPresent(""):
        test.passes("")
    else:
        test.fail("")
