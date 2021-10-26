# Engineering III Notebook
# Circuit Python:

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
---

## Hello_CircuitPython
**Let's get vi-su-al, vi-su-al**
### Description & Code
Hi there again! We're back, and we're better than ever. In this, I've made a LED on an Arduino (via Python) fade & flash in a rainbow-ish pattern. 

```python
# Written by Henry Heisig
import board
import neopixel
import time

x = 50
y = 50
z = 50
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

dot.brightness = .1
```
The LED color is set to be those variables we set up above, and then move to doing the math on making them change at different rates.
```python
while True:
    dot.fill((x, y, z))
    time.sleep(.25)
    x = x + 1
    if x >= 255:
        x = 50

    y = y + 5
    if y >= 255:
        y = 50
```
For example, every time this loops, ```z``` gets 10 added to it, and then it checks if z is at or above 255 (the max value the channel can be). If z is at or above 255, it gets knocked back down to 5, to then start the process over again.
```python
    z = z + 10
    if z >= 255:
        z = 50

    print((x, y, z))
```

### Evidence
| [Code .py file](https://github.com/hheisig51/VigilantWaddle/blob/54f87c2e407671d9991133bff1444b09ff88951b/Code/9.1.21%20-%20Hello_CircuitPython.py?plain=1)  |
| ---- |
| [Youtube playlist of videos](https://youtube.com/playlist?list=PLWQhE570pqHrpQAAHPEJapQYsuC3Ob_V9)  |

https://user-images.githubusercontent.com/71345201/133451297-49025164-4126-4a11-ae27-32b3ffb30b0a.mp4

https://user-images.githubusercontent.com/71345201/133452459-4e8d6e7f-8229-4ffa-ac65-582f2c7dd55c.mp4

### Wiring

In this example, no wiring is needed. The neopixel on the Adafruit Arduino Metro was used.

### Reflection
1. In the code above, the `dot.brightness = .1` is important for preventing any LED burnout, alongside enabling the LED to better produce the colors.
2. At the end of the code above, the `print((x, y, z))` is part of a bigger thing to remember; printing to the serial monitor is highly important in every project. Don't overwhelmn it, but use it as a tool.

This assignment is a basis for learning more about CircuitPython. There's only thing to plug in is the board. The hardest part was actually figuring out the code to change the channels at different rates. Python is such an able language, that finding the exact resource you need is hard. Search engines (Ecosia, DuckDuckGo, Google, etc.) are all good tools to be able to peruse the web.

Also, ASK! PEOPLE! QUESTIONS! If you don't, the person next to you is 10 steps ahead, it
s because they asked the person who's ahead by 11. If you manage to find something that nobody has documented, please document it yourself.

## CircuitPython_Servo
  **Servo time! (with a *touch* of love)**
### Description & Code
So, our objective today is to properly wire up a servo, and then use two wires, via touch, to control the servo.

First step: wire the board and servo as shown below. If you want to, you can change the analog pins around, just make sure you change it in the code also.
```python
# Write your code here :-)
import time
import board
import pwmio
import servo
import touchio
```
`import nomoreimports`.

`pwmio`, `servo`, and `touchio` are new this go-around, so make sure you grab   `servo.mpy` and put it into your `lib` folder

([Here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/) you can grab a CircuitPython Library shmorgishborg. In `/lib/adafruit_motor` you'll find servo.mpy)

```python
# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

touch = touchio.TouchIn(board.A0)
tauch = touchio.TouchIn(board.A4)
```
- The `pwm =` sets up the actual frequency the board will output that (via the analog pins) to the servo.
- `my_servo` makes sure we can actually send values to the servo, and have them be correct.
- The `touch =` and `tauch =` setup the input from the two pin `A0` and `A4`

```python
angle = 0
while True:
    if touch.value: 
        print("Touched A0")
        my_servo.angle = angle
        if angle < 180:
            angle = angle + 5
        if angle >= 180:
            angle = 180
        print(angle)
```
- `angle = 0` resets the value before any loop starts, just to prevent errors.
- `if touch.value:` carries out what's contained if something touches A0 (like we set it up above)
- `my_servo.angle = angle` set's the actual servo angle based off of the value of `angle`
- The next series of statements, everytime this runs;
    - increase the angle by 5 degrees if it's less than 180
    - if 180 or greater, keeps it at 180, to prevent any errors from sending too large of a number to the servo
    - prints the value of `angle`, for serial monitor monitor-ing

```python
    if tauch.value:
        print("Tauched A4")
        my_servo.angle = angle
        if angle > 0:
            angle = angle - 5
        if angle <= 0:
            angle = 0
        print(angle)
    time.sleep(0.05)
```
- Very similar thing as description above, just for `A4` instead (see how it's `tauch` instead of `touch`?).
- Just goes down by 5 degree increments to 0.
- There's also the `time.sleep` function that calls at the end of the whole `while True:` loop.

Also, [this Adafruit tutorial](https://learn.adafruit.com/circuitpython-essentials/circuitpython-cap-touch) gave the very essential building blocks for me to start the whole assignment.

### Evidence
| [Code .py file](https://github.com/hheisig51/VigilantWaddle/blob/6b992f8651e3bf654e8c98281999d74d3c7aee57/Code/9.15.21%20-%20CircuitPython_Servo.py?plain=1)  |
| ---- |
| [Youtube playlist of videos](https://www.youtube.com/playlist?list=PLWQhE570pqHqSyWS2b8-lJPu_HJ_XI2gx)  |


https://user-images.githubusercontent.com/71345201/134691396-404dfc4b-370d-4e89-9533-c13554280411.mp4


https://user-images.githubusercontent.com/71345201/134691403-e6190f6b-589d-4bf4-b237-5a373c5ada7f.mp4


### Wiring

![CircuitPython_Servo Diagram](https://github.com/hheisig51/VigilantWaddle/blob/main/Diagrams/Renders/CircuitPython_Servo.png?raw=true)

### Reflection
The reflections are hard to write. I wish I was Narcissus, and could fall in love with them.

Anyway, you've seen the assignment, now for the lesson; copying code. Like I linked adafruit above, and may link my classmates in the future, there's no need to invent the wheel twice. Steal, borrow, copy, take, link, anything. Just give credit where credit is due, and you'll be as golden as the [ram that flew Phrixus and Helle](https://en.wikipedia.org/wiki/Golden_Fleece).

This assignment was simple as pumpkin pie, because the stuff I borrowed would've been the hardest had I written it myself.

## Special Thanks
Thank you to [Mr. Helmstetter](https://github.com/Helmstk1) and [Mr. Dierolf](https://github.com/david-dierolf) at [Charlottesville High School](https://github.com/chssigma/) for being super helpful 

Thank you to [Github](https://github.com/) (do you really need a link?), [VSCode](https://code.visualstudio.com/) (Which I'm writing this from), [Mu](https://codewith.mu/), [OBS](https://obsproject.com/), [FFmpeg](https://www.ffmpeg.org/), and [QWinFF](https://qwinff.github.io/) for being awesome software resources.

And of course - shoutout to all my classmates, and my lab partner of two years; [Shrey P.](https://github.com/shrey45)
