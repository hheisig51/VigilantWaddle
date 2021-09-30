# Let's get this DistanceSensor party started
print("code running!")
import adafruit_hcsr04
from adafruit_hcsr04 import HCSR04
trig = 
sonar = HCSR04(trig, echo)
print("hello!")
while True:
        print(sonar.dist_cm())
        sleep(.5)