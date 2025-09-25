from helper import core
from constants import names
import squish
import test

def stackRecipeTab():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's: Stack Recipe Tab")
    core.ClickButton(squish.waitForObject(names.recipeTabBar_BransonTabButton_4))
    test.log("Finished clicking on the Recipe's: Stack Recipe Tab")

def digitalTune():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's: Stack Recipe Tab: Digital Tune card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_DIGITAL_TUNE_Text))
    test.log("Finished clicking on the Recipe's: Stack Recipe Tab: Digital Tune card")

def endOfWeldStore():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's: Stack Recipe Tab: end of weld store card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_END_OF_WELD_STORE_Text))
    test.log("Finished clicking on the Recipe's: Stack Recipe Tab: end of weld store card")

def endOfWeldStoreEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's: Stack Recipe Tab: end of weld store enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_endOfWeldStoreSwitch_BransonSwitch))
    test.log("Finished clicking on the Recipe's: Stack Recipe Tab: end of weld store enable")

def frequencyOffSet():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's: Stack Recipe Tab: frequency off set card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_FREQUENCY_OFFSET_Text))
    test.log("Finished clicking on the Recipe's: Stack Recipe Tab: frequency off set card")

def frequencyOffSetEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's: Stack Recipe Tab: frequency off set enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_frequencyOffsetSwitch_BransonSwitch))
    test.log("Finished clicking on the Recipe's: Stack Recipe Tab: frequency off set enable")

def internalFreqOffset():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's: Stack Recipe Tab: internal freq offset card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_INTERNAL_FREQ_OFFSET_Text))
    test.log("Finished clicking on the Recipe's: Stack Recipe Tab: internal freq offset card")

def weldRampTime():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's: Stack Recipe Tab: weld ramp time card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_WELD_RAMP_TIME_Text))
    test.log("Finished clicking on the Recipe's: Stack Recipe Tab: weld ramp time card")

def startFrequency():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's: Stack Recipe Tab: start frequency card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_START_FREQUENCY_Text))
    test.log("Finished clicking on the Recipe's: Stack Recipe Tab: start frequency card")

def memoryOffSet():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's: Stack Recipe Tab: memory offset card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_MEMORY_OFFSET_Text))
    test.log("Finished clicking on the Recipe's: Stack Recipe Tab: memory offset card")

def resetToDefault():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's: Stack Recipe Tab: reset to default button")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_RESET_TO_DEFAULT_BransonPrimaryButton))
    test.log("Finished clicking on the Recipe's: Stack Recipe Tab: reset to default card")

def clearMemory():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's: Stack Recipe Tab: clear memory button")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_CLEAR_MEMORY_BransonPrimaryButton))
    test.log("Finished clicking on the Recipe's: Stack Recipe Tab: clear memory button")


