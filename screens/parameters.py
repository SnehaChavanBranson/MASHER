from helper import core
from constants import names
import squish
import test

from helper.helper import scroll_widget


def paramseters_a_z():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab")
    core.ClickButton(squish.waitForObject(names.recipeTabBar_BransonTabButton_3))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab")


def scroll():
    squish.snooze(0.2)
    test.log("Scrolling the Flickable area")
    
    obj = squish.waitForObject(names.recipeLabWindow_infoScrollRec_Flickable)

    # Optional: click the object to focus it
    core.ClickButton(squish.waitForObject(obj))
    
    # Perform 3 scrolls downward with default values
    for _ in range(3):
        squish.mouseWheel(obj, 0, 0, 0, 30, 0)


 
def test_scroll_ui():

    test.log("Scrolling through scrollable UI...")
 
    # Scroll down in a scrollable area

    scroll_widget(names.recipeLabWindow_infoScrollRec_Flickable, delta=-60, repeat=3)
 
    # Scroll up

    scroll_widget(names.recipeLabWindow_infoScrollRec_Flickable, delta=60, repeat=2)
 
    test.passes("Scroll test completed.")

 
def perform_scroll_actions():
    """
    Performs a sequence of mouse wheel scrolls on specific UI elements.
    This function replicates the scroll behavior from the original script.
    """
    test.log("Starting scroll actions...")

    # Scroll on the info scroll area
    flickable = squish.waitForObject(names.recipeLabWindow_infoScrollRec_Flickable)
    squish.mouseWheel(flickable, 1407, 372, 0, -45, 0)
    test.log("Scroll actions completed.")

    
def params_afterBurstcard():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: afterburst card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_AFTERBURST_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: afterburst card")

def params_afterBurstEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: afterburst card enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_afterburstSwitch_BransonSwitch))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: afterburst card enable")

def params_afterBurstDelay():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: afterburst delay enter value")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_AFTERBURST_DELAY_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: afterburst delay enter value")

def params_afterBurstTime():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: afterburst time enter value")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_AFTERBURST_TIME_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: afterburst time enter value")

def params_afterBurstAmplitude():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: afterburst amplitude enter value")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_AFTERBURST_AMPLITUDE_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: afterburst amplitude enter value")
    

def actuatorClear():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator clear card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_ACTUATOR_CLEAR_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator clear card")

def actuatorClearEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator clear card enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_actuatorClearSwitch_BransonSwitch))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator clear card enable")

def actuatorSetting():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_ACTUATOR_SETTING_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card")

def actuatorSettingTimeEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: time radio button enabled")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_settingTime_BransonRadioButton))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: time radio button enabled")

def actuatorTime():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: actuator time card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_ACTUATOR_TIME_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: actuator time card")

def actuatorSettingDistanceEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: distance radio button enabled")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_settingDistance_BransonRadioButton))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: distance radio button enabled")

def actuatorDistance():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: actuator distance card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_ACTUATOR_DISTANCE_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: actuator distance card")
    
def energyBraking():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: energy braking card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_ENERGY_BRAKING_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: energy braking card")

def energyBrakingEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: energy braking enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_energyBrakingSwitch_BransonSwitch))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: energy braking enable")

def energyBrakeTime():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: energy braking time card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_ENERGY_BRAKE_TIME_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: energy time card")

def energyBrakeAmplitude():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: energy braking amplitude")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_ENERGY_BRAKE_AMPLITUDE_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: energy braking amplitude")

def extraCooling():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: extra cooling card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_EXTRA_COOLING_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: extra cooling card")

def extraCoolingEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: extra cooling enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_extraCoolingSwitch_BransonSwitch))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: extra cooling enable")

def maxTimeout():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: max timeout card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_MAX_TIMEOUT_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: max timeout card")

def preWeldSeek():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: pre weld seek card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_PRE_WELD_SEEK_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: pre weld seek card")
    
def preWeldSeekEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: pre weld seek enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_preWeldSeekSwitch_BransonSwitch))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: pre weld seek enable")

def postWeldSeek():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: post weld seek card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_POST_WELD_SEEK_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: post weld seek card")

def postWeldSeekEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: post weld seek enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_postWeldSeekSwitch_BransonSwitch))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: post weld seek enable")

def params_pretrigger():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: pre trigger card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_PRETRIGGER_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: pre trigger card")

def params_pretriggerEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: pre trigger enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_pretriggerEnableSwitch_BransonSwitch))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: pre trigger enable")

def params_pretriggerAmplitude():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: pre trigger amplitude card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_PRETRIGGER_AMPLITUDE_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: pre trigger amplitude card")

def params_pretriggerStart():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: pre trigger start card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_PRETRIGGER_START_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: pre trigger start card")

def params_pretriggerDistanceSelected():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: pre trigger distance radio button selected")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_radioButtonDistance_BransonRadioButton))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: pre trigger distance radio button selected")
    squish.snooze(5)

def params_pretriggerTimeSelected():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: pre trigger time radio button selected")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_radioButtonTime_BransonRadioButton))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: pre trigger time radio button selected")

def params_pretriggerAutoSelected():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: pre trigger auto radio button selected")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_radioButtonAuto_BransonRadioButton))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: pre trigger auto radio button selected")

def params_pretriggerTime():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: pre trigger time card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_PRETRIGGER_TIME_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: pre trigger time card")

def params_pretriggerDistance():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: pre trigger distance card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_PRETRIGGER_DISTANCE_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: pre trigger distance card")

def rapidTravserse():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: rapid traverse card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_RAPID_TRAVERSE_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: rapid traverse card")

def rapidTraverseEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: rapid traverse enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_rapidTraverseSwitch_BransonSwitch))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: rapid traverse enable")

def rapidTraverseDistance():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: rapid traverse distance card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_RAPID_TRAVERSE_DISTANCE_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: rapid traverse distance card")

def triggerLost():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger lost card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_TRIGGER_LOST_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger lost card")

def triggerLostEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger lost enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_triggerLostSwitch_BransonSwitch))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger lost enabled")

def externalAmplitudeSetting():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: external amplitude setting card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_EXTERNAL_AMPLITUDE_SETTING_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: external amplitude setting card")

def externalAmplitudeSettingEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: external amplitude setting enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_extAmpettingSwitch_BransonSwitch))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: external amplitude setting enabled")
  

def triggerType():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger type card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_TRIGGER_TYPE_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger type card")
  

def triggerTypeForceSelected():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger type force radio button selected")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_triggertypeForce_BransonRadioButton))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger type force radio button selected")

def triggerTypeDistanceSelected():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger type distance radio button selected")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_triggertypeDistnce_BransonRadioButton))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger type distance radio button selected")

def triggerDistance():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger type distance card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_TRIGGER_DISTANCE_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger type distance card")

def triggerForce():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger type force card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_TRIGGER_FORCE_Text_2))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: trigger type force card")

def timeSeek():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: time seek enable card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_TIME_SEEK_ENABLE_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: time seek enable card")

def timeSeekEnable():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: time seek enable")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_timeSeekSwitch_BransonSwitch))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: time seek enabled")

def timeSeekPeriod():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: time seek period card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_TIME_SEEK_PERIOD_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: time seek period card")

def scrubAmplitude():
    squish.snooze(0.2)
    test.log("Clicked on the Recipe's Parameters A-Z Tab: actuator Setting card: scrub amplitude card")
    core.ClickButton(squish.waitForObject(names.recipeLabWindow_SCRUB_AMPLITUDE_Text))
    test.log("Finished clicking on the Recipe's Parameters A-Z Tab: actuator Setting card: scrub amplitude card")







    