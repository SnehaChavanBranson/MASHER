import test
from constants import names
from helper import core

#All the version which are listed on the Information tab about the system
def UI_Controller_Version():
    core.GetValueFromObject(names.systemInformation_0_38_0_0_Text)
    
def SC_Controller_Version():
    core.GetValueFromObject(names.systemInformation_0_38_0_1_Text)

def AC_Controller_Version():
    core.GetValueFromObject(names.systemInformation_0_0_0_1_Text)

def SafetyController_Version():
    core.GetValueFromObject(names.systemInformation_0_0_0_1_Text_2)

def PowerController_Version():
    core.GetValueFromObject(names.systemInformation_0_0_0_0_Text)
    
def Number_of_Alarams():
    core.GetValueFromObject(names.systemInformation_31_Text)

#two buttons in the information tab
def click_SoftwareUpgrade():
    core.ClickButton(names.systemInformation_SOFTWARE_UPGRADE_BransonPrimaryButton)
    
def click_ConfigurationUpgrade():
    core.ClickButton(names.systemInformation_Configuration_Upgrade_BransonPrimaryButton)



















# def information_capturing():
#
#     """UI_Controller_Version, AC_Controller_Version and SC_Controller_Version
#      for capturing the version number and adding it to the reports.
#     """
#     # GetValueFromObject(names.systemInformation_0_38_0_0_Text)
#
#     UI_Controller = names.systemInformation_0_38_0_0_Text
#     UI_Controller_version = waitForObject(UI_Controller).text
#     test.log(f'UI_Controller_version: {UI_Controller_version}')
#
#     AC_Controller = names.systemInformation_0_0_0_1_Text
#     AC_Controller_version = waitForObject(AC_Controller).text
#     test.log(f'AC_Controller_version: {AC_Controller_version}')
#
#     SC_Controller = names.systemInformation_0_38_0_1_Text
#     SC_Controller_version = waitForObject(SC_Controller).text
#     test.log(f'SC_Controller_version: {SC_Controller_version}')
    
    
    