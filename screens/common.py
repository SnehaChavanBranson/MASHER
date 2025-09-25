import squish
from constants import names
import test
from helper import core

def scroll_limits():
    squish.snooze(0.2)
    test.log("Scrolling the Flickable area")
    
    obj = squish.waitForObject(names.recipeLabWindow_gridView_GridView)
    
    # Optional: click the object to focus it
    # core.ClickButton(squish.waitForObject(obj))
    
    # squish.mouseWheel(obj, 1407, 372, 0, -45, 0)
    
    squish.mouseWheel(obj, 644, 13, 0, -25, 167772160)

    # Perform 3 scrolls downward with default values
    # for _ in range(3):
    #     squish.mouseWheel(obj, 0, 0, 0, 30, 0)

#flickable = squish.waitForObject(names.recipeLabWindow_infoScrollRec_Flickable)
# squish.mouseWheel(flickable, 1407, 372, 0, -45, 0)
# test.log("Scroll actions completed.")

def scroll_params():
    squish.snooze(0.2)
    test.log("Scrolling the Flickable area")
    
    obj = squish.waitForObject(names.recipeLabWindow_infoScrollRec_Flickable)
    squish.mouseWheel(obj, 644, 13, 0, -40, 167772160)
    