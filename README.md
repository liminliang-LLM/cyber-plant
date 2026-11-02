# Cyber Plant

Cyber Plant is an interactive physical-computing prototype created with a BBC micro:bit.

The project gives a plant a simple digital personality. It reads the soil moisture level and responds using facial expressions, coloured lights and sound.

<img width="1072" height="1430" alt="cf7dacdf9a1380d50d1b59386ff96230" src="https://github.com/user-attachments/assets/2b049623-1470-4d44-9291-42edf58c590d" />

## What it does

A soil moisture sensor is inserted into the plant pot and connected to a BBC Micro:bit V2.

When the sensor starts, it'll appear a loved face, and the Neopixel ring will turn to pink for 8 seconds. If the soil is wet enough, the plant shows a happy face, the NeoPixel ring turns green, and it plays an entertainer music through the micro:bit's built-in speaker. When the soil becomes dry, the plant shows a sad face, changes colour and plays a power-down music.

The Micro:bit buttons can also trigger different expressions, when press button A, it'll show a happy face, when press button B, the expression turns to sad, if press A and B together, it'll appear a silly face.

## Hardware

- BBC micro:bit V2
<img width="4000" height="3000" alt="84063d9626d950ca83b6950c5bc6f2da" src="https://github.com/user-attachments/assets/dc4a3368-4321-4609-a423-11caef562b86" />

- Micro:bit breakout board
<img width="1706" height="1280" alt="90285584e3e7f3ba2f6134071d052972" src="https://github.com/user-attachments/assets/753815e1-9f77-40fb-8f10-d8cb6c5593d1" />

- Soil moisture sensor
<img width="1706" height="1280" alt="049ecdbeeef625b1af4ea8f36e0c85a5" src="https://github.com/user-attachments/assets/5e3c0db7-bbd6-4a1c-9883-acb796c697d3" />

- 1.3-inch SH1106 SPI OLED
<img width="1706" height="1280" alt="fd8216ca3b43d70b6f07b039f1db98b7" src="https://github.com/user-attachments/assets/2b88fffb-d47a-4e11-836a-ea35c023886b" />

- 12-pixel NeoPixel ring
<img width="1706" height="1280" alt="fc1b82613d6c19e0bfb988e7597db5e5" src="https://github.com/user-attachments/assets/e255eda0-28d8-4636-bf43-f81bce9c2408" />

- Breadboard
<img width="4000" height="3000" alt="c659c336ccbcd084f6f1c95e549eef9a" src="https://github.com/user-attachments/assets/4b7c8c8d-f394-45b6-a538-3c3c61de0143" />

- Jumper wires
<img width="1706" height="1280" alt="cf359b526566c7f9f58c03e1a376e599" src="https://github.com/user-attachments/assets/8f11c8dc-05bb-4254-9507-a28afae8866e" />


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
