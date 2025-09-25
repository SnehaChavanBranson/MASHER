import test
import squish
import time
from helper.core import *
from helper import core
from constants import names
import test


def batchSettingTab():
    test.log("Entered batch setting tab")
    ClickButton(names.recipeTabBar_BransonTabButton_5)


def batchSetupCard():
    test.log("Entered batch setup card")
    ClickButton(names.recipeLabWindow_BATCH_SETUP_Text)


def batchSetupEnable():
    test.log("Enable batch setup")
    ClickButton(names.recipeLabWindow_batchSetupEnableSwitch_BransonSwitch)


def countWithAlaramsCard():
    test.log("Click on count with alarams card")
    ClickButton(names.recipeLabWindow_COUNT_WITH_ALARMS_Text)


def countWithAlaramsEnable():
    test.log("Enable count with alarams")
    ClickButton(names.recipeLabWindow_countWithAlarmsEnableSwitch_BransonSwitch)


def batchCounterLimit():
    test.log("Click on count limit card")
    ClickButton(names.recipeLabWindow_Rectangle_2)


def resetBatchCounter():
    test.log("Click on reset batch counter button")
    ClickButton(names.recipeLabWindow_RESET_BATCH_COUNTER_BransonPrimaryButton)


def resetBatchCounterOK():
    test.log("Click on reset batch counter button confirmation yes")
    ClickButton(names.oK_BransonPrimaryButton_2)


def resetBatchCounterCANCEL():
    test.log("Click on reset batch counter button confirmation CANCEL")
    ClickButton(names.cANCEL_BransonPrimaryButton)
