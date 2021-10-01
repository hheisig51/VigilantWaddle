# Let's get this DistanceSensor party started
import board
import neopixel
import time
import simpleio
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
x = 0
y = 0
z = 0

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = .1

while True:
    try:
        print(str(sonar.distance), "cm")
        if sonar.distance < 5:
            x = 255
            y = 0
            z = 0
        if sonar.distance >= 5 and sonar.distance <= 20:
            x = simpleio.map_range(sonar.distance, 5, 20, 255, 0)
            y = 0
            z = simpleio.map_range(sonar.distance, 5, 20, 0, 255)
        if sonar.distance > 20 and sonar.distance <= 35:
            x = 0
            y = simpleio.map_range(sonar.distance, 20, 35, 0, 255)
            z = simpleio.map_range(sonar.distance, 20, 35, 255, 0)
        if sonar.distance > 35:
            x = 0
            y = 255
            z = 0
        dot.fill((int(x), int(y), int(z)))
        print((int(x), int(y), int(z)))
    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.1)
