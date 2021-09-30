# Let's get this DistanceSensor party started
import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
while True:
        try:
                print((sonar.distance,))
        except RuntimeError:
                print("Retrying!")
                pass
        time.sleep(0.1)