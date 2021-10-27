# Written by Henry Heisig, 09.01.21
import board
import neopixel
import time

x = 50
y = 50
z = 50
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

dot.brightness = .1

while True:
    dot.fill((x, y, z))
    time.sleep(.25)
    x = x + 1
    if x >= 255:
        x = 50

    y = y + 5
    if y >= 255:
        y = 50

    z = z + 10
    if z >= 255:
        z = 50

    print((x, y, z))
