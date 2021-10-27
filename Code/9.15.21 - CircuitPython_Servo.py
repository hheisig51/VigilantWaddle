# Written by Henry Heisig, 09.15.21
import time
import board
import pwmio
import servo
import touchio

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

touch = touchio.TouchIn(board.A0)
tauch = touchio.TouchIn(board.A4)

angle = 0
while True:
    if touch.value: # detects if the wire has been touched
        print("Touched A0")
        my_servo.angle = angle # sets the angle of the servo based off of what `angle` is
        if angle < 180: # 180 is the max degree capable
            angle = angle + 5 # adds 5 degrees if the value 
        if angle >= 180:
            angle = 180
        print(angle)
    if tauch.value:
        print("Tauched A4")
        my_servo.angle = angle
        if angle > 0:
            angle = angle - 5
        if angle <= 0:
            angle = 0
        print(angle)
    time.sleep(0.05)
