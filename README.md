# Cyber Plant

Cyber Plant is an interactive physical-computing prototype created with a BBC micro:bit.

The project gives a plant a simple digital personality. It reads the soil moisture level and responds using facial expressions, coloured lights and sound.

## What it does

A soil moisture sensor is inserted into the plant pot and connected to a BBC Micro:bit V2.

When the sensor starts, it'll appear a loved face, and the Neopixel ring will turn to pink for 8 seconds. If the soil is wet enough, the plant shows a happy face, the NeoPixel ring turns green, and it plays an entertainer music through the micro:bit's built-in speaker. When the soil becomes dry, the plant shows a sad face, changes colour and plays a power-down music.

The Micro:bit buttons can also trigger different expressions, when press button A, it'll show a happy face, when press button B, the expression turns to sad, if press A and B together, it'll appear a silly face.

## Hardware

- BBC micro:bit V2
- Micro:bit breakout board
- Soil moisture sensor
- 1.3-inch SH1106 SPI OLED
- 12-pixel NeoPixel ring
- Breadboard
- Jumper wires

## Connections

### Soil moisture sensor

- Signal: P1
- Power: 3V3
- Ground: GND

### NeoPixel ring

- Data: P2
- Power: 3V3
- Ground: GND

### OLED

- CLK: P13
- MOSI: P15
- DC: P8
- RES: P9
- CS: P16
- VCC: 3V3
- GND: GND

## Code

`main.py` contains the sensor readings, button interactions, facial expressions, NeoPixel colours and sound responses.

`sh1106_microbit_lines.py` contains the functions used to communicate with the OLED and draw lines using screen coordinates.

The faces and plant character are made from multiple `draw_line()` instructions rather than image files.

## Running the project

1. Open the project in the micro:bit Python Editor.
2. Make sure both `main.py` and `sh1106_microbit_lines.py` are included.
3. Connect the micro:bit V2 by USB.
4. Send the program to the micro:bit.
5. Insert the moisture sensor into the soil.
6. Adjust the moisture threshold in `main.py` if necessary.

The moisture value depends on the soil, sensor depth and amount of water, so the threshold may need to be recalibrated.

## OLED code references

My OLED uses an SH1106 controller, which was not directly supported by the Micro:bit python editor. I used AI as an assistant to help me adapt parts of the following open-source projects for the OLED communication and drawing functions:

- [Robert-hh/SH1106](https://github.com/robert-hh/SH1106)
- [Pythom1234/pxt-oled](https://github.com/Pythom1234/pxt-oled)

The plant character, expressions, interaction design and project logic were created for this project.
