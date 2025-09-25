from helper import core
from constants import names
import squish
import time
import test

def left_side_panel() -> None:
    core.ClickButton(names.uIController_imageLeftMenu_Image)
    
def SI_MetricButton() -> None:
    core.ClickButton(names.sysConfgGenWindow_SI_Metric_RadioButton)
    # core.ClickButton(names.sysConfgGenWindow_Rectangle)

def SystemNav() -> None:
    test.log("clicked on the system > navigation button inside the system")
    core.ClickButton(names.uIController_SYSTEM_Text)

def ClickOnRecipe() -> None:
    test.log("Clicking on recipe screen from left side panel")
    core.ClickButton(names.uIController_menuImageTextLayout_Rectangle_2)

def CalibrationButton() -> None:
    test.log("clicked on the system > calibration button inside the system")
    core.ClickButton(names.systemWindow_Image_4)

#Configuration
def ConfigurationButton() -> None:
    test.log("clicked on the system > configuration button inside the system")
    core.ClickButton(names.systemWindow_cellIcon_Image_2)
    

def unit_display() -> None:
    test.log("system->configuration-> general (direct screen)")
    core.ClickButton(names.unit_imperial)
    

#Data
def DataButton() -> None:
    test.log("clicked on the system > data button inside the system")
    core.ClickButton(names.systemWindow_Image_2)

#Information
def InformationButton() -> None:
    test.log("clicked on the system > information button inside the system")
    core.ClickButton(names.systemWindow_Image_3)

#Service Count
def ServiceCountButton() -> None:
    test.log("clicked on the system > service count button inside the system")
    core.ClickButton(names.systemWindow_cellIcon_Image)

#Notification
def NotificationButton() -> None:
    core.ClickButton(names.uIController_imageAlarmNotification_Image)

#User Setting
def UserSettingButton() -> None:
    core.ClickButton()

#System tab
def SystemTab() -> None:
    core.ClickButton()

#Save button
def SaveButton() -> None:
    test.log("click on the save button of the system")
    core.ClickButton(squish.waitForObject(names.sysConfgGenWindow_SAVE_BransonPrimaryButton))