from helper import core
from constants import names
import squish
import time
import test


def NotificationsSkip() -> None:
    core.ClickButton(names.uIController_OK_BransonPrimaryButton)
    core.DoubleClick(names.uIController_OK_BransonPrimaryButton)
    core.ClickButton(names.imageCross_Image)
    try:
        squish.waitForObject(names.imageCross_Image, 2000)
        core.ClickButton(names.imageCross_Image)
        test.xpasses("Found the checkbox")
    except LookupError as err:
        test.xfail("Expectedly failed to find the checkbox", str(err))


def editRecipe() -> None:
    squish.snooze(3)
    core.ClickButton(squish.waitForObject(names.uIController_Rectangle_2))
    squish.snooze(3)
    core.ClickButton(squish.waitForObject(names.uIController_imageLeftMenu_Image))
    squish.snooze(3)
    core.ClickButton(squish.waitForObject(names.uIController_RECIPES_Text))
    squish.snooze(3)
    core.ClickButton(squish.waitForObject(names.recipeSwipeView_Recipe_Ver_2_Text))
    squish.snooze(3)
    core.ClickButton(squish.waitForObject(names.recipeSwipeView_BransonChildButton))


def enterValue(value: float) -> None:
    core.EnterText(names.uIController_input_BransonTextField, value)


def enterValue_int(value: int) -> None:
    core.EnterText(names.uIController_placeholder_PlaceholderText, value)


def CreateNewRecipe() -> None:
    core.ClickButton(squish.waitForObject(names.uIController_imageLeftMenu_Image))
    test.log("clicked on the dashboard")
    squish.snooze(0.2)
    core.ClickButton(squish.waitForObject(names.uIController_menuOptionImage_Image))
    squish.snooze(0.2)
    test.log("Clicked on the recipes of the left panel")
    test.log("trying to enter recipe swipe view")
    squish.snooze(0.2)
    core.ClickButton(names.recipeSwipeView_New_Recipe_Text)
    squish.snooze(0.2)
    test.log("Clicked on the plus sign of recipe creation")


def EnergyTab() -> None:
    squish.snooze(2)
    test.log("Clicked on energy tab")
    core.ClickButton(names.recipeLabWindow_ENERGY_Text)


def EnergyTab_quickedit() -> None:
    test.log("clicking on energy in quick edit")
    core.ClickButton(names.recipeLabWindow_btnRecipeSetting_Rectangle)
    ClearNumberPad()


def TimeTab() -> None:
    test.log("clicked on time tab")
    core.ClickButton(names.recipeLabWindow_TIME_Text)


def TimeTab_quickedit() -> None:
    test.log("clicking on time in quick edit")
    core.ClickButton(names.recipeLabWindow_btnRecipeSetting_Rectangle)
    ClearNumberPad()


def AbsoulteDistanceTab() -> None:
    test.log("entered into absolute distance")
    core.ClickButton(names.recipeLabWindow_ABSOLUTE_DISTANCE_Text)
    test.log("done into absolute distance")


def AbsoulteDistanceTab_quickedit() -> None:
    test.log("clicking on absolute distance in quick edit")
    core.ClickButton(names.recipeLabWindow_btnRecipeSetting_Rectangle)
    ClearNumberPad()


def CollapseDistanceTab() -> None:
    test.log("entered into collapse distance")
    core.ClickButton(names.recipeLabWindow_COLLAPSE_DISTANCE_Text)


def CollapseDistanceTab_quickedit() -> None:
    test.log("clicking on collapse distance in quick edit")
    core.ClickButton(names.recipeLabWindow_btnRecipeSetting_Rectangle)
    ClearNumberPad()


def PeakPowerTab() -> None:
    test.log("Click on peak power")
    core.ClickButton(names.recipeLabWindow_PEAK_POWER_Text)


def PeakPowerTab_quickedit() -> None:
    test.log("clicking on peak power in quick edit")
    core.ClickButton(names.recipeLabWindow_btnRecipeSetting_Rectangle)
    squish.snooze(4)
    ClearNumberPad()


def GroundDetectTab() -> None:
    test.log("Click on Ground Detect")
    core.ClickButton(names.recipeLabWindow_GROUND_DETECT_Text)


def GroundDetectTab_quickedit() -> None:
    test.log("clicking on ground detect in quick edit")
    core.ClickButton(names.recipeLabWindow_btnRecipeSetting_Rectangle)
    ClearNumberPad()


def weld_amplitude_quickedit() -> None:
    test.log("Clicking on the weld amplitude")
    core.ClickButton(names.recipeLabWindow_WELD_AMPLITUDE_Text)
    ClearNumberPad()


def downspeed_quickedit() -> None:
    test.log("Clicking on the downspeed")
    core.ClickButton(names.recipeLabWindow_DOWNSPEED_Text)
    ClearNumberPad()


def weld_pressure_quickedit() -> None:
    test.log("Clicking on the weld pressure")
    core.ClickButton(names.recipeLabWindow_WELD_PRESSURE_Text)
    ClearNumberPad()


def hold_pressure_quickedit() -> None:
    test.log("Clicking on the hold pressure")
    core.ClickButton(names.recipeLabWindow_HOLD_PRESSURE_Text)
    ClearNumberPad()


def trigger_force_quickedit() -> None:
    test.log("Clicking on the trigger force")
    core.ClickButton(names.recipeLabWindow_TRIGGER_FORCE_Text)
    ClearNumberPad()


def hold_time_quickedit() -> None:
    test.log("Clicking on the hold time")
    core.ClickButton(names.recipeLabWindow_HOLD_TIME_Text)
    ClearNumberPad()


def AddParameters() -> None:
    test.log("cross taking back the default number")
    core.ClickButton(names.uIController_BransonFunctionKeyboard)
    test.log("clear the number button")
    core.ClickButton(names.uIController_Clr_BransonDigitalKeyboard)
    test.log("textbox to enter the text")
    squish.snooze(2)
    DoneButton()


def DoneButton() -> None:
    test.log("saving the number")
    core.ClickButton(names.uIController_DONE_BransonPrimaryButton)


def weld_amplitude_DoneButton() -> None:
    test.log("saving the number in weld amplitude")
    core.ClickButton(names.uIController_DONE_BransonPrimaryButton_2)


# def downspeed_DoneButton() -> None:
#     test.log("saving the number in weld amplitude")
#     core.ClickButton(names.uIController_DONE_BransonPrimaryButton)


def ClearNumberPad() -> None:
    test.log("clear the number pad")
    core.ClickButton(names.uIController_Clr_BransonDigitalKeyboard)


def ResetToDefaultButton() -> None:
    test.log("Clicking on the reset default button")
    core.ClickButton(names.recipeLabWindow_RESET_TO_DEFAULT_BransonPrimaryButton)


def verifyInvalidValues() -> None:
    test.log("Clicking on the reset default button")
    core.ClickButton(names.recipeLabWindow_RESET_TO_DEFAULT_BransonPrimaryButton)
