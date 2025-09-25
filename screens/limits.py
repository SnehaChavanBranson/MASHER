from helper import core
from constants import names
import squish
import time
import test

    # mouseClick(waitForObject(names.recipeTabBar_BransonTabButton_2), 21, 7, Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)
    # squish.snooze(3)
    # mouseClick(waitForObject(names.subrecipeTabBar_BransonTabButton_2), 112, 25, Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)
    # squish.snooze(3)
    # mouseClick(waitForObject(names.recipeLabWindow_GLOBAL_SUSPECT_Text), Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)
    # squish.snooze(3)
    # mouseClick(waitForObject(names.recipeLabWindow_GLOBAL_SUSPECT_Text), Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)
    # squish.snooze(3)
    # mouseClick(waitForObject(names.recipeLabWindow_switchControl_BransonSwitch), 33, 4, Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)
    # squish.snooze(3)
    # mouseClick(waitForObject(names.recipeLabWindow_GLOBAL_REJECT_Text), Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)
    # squish.snooze(3)
    # mouseClick(waitForObject(names.recipeLabWindow_switchControl_BransonSwitch_2), 26, 6, Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)
    # squish.snooze(3)

    # mouseClick(waitForObject(names.recipeLabWindow_TIME_Text), Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)
    # squish.snooze(3)
    # mouseClick(waitForObject(names.uIController_suspectSwitchBtn_BransonSwitch), 33, 2, Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)
    # squish.snooze(3)
    # mouseClick(waitForObject(names.uIController_rejectSwitchBtn_BransonSwitch), 36, 8, Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)
    # squish.snooze(3)
    # mouseClick(waitForObject(names.uIController_input_TextField), 46, 16, Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)
    # squish.snooze(3)
    # mouseClick(waitForObject(names.uIController_input_TextField), 46, 16, Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)
    # squish.snooze(3)
    # type(waitForObject(names.uIController_input_TextField), "<Backspace>")
    # type(waitForObject(names.uIController_input_TextField), "<NumPad0>")
    # type(waitForObject(names.uIController_input_TextField), "<NumPad.>")
    # type(waitForObject(names.uIController_input_TextField), "<NumPad0>")
    # type(waitForObject(names.uIController_input_TextField), "<NumPad1>")
    # type(waitForObject(names.uIController_input_TextField), "<NumPad1>")
    # mouseClick(waitForObject(names.uIController_DONE_BransonPrimaryButton), 40, 12, Qt.ShiftModifier + Qt.AltModifier, Qt.LeftButton)

def limitsTab():
    test.log("Clicking on the weld limits tab")
    core.ClickButton(squish.waitForObject(names.recipeTabBar_BransonTabButton_2))

def suspectandRejectTab():
    test.log("Clicking on the weld limit: suspect & reject tab: Enable Suspect")
    squish.snooze(3)
    core.ClickButton(squish.waitForObject(names.subrecipeTabBar_BransonTabButton_2))


def globalSuspectEnable():
    test.log("Clicking on the weld limit: suspect & reject tab: Enable suspect")
    squish.snooze(3)
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_switchControl_BransonSwitch))

def globalRejectEnable():
    test.log("Clicking on the weld limit: suspect & reject tab: Enable global Suspect")
    squish.snooze(3)
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_switchControl_BransonSwitch_2))


def timeTabEnterValue():
    squish.snooze(3)
    test.log("got into time tab")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_TIME_Text))
    test.log("enabling suspect for time tab")
    squish.snooze(3)
    core.ClickButton(squish.waitForObject(names.uIController_suspectSwitchBtn_BransonSwitch))
    squish.snooze(3)
    core.ClickButton(squish.waitForObject(names.uIController_rejectSwitchBtn_BransonSwitch))
    test.log("enabling reject for time tab")
    # squish.snooze(3)
    # core.ClickButton(squish.waitForObject(names.uIController_input_TextField))
    # test.log("entered value")
    # core.ClickButton(squish.waitForObject(names.uIController_input_TextField))
    


def energyTabEnterValue():
    test.log("enabling suspect for energy tab")
    enableSuspect()
    test.log("enabling reject for energy tab")
    enableReject()
    test.log("clicking on energy tab")
    squish.snooze(2)
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_ENERGY_Text_2))
    
def peakPowerTabEnterValue():
    pass

def absoluteDistanceTabEnterValue():
    pass

def collapseDistanceTabEnterValue():
    pass

def endWeldForceTabEnterValue():
    pass

def triggerDistabceTabEnterValue():
    pass

def velocityTabEnterValue():
    pass

def frequencyTabEnterValue():
    pass

def controlTab():
    test.log("Clicking on the weld limit: switch to second tab control tab")
    squish.snooze(3)
    core.ClickButton(squish.waitForObject(names.subrecipeTabBar_BransonTabButton))

def controlEnable():
    test.log("Clicking on the weld limit: switch to second tab control tab enable control")
    squish.snooze(3)
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_controlSwitch_BransonSwitch))

def frequencyLowCutOffEnterValue():
    pass

def peakPowerCutOffEnterValue():
    pass

def frequencyHighCutOffEnterValue():
    pass

def energyCutOff():
    pass

def groundDetectCutOffEnterValue():
    pass

def timeCutOffEnterValue():
    pass

def absoluteDistanceCutOffEnterValue():
    pass

def collapseDistanceCutOffEnterValue():
    pass

def energyCompensationTabEnterValue():
    pass

def energyCompensationTab():
    pass

def energyCompensationTabEnable():
    pass

def energyCompensationMinimumValueEnterValue():
    pass

def energyCompensationMaximumValueEnterValue():
    passrecipeLabWindow_TIME_Text

# #limits tab
#
# recipeTabBar_BransonTabButton = {"checkable": True, "container": recipeLabWindow_recipeTabBar_TabBar, "occurrence": 4, "type": "BransonTabButton", "unnamed": 1, "visible": True}
#
# #suspect&reject tab
# subrecipeTabBar_BransonTabButton_2 = {"checkable": True, "container": recipeLabWindow_subrecipeTabBar_TabBar, "type": "BransonTabButton", "unnamed": 1, "visible": True}
#
# #control tab
# subrecipeTabBar_BransonTabButton = {"checkable": True, "container": recipeLabWindow_subrecipeTabBar_TabBar, "occurrence": 2, "type": "BransonTabButton", "unnamed": 1, "visible": True}
#
# #energy compensation
# subrecipeTabBar_BransonTabButton_3 = {"checkable": True, "container": recipeLabWindow_subrecipeTabBar_TabBar, "occurrence": 3, "type": "BransonTabButton", "unnamed": 1, "visible": True}
#
# #inside suspect & reject parameters
#
# #time tab
# recipeLabWindow_TIME_Text = {"container": uIController_recipeLabWindow_Item, "occurrence": 2, "text": "TIME", "type": "Text", "unnamed": 1, "visible": True}
#
# #energy tab
# recipeLabWindow_ENERGY_Text_2 = {"container": uIController_recipeLabWindow_Item, "text": "ENERGY", "type": "Text", "unnamed": 1, "visible": True}
#
# #peak power
# recipeLabWindow_PEAK_POWER_Text = {"container": uIController_recipeLabWindow_Item, "text": "PEAK POWER", "type": "Text", "unnamed": 1, "visible": True}
#
# #absolute distance
# recipeLabWindow_ABSOLUTE_DISTANCE_Text = {"container": uIController_recipeLabWindow_Item, "text": "ABSOLUTE DISTANCE", "type": "Text", "unnamed": 1, "visible": True}
#
# #collapse distance
# recipeLabWindow_COLLAPSE_DISTANCE_Text = {"container": uIController_recipeLabWindow_Item, "text": "COLLAPSE DISTANCE", "type": "Text", "unnamed": 1, "visible": True}
#
# #end weld force
# recipeLabWindow_END_WELD_FORCE_Text = {"container": uIController_recipeLabWindow_Item, "text": "END WELD FORCE", "type": "Text", "unnamed": 1, "visible": True}
#
# #trigger distance
# recipeLabWindow_TRIGGER_DISTANCE_Text = {"container": uIController_recipeLabWindow_Item, "text": "TRIGGER DISTANCE", "type": "Text", "unnamed": 1, "visible": True}
#
# #velocity
# recipeLabWindow_VELOCITY_Text = {"container": uIController_recipeLabWindow_Item, "text": "VELOCITY", "type": "Text", "unnamed": 1, "visible": True}
#
# #frequency
# recipeLabWindow_FREQUENCY_Text = {"container": uIController_recipeLabWindow_Item, "text": "FREQUENCY", "type": "Text", "unnamed": 1, "visible": True}
#
# #done
# uIController_DONE_BransonPrimaryButton = {"checkable": False, "container": uIController_QQuickWindowQmlImpl, "id": "done", "text": "DONE", "type": "BransonPrimaryButton", "unnamed": 1, "visible": True}
#
# #clear
# uIController_Clr_BransonDigitalKeyboard = {"checkable": False, "container": uIController_QQuickWindowQmlImpl, "id": "customButton", "text": "Clr", "type": "BransonDigitalKeyboard", "unnamed": 1, "visible": True}
#
# #cross
# uIController_headercls_Image = {"container": uIController_QQuickWindowQmlImpl, "id": "headercls", "source": "qrc:/Images/crossMark.svg", "type": "Image", "unnamed": 1, "visible": True}
#
# #global suspect enable
# recipeLabWindow_switchControl_BransonSwitch = {"checkable": True, "container": uIController_recipeLabWindow_Item, "id": "switchControl", "type": "BransonSwitch", "unnamed": 1, "visible": True}
#
# #global reject enable
# recipeLabWindow_switchControl_BransonSwitch_2 = {"checkable": True, "container": uIController_recipeLabWindow_Item, "id": "switchControl", "occurrence": 2, "type": "BransonSwitch", "unnamed": 1, "visible": True}
#
# #control tab
# #control tab control enable
# recipeLabWindow_energyEnableSwitch_BransonSwitch = {"checkable": True, "container": uIController_recipeLabWindow_Item, "id": "energyEnableSwitch", "type": "BransonSwitch", "unnamed": 1, "visible": True}
#
# recipeLabWindow_controlSwitch_BrecipeLabWindow_switchControl_BransonSwitchransonSwitch = {"checkable": True, "container": uIController_recipeLabWindow_Item, "id": "controlSwitch", "type": "BransonSwitch", "unnamed": 1, "visible": True}
#
# #frequency low cut off
# recipeLabWindow_FREQUENCY_LOW_CUTOFF_Text = {"container": uIController_recipeLabWindow_Item, "text": "FREQUENCY LOW CUTOFF", "type": "Text", "unnamed": 1, "visible": True}
#
# #peak power cut off
# recipeLabWindow_PEAK_POWER_CUTOFF_Text = {"container": uIController_recipeLabWindow_Item, "text": "PEAK POWER CUTOFF", "type": "Text", "unnamed": 1, "visible": True}
#
# #frequency high cut off
# recipeLabWindow_FREQUENCY_HIGH_CUTOFF_Text = {"container": uIController_recipeLabWindow_Item, "text": "PEAK POWER CUTOFF", "type": "Text", "unnamed": 1, "visible": True}
#
# #energy cut off
# recipeLabWindow_ENERGY_CUTOFF_Text = {"container": uIController_recipeLabWindow_Item, "text": "ENERGY CUTOFF", "type": "Text", "unnamed": 1, "visible": True}
#
# #ground detect cut off
# recipeLabWindow_GROUND_DETECT_CUTOFF_Text = {"container": uIController_recipeLabWindow_Item, "text": "GROUND DETECT CUTOFF", "type": "Text", "unnamed": 1, "visible": True}
#
# #time cut off
# recipeLabWindow_TIME_CUTOFF_Text = {"container": uIController_recipeLabWindow_Item, "text": "TIME CUTOFF", "type": "Text", "unnamed": 1, "visible": True}
#
# #absolute distance cut off
# recipeLabWindow_ABSOLUTE_DISTANCE_CUTOFF_Text = {"container": uIController_recipeLabWindow_Item, "text": "ABSOLUTE DISTANCE CUTOFF", "type": "Text", "unnamed": 1, "visible": True}
#
# #collapse distance cut off
# recipeLabWindow_COLLAPSE_DISTANCE_CUTOFF_Text = {"container": uIController_recipeLabWindow_Item, "text": "COLLAPSE DISTANCE CUTOFF", "type": "Text", "unnamed": 1, "visible": True}
#
# #energy compensation tab inside params
# recipeLabWindow_energyEnableSwitch_BransonSwitch = {"checkable": True, "container": uIController_recipeLabWindow_Item, "id": "energyEnableSwitch", "type": "BransonSwitch", "unnamed": 1, "visible": True}
#
# #ENERGY COMPENSATION MINIMUM VALUE
# recipeLabWindow_ENERGY_COMPENSATION_MINIMUM_VALUE_Text = {"container": uIController_recipeLabWindow_Item, "text": "ENERGY COMPENSATION MINIMUM VALUE", "type": "Text", "unnamed": 1, "visible": True}
#
# #ENERGY COMPENSATION MAXIMUM VALUE
# recipeLabWindow_ENERGY_COMPENSATION_MAXIMUM_VALUE_Text = {"container": uIController_recipeLabWindow_Item, "text": "ENERGY COMPENSATION MAXIMUM VALUE", "type": "Text", "unnamed": 1, "visible": True}
#
# #global Suspect enable
# recipeLabWindow_switchControl_BransonSwitch = {"checkable": True, "container": uIController_recipeLabWindow_Item, "id": "switchControl", "type": "BransonSwitch", "unnamed": 1, "visible": True}
#
# #global reject enable
# recipeLabWindow_switchControl_BransonSwitch_2 = {"checkable": True, "container": uIController_recipeLabWindow_Item, "id": "switchControl", "occurrence": 2, "type": "BransonSwitch", "unnamed": 1, "visible": True}
#
# #enable suspect inside the parameters
# uIController_suspectSwitchBtn_BransonSwitch = {"checkable": True, "container": uIController_QQuickWindowQmlImpl, "id": "suspectSwitchBtn", "type": "BransonSwitch", "unnamed": 1, "visible": True}
#
# #enable reject inside the parameters
# uIController_rejectSwitchBtn_BransonSwitch = {"checkable": True, "container": uIController_QQuickWindowQmlImpl, "id": "rejectSwitchBtn", "type": "BransonSwitch", "unnamed": 1, "visible": True}
#
#
#
#


