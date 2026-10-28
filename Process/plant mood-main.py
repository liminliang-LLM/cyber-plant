# Imports go at the top
from microbit import *

import neopixel
np = neopixel.NeoPixel(pin0, 12)

np = neopixel.NeoPixel(pin0, 12)
np.fill((20,0,15))
sleep(1000)
np.show()

display.show(Image.HEART)
sleep(500)

while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
        sleep(1000)
        np.fill((0,20,0))
        np.show()

    if button_b.was_pressed():
        display.show(Image.SAD)
        np.fill((0,0,20))
        np.show()
        sleep(1000)

    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.SILLY)
        np.fill((20,20,0))
        np.show()
        sleep(1000)    
