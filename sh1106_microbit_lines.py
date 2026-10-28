# Minimal SH1106 coordinate-line library for BBC micro:bit.
#
# SOURCE 1:
# Robert Hammelrath et al., SH1106
# https://github.com/robert-hh/SH1106
# MIT License
#
# SOURCE 2:
# Pythom1234, pxt-oled
# https://github.com/Pythom1234/pxt-oled
# MIT License
#
# CHANGES:
# - machine.Pin and machine.SPI changed to micro:bit APIs.
# - framebuf removed.
# - TypeScript drawing functions translated to Python.
# - SSD1306 I2C changed to SH1106 SPI.
# - Wiring: CLK=P13, MOSI=P15, DC=P8, RES=P9, CS=P16.
# - Text, rectangles, images and pixel-reading were removed.

from microbit import (
    spi,
    pin8,
    pin9,
    pin13,
    pin14,
    pin15,
    pin16,
    sleep
)


WIDTH = 128
HEIGHT = 64
PAGES = HEIGHT // 8


class SH1106:

    # ADAPTED:
    # Combines both libraries and assigns micro:bit pins.
    def __init__(self, dc=pin8, reset=pin9, cs=pin16):
        self.dc = dc
        self.reset_pin = reset
        self.cs = cs

        # SOURCE 2:
        # Based on pxt-oled's 128x64 screen buffer.
        self.buffer = bytearray(WIDTH * PAGES)

        # ADAPTED:
        # Uses micro:bit SPI and this project's wiring.
        spi.init(
            baudrate=1000000,
            bits=8,
            mode=0,
            sclk=pin13,
            mosi=pin15,
            miso=pin14
        )

        self.cs.write_digital(1)
        self.dc.write_digital(0)
        self.reset_pin.write_digital(1)

        self._reset_display()
        self._initialize_display()
        self.clear()

    # SOURCE 1:
    # Adapted from SH1106_SPI.write_cmd().
    #
    # CHANGE:
    # Pin(value) changed to pin.write_digital(value).
    def _write_command(self, command):
        self.cs.write_digital(1)
        self.dc.write_digital(0)
        self.cs.write_digital(0)

        spi.write(bytearray([command]))

        self.cs.write_digital(1)

    # SOURCE 1:
    # Adapted from SH1106_SPI.write_data().
    #
    # CHANGE:
    # Uses micro:bit's global spi object.
    def _write_data(self, data):
        self.cs.write_digital(1)
        self.dc.write_digital(1)
        self.cs.write_digital(0)

        spi.write(data)

        self.cs.write_digital(1)

    # SOURCE 1:
    # Adapted from SH1106.reset().
    #
    # CHANGE:
    # Uses write_digital() and micro:bit sleep().
    def _reset_display(self):
        self.reset_pin.write_digital(1)
        sleep(1)

        self.reset_pin.write_digital(0)
        sleep(20)

        self.reset_pin.write_digital(1)
        sleep(20)

    # ADAPTED FROM BOTH SOURCES:
    #
    # SSD1306-only I2C addressing and zoom commands
    # were removed.
    #
    # SH1106 DC-DC control 0xAD, 0x8B is used.
    def _initialize_display(self):
        commands = (
            0xAE,        # Display off
            0xD5, 0x80,  # Display clock
            0xA8, 0x3F,  # 64 display rows
            0xD3, 0x00,  # Display offset
            0x40,        # Display start line
            0xAD, 0x8B,  # SH1106 DC-DC control
            0xA1,        # Segment remap
            0xC8,        # COM scan direction
            0xDA, 0x12,  # COM pin configuration
            0x81, 0x80,  # Contrast
            0xD9, 0x22,  # Pre-charge period
            0xDB, 0x35,  # VCOM level
            0xA4,        # Follow display memory
            0xA6,        # Normal display
            0xAF         # Display on
        )

        for command in commands:
            self._write_command(command)

    # SOURCE 2:
    # Python translation of pxt-oled clear().
    #
    # CHANGE:
    # TypeScript Buffer.fill() changed to a Python loop.
    def clear(self, draw=True):
        for index in range(len(self.buffer)):
            self.buffer[index] = 0

        if draw:
            self.draw_screen()

    # SOURCE 2:
    # Python translation of pxt-oled setPx().
    #
    # CHANGES:
    # - Removed the I2C control byte from the index.
    # - Corrected y limit to 64 pixels.
    # - Uses 1 and 0 instead of true and false.
    def set_px(self, x, y, color=1):
        if x < 0 or x >= WIDTH:
            return

        if y < 0 or y >= HEIGHT:
            return

        page, bit_position = divmod(y, 8)
        index = page * WIDTH + x

        if color:
            self.buffer[index] |= 1 << bit_position
        else:
            self.buffer[index] &= ~(1 << bit_position)

    # SOURCE 2:
    # Python translation of pxt-oled drawLine().
    #
    # CHANGES:
    # - TypeScript syntax translated into Python.
    # - Temporary line array removed.
    # - Each calculated coordinate is written immediately.
    def draw_line(self, x1, y1, x2, y2, color=1):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1

        error = dx - dy

        while True:
            self.set_px(x1, y1, color)

            if x1 == x2 and y1 == y2:
                break

            error_twice = 2 * error

            if error_twice > -dy:
                error -= dy
                x1 += sx

            if error_twice < dx:
                error += dx
                y1 += sy

    # SOURCE 1:
    # Adapted from SH1106.show().
    #
    # CHANGES:
    # - Sends all eight screen pages.
    # - Keeps SH1106's two-column offset.
    def draw_screen(self):
        for page in range(PAGES):
            self._write_command(0xB0 | page)
            self._write_command(0x02)
            self._write_command(0x10)

            start = page * WIDTH
            end = start + WIDTH

            self._write_data(
                self.buffer[start:end]
            )