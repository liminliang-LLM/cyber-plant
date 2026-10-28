# Imports go at the top
from microbit import *

import neopixel
import music

DRY_THRESHOLD = 350
was_dry=False

np = neopixel.NeoPixel(pin2, 12)
np.fill((20,0,15))
sleep(1000)
np.show()

display.show(Image.HEART)
sleep(500)

while True:

    moisture = pin1.read_analog()
    is_dry = moisture < DRY_THRESHOLD
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.SILLY)
        music.play(music.BA_DING, pin=pin0)
        np.fill((20,20,0))
        sleep(1000)
        np.show()

    elif button_a.was_pressed():
        display.show(Image.HAPPY)
        music.play(music.ENTERTAINER, pin=pin0)
        np.fill((0,20,0))
        sleep(1000)
        np.show()

    elif button_b.was_pressed():
        display.show(Image.SAD)
                     
        if is_dry and not was_dry:
            music.play(music.POWER_DOWN, pin=pin0)

        music.play(music.POWER_DOWN, pin=pin0)
        np.fill((0,0,20))
        sleep(1000)
        np.show()
        
    elif is_dry:
        display.show(Image.SAD)
        np.fill((0, 0, 20))
        np.show()

        if not was_dry:
            music.play(music.POWER_DOWN, pin=pin0)

        was_dry = True
        sleep(500)

    else:
        display.show(Image.HAPPY)
        np.fill((0, 20, 0))
        np.show()

        was_dry = False
        sleep(500)
