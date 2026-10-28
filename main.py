# Import the OLED, micro:bit, NeoPixel and music functions
from sh1106_microbit_lines import SH1106
from microbit import *
import neopixel
import music

# Project settings
DRY_THRESHOLD = 650
was_dry=False
oled = SH1106()

def draw_happy_face():
    # Pot
    oled.draw_line(110, 20, 110, 43)
    oled.draw_line(85, 18, 85, 46)
    oled.draw_line(110, 20, 85, 18)
    oled.draw_line(110, 43, 85, 46)
    
    # Head, stem, leaves and nose
    oled.draw_line(10, 5, 10, 58)
    oled.draw_line(55, 5, 55, 58)
    oled.draw_line(55, 5, 10, 5)
    oled.draw_line(55, 58, 10, 58)
    oled.draw_line(55, 32, 85, 32)
    oled.draw_line(85, 32, 70, 50)
    oled.draw_line(85, 32, 70, 13)
    oled.draw_line(30, 32, 35, 32)

    # Happy expression
    oled.draw_line(24, 47, 19, 43)
    oled.draw_line(19, 43, 24, 39)
    oled.draw_line(24, 23, 19, 19)
    oled.draw_line(19, 19, 24, 15)
    oled.draw_line(41, 43, 47, 37)
    oled.draw_line(47, 37, 47, 24)
    oled.draw_line(47, 24, 41, 18)
    
def draw_sad_face():
    # Pot
    oled.draw_line(110, 20, 110, 43)
    oled.draw_line(85, 18, 85, 46)
    oled.draw_line(110, 20, 85, 18)
    oled.draw_line(110, 43, 85, 46)

    # Head, stem, leaves and nose
    oled.draw_line(10, 5, 10, 58)
    oled.draw_line(55, 5, 55, 58)
    oled.draw_line(55, 5, 10, 5)
    oled.draw_line(55, 58, 10, 58)
    oled.draw_line(55, 32, 85, 32)
    oled.draw_line(85, 32, 70, 50)
    oled.draw_line(85, 32, 70, 13)
    oled.draw_line(30, 32, 35, 32)

    # Sad expression
    oled.draw_line(21, 47, 25, 39)
    oled.draw_line(25, 23, 21, 15)
    oled.draw_line(49, 43, 44, 37)
    oled.draw_line(44, 37, 44, 24)
    oled.draw_line(44, 24, 49, 18)

def draw_silly_face():
    # Pot
    oled.draw_line(110, 20, 110, 43)
    oled.draw_line(85, 18, 85, 46)
    oled.draw_line(110, 20, 85, 18)
    oled.draw_line(110, 43, 85, 46)

    # Head, stem, leaves and nose
    oled.draw_line(10, 5, 10, 58)
    oled.draw_line(55, 5, 55, 58)
    oled.draw_line(55, 5, 10, 5)
    oled.draw_line(55, 58, 10, 58)
    oled.draw_line(55, 32, 85, 32)
    oled.draw_line(85, 32, 70, 50)
    oled.draw_line(85, 32, 70, 13)
    oled.draw_line(30, 32, 35, 32)

    # Silly expression
    oled.draw_line(18, 47, 23, 39)
    oled.draw_line(23, 39, 28, 47)
    oled.draw_line(18, 15, 23, 23)
    oled.draw_line(23, 23, 28, 15)
    oled.draw_line(45, 43, 42, 36)
    oled.draw_line(42, 36, 47, 31)
    oled.draw_line(47, 31, 42, 26)
    oled.draw_line(42, 26, 45, 19)

def draw_love_face():
    #Pot
    oled.draw_line(110, 20, 110, 43)
    oled.draw_line(85, 18, 85, 46)
    oled.draw_line(110, 20, 85, 18)
    oled.draw_line(110, 43, 85, 46)

    # Head, stem, leaves and nose
    oled.draw_line(10, 5, 10, 58)
    oled.draw_line(55, 5, 55, 58)
    oled.draw_line(55, 5, 10, 5)
    oled.draw_line(55, 58, 10, 58)
    oled.draw_line(55, 32, 85, 32)
    oled.draw_line(85, 32, 70, 50)
    oled.draw_line(85, 32, 70, 13)
    oled.draw_line(30, 32, 35, 32)
    oled.draw_line(20, 48, 17, 45)

    # Loved expression
    oled.draw_line(17, 45, 20, 42)
    oled.draw_line(20, 42, 17, 39)
    oled.draw_line(17, 39, 20, 36)
    oled.draw_line(20, 36, 27, 42)
    oled.draw_line(27, 42, 20, 48)
    oled.draw_line(20, 25, 17, 22)
    oled.draw_line(17, 22, 20, 19)
    oled.draw_line(20, 19, 17, 16)
    oled.draw_line(17, 16, 20, 13)
    oled.draw_line(20, 13, 27, 19)
    oled.draw_line(27, 19, 20, 25)
    oled.draw_line(41, 43, 47, 37)
    oled.draw_line(47, 37, 47, 24)
    oled.draw_line(47, 24, 41, 18)


def show_face(face):
    # Clear the previous image
    oled.clear(draw=False)

    # Choose an expression
    if face == "sad":
        draw_sad_face()

    elif face == "silly":
        draw_silly_face()

    elif face == "love":
        draw_love_face()
        
    else:
        draw_happy_face()
        
    # Update the physical OLED screen
    oled.draw_screen()
    
# Set up the 12-pixel NeoPixel ring on P2
np = neopixel.NeoPixel(pin2, 12)

# Startup response
np.fill((20,0,15))
show_face("love")
np.show()
sleep(8000)

while True:
    
    # Read the soil moisture sensor from P1
    moisture = pin1.read_analog()
    
    # Convert the sensor comparison into a Boolean value.
    # True means the reading is below the dry threshold.
    is_dry = moisture < DRY_THRESHOLD

    # Press A and B together for the silly response
    if button_a.is_pressed() and button_b.is_pressed():
        show_face("silly")
        music.play(music.BA_DING, pin=pin0)
        np.fill((20,20,0))
        np.show()
        sleep(2000)
        
    # Button A gives a happy response
    elif button_a.was_pressed():
        show_face("happy")
        music.play(music.ENTERTAINER, pin=pin0)
        np.fill((0,20,0))
        np.show()
        sleep(2000)
        
    # Button B gives a sad response
    elif button_b.was_pressed():
        show_face("sad")             
        if is_dry and not was_dry:
            music.play(music.POWER_DOWN, pin=pin0)
        np.fill((0,0,20))
        np.show()
        sleep(2000)
        
    # Automatically enter the sad state when the soil is dry.        
    elif is_dry:
        show_face("sad")
        np.fill((0, 0, 20))
        np.show()
        
        # Only play the warning when the plant first becomes dry.
        if not was_dry:
            music.play(music.POWER_DOWN, pin=pin0)

        was_dry = True
        sleep(2000)
        
    # If no dry condition is detected, show the healthy state.
    else:
        show_face("happy")
        np.fill((0, 20, 0))
        np.show()
        
        if was_dry:
            music.play(music.ENTERTAINER, pin=pin0)

        was_dry = False
        sleep(2000)
