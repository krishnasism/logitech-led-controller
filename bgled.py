import pythoncom, pyHook
from logipy import logi_led
import time
import ctypes
import random

def OnKeyboardEvent(event):
    try:
        if event.Key=='W':
            logi_led.logi_led_set_lighting(100, 0, 0)
        elif event.Key=='S':
            logi_led.logi_led_set_lighting(0,100,0)
        elif event.Key=='D':
            logi_led.logi_led_set_lighting(0,0,100)
        elif event.Key=='A':
            logi_led.logi_led_set_lighting(100,0,100)
        else:
            logi_led.logi_led_set_lighting(random.randint(0,100),random.randint(0,100),random.randint(0,100))
    except Exception as e:
        pass
          


# return True to pass the event to other handlers
    return True

logi_led.logi_led_init()

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()

logi_led.logi_led_shutdown()

