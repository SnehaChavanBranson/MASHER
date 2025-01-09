""" Object repository for login to host all the UI objects in this file."""


LOGIN_PAGE_OBJECTS = {
    "Area": {
        "container": "Core.MainWindow",
        "id": "loginFlick",
        "type": "Flickable",
        "unnamed": 1,
        "visible": True
    },
    "UsernameInput": {
        "backgroundcolor": "#ffffff",
        "container": "Area",
        "echoMode": 0,
        "id": "textFildUserName",
        "type": "TextField",
        "unnamed": 1,
        "visible": True
    },
    "PasswordInput": {
        "backgroundcolor": "#ffffff",
        "container": "Area",
        "echoMode": 2,
        "id": "textFildPassword",
        "passwordCharacter": "*",
        "type": "TextField",
        "unnamed": 1,
        "visible": True
    },
    "Button": {
        "checkable": False,
        "container": "Area",
        "id": "loginButton",
        "type": "Button",
        "unnamed": 1,
        "visible": True
    }
}


recipes = {
    "NumpadInputField": {
        "backgroundcolor": "#ffffff",
        "container": "Core.MainWindow",
        "echoMode": 0,
        "id": "input",
        "type": "BransonTextField",
        "unnamed": 1,
        "visible": True
    },
    "NumpadDoneButton": {
        "checkable": False,
        "container": "Core.MainWindow",
        "id": "done",
        "text": "DONE",
        "type": "BransonPrimaryButton",
        "unnamed": 1,
        "visible": True
    },
    "NumpadCancelButton": {
        "checkable": False,
        "container": "Core.MainWindow",
        "id": "cancel",
        "text": "CANCEL",
        "type": "BransonPrimaryButton",
        "unnamed": 1,
        "visible": True
    },
    "NumpadDoneButton_Stepping": {
        "checkable": False,
        "container": "Core.MainWindow",
        "id": "btnDone",
        "text": "DONE",
        "type": "BransonPrimaryButton",
        "unnamed": 1,
        "visible": True
    },
    "NumpadCancelButton_Stepping": {
        "checkable": False,
        "container": "Core.MainWindow",
        "id": "btnCancel",
        "text": "CANCEL",
        "type": "BransonPrimaryButton",
        "unnamed": 1,
        "visible": True
    },
    "ControlText": {
        "container": "Recipe.EditWindow",
        "text": "CONTROL",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "ControlTurnSettingsOffText": {
        "container": "Recipe.EditWindow",
        "text": "Turn Settings OFF",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "ControlGridView": {
        "container": "Recipe.EditWindow",
        "id": "recipeControlGridView",
        "type": "BransonGridView",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "pretriggerEnableTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "Pretrigger Text": {
        "container": "Recipe.EditWindow",
        "text": "PRETRIGGER",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerToggleSwitch": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "pretriggerEnableSwitch",
        "type": "BransonSwitch",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIcon",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerAmplitudeInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "pretriggerAmplitudeTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerAmplitudeText": {
        "container": "Recipe.EditWindow",
        "text": "PRETRIGGER AMPLITUDE",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerAmplitudeClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickPretriggerAmplitude",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerDistanceInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "pretriggerDistanceTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerDistanceText": {
        "container": "Recipe.EditWindow",
        "text": "PRETRIGGER DISTANCE",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerDistanceClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickPretriggerDistance",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerTimeInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "pretriggerTimeTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerTimeText": {
        "container": "Recipe.EditWindow",
        "text": "PRETRIGGER TIME",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerTimeClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickPretriggerTime",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerStartInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "pretriggerType",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerStartText": {
        "container": "Recipe.EditWindow",
        "text": "PRETRIGGER START",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerStartTimeRadioButton": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "radioButtonTime",
        "type": "BransonRadioButton",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerStartAutoRadioButton": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "radioButtonAuto",
        "type": "BransonRadioButton",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerStartDistanceRadioButton": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "radioButtonDistance",
        "type": "BransonRadioButton",
        "unnamed": 1,
        "visible": True
    },
    "AfterburstInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "afterburstEnableTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "AfterburstText": {
        "container": "Recipe.EditWindow",
        "text": "AFTERBURST",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "AfterburstToggleSwitch": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "afterburstSwitch",
        "type": "BransonSwitch",
        "unnamed": 1,
        "visible": True
    },
    "AfterburstInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIcon",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "AfterburstDelayInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "afterburstDelayTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "AfterburstDelayText": {
        "container": "Recipe.EditWindow",
        "text": "AFTERBURST DELAY",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "AfterburstDelayClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickAfterburstDelay",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "AfterburstTimeInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "afterburstTimeTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "AfterburstTimeText": {
        "container": "Recipe.EditWindow",
        "text": "AFTERBURST TIME",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "AfterburstTimeClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickAfterburstTime",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "AfterburstAmplitudeInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "afterburstAmplitudeTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "AfterburstAmplitudeText": {
        "container": "Recipe.EditWindow",
        "text": "AFTERBURST AMPLITUDE",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "AfterburstAmplitudeClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickAfterburstAmplitude",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "QuickEditRectangle": {
        "container": "Recipe.EditWindow",
        "id": "rectQuickEdit",
        "type": "Rectangle",
        "unnamed": 1,
        "visible": True
    },
    "DigitalTuneInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "digitalTuneTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "DigitalTuneText": {
        "container": "Recipe.EditWindow",
        "text": "DIGITAL TUNE",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "DigitalTuneClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickDigitalTune",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "DigitalTuneInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIcon",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "EndOfWeldStoreInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "endOfWeldStoreTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "EndOfWeldStoreText": {
        "container": "Recipe.EditWindow",
        "text": "END OF WELD STORE",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "EndOfWeldStoreToggleSwitch": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "endOfWeldStoreSwitch",
        "type": "BransonSwitch",
        "unnamed": 1,
        "visible": True
    },
    "EndOfWeldStoreClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickEndOfWeldStore",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "EndOfWeldStoreInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "endOfWeldStoreTitleinfoIcon",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "FrequencyOffsetInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "frequencyOffsetTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "FrequencyOffsetText": {
        "container": "Recipe.EditWindow",
        "text": "FREQUENCY OFFSET",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "FrequencyOffsetToggleSwitch": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "frequencyOffsetSwitch",
        "type": "BransonSwitch",
        "unnamed": 1,
        "visible": True
    },
    "FrequencyOffsetClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickFrequencyOffset",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "FrequencyOffsetInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "frequencyOffsetTitleinfoicon",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "InternalFrequencyOffsetInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "internalFreqOffsetTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "InternalFrequencyOffsetText": {
        "container": "Recipe.EditWindow",
        "text": "INTERNAL FREQ OFFSET",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "InternalFrequencyOffsetClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickInternalFreqOffset",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "InternalFrequencyOffsetInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "internalFreqOffsetTitleinfoicon",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "EnergyBrakingInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "energyBrakingEnableTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "EnergyBrakingText": {
        "container": "Recipe.EditWindow",
        "text": "ENERGY BRAKING",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "EnergyBrakingClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickEnergyBraking",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "EnergyBrakingToggleSwitch": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "energyBrakingSwitch",
        "type": "BransonSwitch",
        "unnamed": 1,
        "visible": True
    },
    "EnergyBrakingInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIconEnergyBraking",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "EnergyBrakeTimeInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "energyBrakeTimeTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "EnergyBrakeTimeText": {
        "container": "Recipe.EditWindow",
        "text": "ENERGY BRAKE TIME",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "EnergyBrakeTimeClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickEnergyBrakeTime",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "EnergyBrakeTimeInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIconEnergyBrakeTime",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "EnergyBrakeAmplitudeInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "energyBrakeAmplitudeTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "EnergyBrakeAmplitudeText": {
        "container": "Recipe.EditWindow",
        "text": "ENERGY BRAKE AMPLITUDE",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "EnergyBrakeAmplitudeClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickEnergyBrakeAmplitude",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "EnergyBrakeAmplitudeInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIconEnergyBrakeAmplitude",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "ExtraCoolingInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "extraCoolingEnableTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "ExtraCoolingText": {
        "container": "Recipe.EditWindow",
        "text": "EXTRA COOLING",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "ExtraCoolingToggleSwitch": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "extraCoolingSwitch",
        "type": "BransonSwitch",
        "unnamed": 1,
        "visible": True
    },
    "ExtraCoolingClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickExtraCooling",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "ExtraCoolingInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIconExtraCooling",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "MaxTimeoutInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "maxTimeoutEnableTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "MaxTimeoutText": {
        "container": "Recipe.EditWindow",
        "text": "MAX TIMEOUT",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "MaxTimeoutClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickMaxTimeout",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "MaxTimeoutInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIconMaxTimeout",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "HoldForceRampInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "holdForceRampTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": False
    },
    "HoldForceRampText": {
        "container": "Recipe.EditWindow",
        "text": "HOLD FORCE RAMP",
        "type": "Text",
        "unnamed": 1,
        "visible": False
    },
    "HoldForceRampClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickHoldForceRamp",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": False
    },
    "HoldForceRampInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIconHoldForceRamp",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": False
    },
    "PreWeldSeekInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "preWeldSeekTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "PreWeldSeekText": {
        "container": "Recipe.EditWindow",
        "text": "PRE WELD SEEK",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "PreWeldSeekToggleSwitch": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "preWeldSeekSwitch",
        "type": "BransonSwitch",
        "unnamed": 1,
        "visible": True
    },
    "PreWeldSeekClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickPreWeldSeek",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "PreWeldSeekInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIconPreWeldSeek",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "ActuatorClearInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "actuatorClearEnableTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "ActuatorClearText": {
        "container": "Recipe.EditWindow",
        "text": "ACTUATOR CLEAR",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "ActuatorClearToggleSwitch": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "actuatorClearSwitch",
        "type": "BransonSwitch",
        "unnamed": 1,
        "visible": True
    },
    "ActuatorClearClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickActuatorClear",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": True
    },
    "ActuatorClearInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIconActuatorClear",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "SettingInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "setting",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "SettingText": {
        "container": "Recipe.EditWindow",
        "text": "SETTING",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "SettingDistanceRadioButton": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "settingDistance",
        "type": "BransonRadioButton",
        "unnamed": 1,
        "visible": True
    },
    "SettingTimeRadioButton": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "settingTime",
        "type": "BransonRadioButton",
        "unnamed": 1,
        "visible": True
    },
    "SettingInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIconSetting",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "RapidTraverseInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "rapidTraverseEnableTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": False
    },
    "RapidTraverseText": {
        "container": "Recipe.EditWindow",
        "text": "RAPID TRAVERSE",
        "type": "Text",
        "unnamed": 1,
        "visible": False
    },
    "RapidTraverseToggleSwitch": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "rapidTraverseSwitch",
        "type": "BransonSwitch",
        "unnamed": 1,
        "visible": False
    },
    "RapidTraverseClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickRapidTraverse",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": False
    },
    "RapidTraverseInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIconTrapidTraverse",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": False
    },
    "RapidTraverseDistanceInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "rapidTraverseDistanceTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": False
    },
    "RapidTraverseDistanceText": {
        "container": "Recipe.EditWindow",
        "text": "RAPID TRAVERSE DISTANCE",
        "type": "Text",
        "unnamed": 1,
        "visible": False
    },
    "RapidTraverseDistanceClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickRapidTraverseDistance",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": False
    },
    "RapidTraverseDistanceInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIconRapidTraverseDistance",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": False
    },
    "TriggerLostInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "triggerLostEnableTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": False
    },
    "TriggerLostText": {
        "container": "Recipe.EditWindow",
        "text": "TRIGGER LOST",
        "type": "Text",
        "unnamed": 1,
        "visible": False
    },
    "TriggerLostToggleSwitch": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "triggerLostSwitch",
        "type": "BransonSwitch",
        "unnamed": 1,
        "visible": False
    },
    "TriggerLostClickMouseArea": {
        "container": "Recipe.EditWindow",
        "id": "clickTriggerLost",
        "type": "MouseArea",
        "unnamed": 1,
        "visible": False
    },
    "TriggerLostInfoButton": {
        "container": "Recipe.EditWindow",
        "id": "infoIconTriggerLost",
        "source": "qrc:/Images/info.png",
        "type": "Image",
        "unnamed": 1,
        "visible": False
    },
    "GlobalSuspectInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "globalsuspectEnableTitle",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "GlobalSuspectText": {
        "container": "Recipe.EditWindow",
        "text": "GLOBAL SUSPECT",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "GlobalSuspectToggleSwitch": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "globalsuspectEnableSwitch",
        "type": "BransonSwitch",
        "unnamed": 1,
        "visible": True
    },
    "ControlInputRectangle": {
        "container": "Recipe.EditWindow",
        "id": "switchControlRec",
        "type": "BransonLeftBorderRectangle",
        "unnamed": 1,
        "visible": True
    },
    "ControlTurnSettingsOnText": {
        "container": "Recipe.EditWindow",
        "text": "Turn Settings ON",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "ControlToggleSwitch": {
        "checkable": True,
        "container": "Recipe.EditWindow",
        "id": "controlSwitch",
        "type": "BransonSwitch",
        "unnamed": 1,
        "visible": True
    },
    "CardWindow": {
        "container": "Core.MainWindow",
        "id": "recipeCardWindowItem",
        "type": "Item",
        "unnamed": 1,
        "visible": True
    },
    "SwipeView": {
        "container": "CardWindow",
        "id": "recipeSwipeView",
        "type": "SwipeView",
        "unnamed": 1,
        "visible": True
    },
    "CreateImage_RecipeScreen": {
        "container": "SwipeView",
        "id": "creatingImage",
        "source": "qrc:/Images/Add.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "CreateText": {
        "container": "SwipeView",
        "text": "New Recipe",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "WarningPopUpWindow": {
        "container": "CardWindow",
        "id": "popupBackground",
        "type": "Rectangle",
        "unnamed": 1,
        "visible": True
    },
    "WarningOkButton": {
        "checkable": False,
        "container": "CardWindow",
        "id": "ok",
        "text": "OK",
        "type": "BransonPrimaryButton",
        "unnamed": 1,
        "visible": True
    },
    "WarningCancelButton": {
        "checkable": False,
        "container": "CardWindow",
        "id": "cancel",
        "text": "Cancel",
        "type": "BransonPrimaryButton",
        "unnamed": 1,
        "visible": True
    },
    "EditWindow": {
        "container": "Core.MainWindow",
        "id": "recipeLabWindow",
        "type": "Item",
        "unnamed": 1,
        "visible": True
    },
    "TopBar": {
        "container": "Core.MainWindow",
        "id": "backGround",
        "type": "Rectangle",
        "unnamed": 1,
        "visible": True
    },
    "SaveImage": {
        "container": "EditWindow",
        "id": "saveRecipeIcon",
        "source": "qrc:/Images/Save.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "CreateImage_RecipeEditScreen": {
        "container": "EditWindow",
        "id": "createRecipeIcon",
        "source": "qrc:/Images/AddFolder.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "CopyImage_RecipeEditScreen": {
        "container": "EditWindow",
        "id": "copyRecipeIcon",
        "source": "qrc:/Images/Copy.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "ResetToDefaultButton": {
        "checkable": False,
        "container": "EditWindow",
        "id": "btnResetDefaults",
        "text": "RESET TO DEFAULT",
        "type": "BransonPrimaryButton",
        "unnamed": 1,
        "visible": True
    },
    "DeleteImage_RecipeScreen": {
        "container": "SwipeView",
        "id": "deleteIcon",
        "source": "qrc:/Images/Trash.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "CopyImage_RecipeScreen": {
        "container": "SwipeView",
        "id": "copyIcon",
        "source": "qrc:/Images/Copy.png",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "EditTabsBar": {
        "container": "EditWindow",
        "id": "recipeTabBar",
        "type": "TabBar",
        "unnamed": 1,
        "visible": True
    },
    "WeldModeTabButton": {
        "checkable": True,
        "container": "EditTabsBar",
        "type": "BransonTabButton",
        "unnamed": 1,
        "visible": True,
        "tabbtnText": "Weld Mode"
    },
    "WeldProcessTabButton": {
        "checkable": True,
        "container": "EditTabsBar",
        "type": "BransonTabButton",
        "unnamed": 1,
        "visible": True,
        "tabbtnText": "Weld Process"
    },
    "ParameterAZTabButton": {
        "checkable": True,
        "container": "EditTabsBar",
        "type": "BransonTabButton",
        "unnamed": 1,
        "visible": True,
        "tabbtnText": "Parameters A-Z"
    },
    "LimitsTabButton": {
        "checkable": True,
        "container": "EditTabsBar",
        "type": "BransonTabButton",
        "unnamed": 1,
        "visible": True,
        "tabbtnText": "Limits"
    },
    "StackRecipeTabButton": {
        "checkable": True,
        "container": "EditTabsBar",
        "type": "BransonTabButton",
        "unnamed": 1,
        "visible": True,
        "tabbtnText": "Stack Recipe"
    },
    "EditSubTabsBar": {
        "container": "EditWindow",
        "id": "subrecipeTabBar",
        "type": "TabBar",
        "unnamed": 1,
        "visible": True
    },
    "PretriggerTabButton": {
        "checkable": True,
        "container": "EditSubTabsBar",
        "type": "BransonTabButton",
        "unnamed": 1,
        "visible": True,
        "tabbtnText": "Pretrigger"
    },
    "AfterburstTabButton": {
        "checkable": True,
        "container": "EditSubTabsBar",
        "type": "BransonTabButton",
        "unnamed": 1,
        "visible": True,
        "tabbtnText": "Afterburst"
    },
    "SuspectTabButton": {
        "checkable": True,
        "container": "EditSubTabsBar",
        "type": "BransonTabButton",
        "unnamed": 1,
        "visible": True,
        "tabbtnText": "Suspect"
    },
    "ControlTabButton": {
        "checkable": True,
        "container": "EditSubTabsBar",
        "type": "BransonTabButton",
        "unnamed": 1,
        "visible": True,
        "tabbtnText": "Control"
    },
    "WarningOverlay": {
        "container": "Core.MainWindow",
        "type": "Overlay",
        "unnamed": 1,
        "visible": True
    },
    "WarningRectangle": {
        "container": "WarningOverlay",
        "id": "root",
        "type": "Rectangle",
        "unnamed": 1,
        "visible": True
    },
    "WarningOverlay1": {
        "container": "Core.MainWindow",
        "type": "Overlay",
        "unnamed": 1,
        "visible": True
    },
    "WarningRectangle1": {
        "container": "WarningOverlay1",
        "id": "root",
        "type": "Rectangle",
        "unnamed": 1,
        "visible": True
    },
    "WarningPopUpWindow1": {
        "container": "CardWindow",
        "id": "popupBackground",
        "type": "Rectangle",
        "unnamed": 1,
        "visible": True
    },
    "WarningOkButton1": {
        "checkable": False,
        "container": "CardWindow",
        "id": "ok",
        "text": "OK",
        "type": "BransonPrimaryButton",
        "unnamed": 1,
        "visible": True
    },
    "WarningOverlay3": {
        "container": "Core.MainWindow",
        "type": "Overlay",
        "unnamed": 1,
        "visible": True
    },
    "WarningRectangle3": {
        "container": "WarningOverlay1",
        "id": "root",
        "type": "Rectangle",
        "unnamed": 1,
        "visible": True
    },
    "WarningPopUpWindow3": {
        "container": "Core.MainWindow",
        "id": "popupBackground",
        "type": "Rectangle",
        "unnamed": 1,
        "visible": True
    },
    "WarningOkButton3": {
        "checkable": False,
        "container": "Core.MainWindow",
        "id": "ok",
        "text": "OK",
        "type": "BransonPrimaryButton",
        "unnamed": 1,
        "visible": True
    },
    "InputBoxes": {
        "Constants.RecipeParameters.PretriggerAmplitude": {
            "Input Rectangle": "PretriggerAmplitudeInputRectangle",
            "Text": "PretriggerAmplitudeText",
            "Mouse Area": "PretriggerAmplitudeClickMouseArea",
            "Info Button": "DUMMY"
        },
        "Constants.RecipeParameters.PretriggerTime": {
            "Input Rectangle": "PretriggerTimeInputRectangle",
            "Text": "PretriggerTimeText",
            "Mouse Area": "PretriggerTimeClickMouseArea",
            "Info Button": "DUMMY"
        },
        "Constants.RecipeParameters.PretriggerDistance": {
            "Input Rectangle": "PretriggerDistanceInputRectangle",
            "Text": "PretriggerDistanceText",
            "Mouse Area": "PretriggerDistanceClickMouseArea",
            "Info Button": "DUMMY"
        },
        "Constants.RecipeParameters.AfterburstDelay": {
            "Input Rectangle": "AfterburstDelayInputRectangle",
            "Text": "AfterburstDelayText",
            "Mouse Area": "AfterburstDelayClickMouseArea",
            "Info Button": "DUMMY"
        },
        "Constants.RecipeParameters.AfterburstTime": {
            "Input Rectangle": "AfterburstTimeInputRectangle",
            "Text": "AfterburstTimeText",
            "Mouse Area": "AfterburstTimeClickMouseArea",
            "Info Button": "DUMMY"
        },
        "Constants.RecipeParameters.AfterburstAmplitude": {
            "Input Rectangle": "AfterburstAmplitudeInputRectangle",
            "Text": "AfterburstAmplitudeText",
            "Mouse Area": "AfterburstAmplitudeClickMouseArea",
            "Info Button": "DUMMY"
        },
        "Constants.RecipeParameters.DigitalTune": {
            "Input Rectangle": "DigitalTuneInputRectangle",
            "Text": "DigitalTuneText",
            "Mouse Area": "DigitalTuneClickMouseArea",
            "Info Button": "DUMMY"
        },
        "Constants.RecipeParameters.InternalFrequencyOffset": {
            "Input Rectangle": "InternalFrequencyOffsetInputRectangle",
            "Text": "InternalFrequencyOffsetText",
            "Mouse Area": "InternalFrequencyOffsetClickMouseArea",
            "Info Button": "DUMMY"
        },
        "Constants.RecipeParameters.EnergyBrakeTime": {
            "Input Rectangle": "EnergyBrakeTimeInputRectangle",
            "Text": "EnergyBrakeTimeText",
            "Mouse Area": "EnergyBrakeTimeClickMouseArea",
            "Info Button": "DUMMY"
        },
        "Constants.RecipeParameters.EnergyBrakeAmplitude": {
            "Input Rectangle": "EnergyBrakeAmplitudeInputRectangle",
            "Text": "EnergyBrakeAmplitudeText",
            "Mouse Area": "EnergyBrakeAmplitudeClickMouseArea",
            "Info Button": "DUMMY"
        },
        "Constants.RecipeParameters.MaxTimeout": {
            "Input Rectangle": "MaxTimeoutInputRectangle",
            "Text": "MaxTimeoutText",
            "Mouse Area": "MaxTimeoutClickMouseArea",
            "Info Button": "DUMMY"
        }
    },
    "ToggleSwitches": {
        "Constants.RecipeParameters.Pretrigger": {
            "Input Rectangle": "PretriggerInputRectangle",
            "Text": "PretriggerText",
            "Toggle Switch": "PretriggerToggleSwitch",
            "Info Button": "PretriggerInfoButton"
        },
        "Constants.RecipeParameters.Afterburst": {
            "Input Rectangle": "AfterburstInputRectangle",
            "Text": "AfterburstText",
            "Toggle Switch": "AfterburstToggleSwitch",
            "Info Button": "AfterburstInfoButton"
        },
        "Constants.RecipeParameters.EndOfWeldStore": {
            "Input Rectangle": "EndOfWeldStoreInputRectangle",
            "Text": "EndOfWeldStoreText",
            "Toggle Switch": "EndOfWeldStoreToggleSwitch",
            "Info Button": "EndOfWeldStoreInfoButton"
        },
        "Constants.RecipeParameters.FrequencyOffset": {
            "Input Rectangle": "FrequencyOffsetInputRectangle",
            "Text": "FrequencyOffsetText",
            "Toggle Switch": "FrequencyOffsetToggleSwitch",
            "Info Button": "FrequencyOffsetInfoButton"
        },
        "Constants.RecipeParameters.EnergyBraking": {
            "Input Rectangle": "EnergyBrakingInputRectangle",
            "Text": "EnergyBrakingText",
            "Toggle Switch": "EnergyBrakingToggleSwitch",
            "Info Button": "EnergyBrakingInfoButton"
        },
        "Constants.RecipeParameters.ActuatorClear": {
            "Input Rectangle": "ActuatorClearInputRectangle",
            "Text": "ActuatorClearText",
            "Toggle Switch": "ActuatorClearToggleSwitch",
            "Info Button": "ActuatorClearInfoButton"
        },
        "Constants.RecipeParameters.ExtraCooling": {
            "Input Rectangle": "ExtraCoolingInputRectangle",
            "Text": "ExtraCoolingText",
            "Toggle Switch": "ExtraCoolingToggleSwitch",
            "Info Button": "ExtraCoolingInfoButton"
        },
        "Constants.RecipeParameters.PreWeldSeek": {
            "Input Rectangle": "PreWeldSeekInputRectangle",
            "Text": "PreWeldSeekText",
            "Toggle Switch": "PreWeldSeekToggleSwitch",
            "Info Button": "PreWeldSeekInfoButton"
        },
        "Constants.RecipeParameters.Control": {
            "Input Rectangle": "ControlInputRectangle",
            "Text": "ControlText",
            "Toggle Switch": "ControlToggleSwitch",
            "Info Button": "DUMMY"
        },
        "Constants.RecipeParameters.GlobalSuspect": {
            "Input Rectangle": "GlobalSuspectInputRectangle",
            "Text": "GlobalSuspectText",
            "Toggle Switch": "GlobalSuspectToggleSwitch"
        }
    },
    "RadioButtons": {
        "Constants.RecipeParameters.PretriggerStart": {
            "Input Rectangle": "PretriggerStartInputRectangle",
            "Text": "PretriggerStartText",
            "Options": {
                "TIME": "PretriggerStartTimeRadioButton",
                "AUTO": "PretriggerStartAutoRadioButton",
                "DISTANCE": "PretriggerStartDistanceRadioButton"
            }
        },
        "Constants.RecipeParameters.Setting": {
            "Input Rectangle": "SettingInputRectangle",
            "Text": "SettingText",
            "Options": {
                "DISTANCE": "SettingDistanceRadioButton",
                "TIME": "SettingTimeRadioButton"
            }
        }
    }
}


right_menu = {
    "Button": {
        "container": "Core.MainWindow",
        "id": "imageRightMenu",
        "source": "qrc:/Images/RightMenu.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "LogoutText": {
        "container": "Core.MainWindow",
        "text": "Logout",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "LogoutImage": {
        "container": "Core.MainWindow",
        "id": "systemOptionImage",
        "source": "qrc:/Images/Logout Icon.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "ExitText": {
        "container": "Core.MainWindow",
        "text": "Exit",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "ExitImage": {
        "container": "Core.MainWindow",
        "id": "systemOptionImage",
        "source": "qrc:/Images/Power Off Icon.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "LangaugeText": {
        "container": "Core.MainWindow",
        "text": "English",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "LangaugeImage": {
        "container": "Core.MainWindow",
        "id": "systemOptionImage",
        "source": "qrc:/Images/Language2.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "ActuatorSetupImage": {
        "container": "Core.MainWindow",
        "id": "menuOptionImage",
        "source": "qrc:/Images/actuatorSetup.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "ActuatorSetupText": {
        "container": "Core.MainWindow",
        "text": "Actuator Setup",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "DiagnosticsText": {
        "container": "Core.MainWindow",
        "text": "Diagnostics",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "DiagnosticsImage": {
        "container": "Core.MainWindow",
        "id": "menuOptionImage",
        "source": "qrc:/Images/diagnostics.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "ImportExportText": {
        "container": "Core.MainWindow",
        "text": "Import/ Export",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "ImportExportImage": {
        "container": "Core.MainWindow",
        "id": "menuOptionImage",
        "source": "qrc:/Images/importExport.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    }
}


left_menu = {
    "Button": {
        "container": "Core.MainWindow",
        "id": "imageLeftMenu",
        "source": "qrc:/Images/LeftMenu.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "RecipeText": {
        "container": "Core.MainWindow",
        "text": "RECIPES",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "RecipeImage": {
        "container": "Core.MainWindow",
        "id": "menuOptionImage",
        "source": "qrc:/Images/recipe.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "ProductionText": {
        "container": "Core.MainWindow",
        "text": "PRODUCTION",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "ProductionImage": {
        "container": "Core.MainWindow",
        "id": "menuOptionImage",
        "source": "qrc:/Images/production.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "AnalyticsText": {
        "container": "Core.MainWindow",
        "text": "ANALYTICS",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "AnalyticsImage": {
        "container": "Core.MainWindow",
        "id": "menuOptionImage",
        "source": "qrc:/Images/analytics.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    },
    "SystemText": {
        "container": "Core.MainWindow",
        "text": "SYSTEM",
        "type": "Text",
        "unnamed": 1,
        "visible": True
    },
    "SystemImage": {
        "container": "Core.MainWindow",
        "id": "menuOptionImage",
        "source": "qrc:/Images/system.svg",
        "type": "Image",
        "unnamed": 1,
        "visible": True
    }
}