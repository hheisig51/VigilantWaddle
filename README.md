# Engineering III Notebook

# Circuit Python: Heisig's First Adventure in Engineering III
[Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
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
```
Once you import the libraries needed, it's time to set up the variables for the separate color channels of the neopixel LED. Also, we need to turn down the brightness so the LED doesn't burn out. And, you know, so our eyes don't burn out.
```python
x = 50
y = 50
z = 50
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

dot.brightness = .1
```
Next, we set the LED color to be those variables we set up above, and then move to doing the math on making them change at different rates.
```python
while True:
    dot.fill((x, y, z))
    time.sleep(.25)
```
For the love of everything holy, please don't forget ```time.sleep```, otherwise you get a disco inferno, and not the nice kind.
```python
    x = x + 1
    if x >= 255:
        x = 50

    y = y + 5
    if y >= 255:
        y = 50
```
For example, every time this loops, ```z``` gets 10 added to it, and then it checks if z is at or above 255 (the max value the channel can be). If z is at or above 255, it gets knocked back down to 5, to then start the process over again
```python
    z = z + 10
    if z >= 255:
        z = 50

    print((x, y, z))
```
(To the tune of the [Simple Minds' song](https://youtu.be/CdqoNKCCt7A?t=54)) Don't you, forget about se-

rial monitor printing.

### Evidence
| [Code .py file](https://github.com/hheisig51/VigilantWaddle/blob/main/Code/9.1.21%20-%20Neopixel.py)  |
| ---- |
| [Youtube playlist of videos](https://youtube.com/playlist?list=PLWQhE570pqHrpQAAHPEJapQYsuC3Ob_V9)  |

https://user-images.githubusercontent.com/71345201/133451297-49025164-4126-4a11-ae27-32b3ffb30b0a.mp4

https://user-images.githubusercontent.com/71345201/133452450-0c0d6621-a748-4929-bc57-153bb9b4892a.mp4

https://user-images.githubusercontent.com/71345201/133452459-4e8d6e7f-8229-4ffa-ac65-582f2c7dd55c.mp4

### Wiring

In this example, no wiring is needed. The neopixel on the Adafruit Arduino Metro was used.

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.

This assignment, frankly, is the basis for learning more about CircuitPython. There's nothing to plug in except the board. The hardest part was actually figuring out the code to (very jankily) change the channels at different rates. Python is such an able language, that finding the exact resource you need is hard. Search engines (Ecosia, DuckDuckGo, Google, etc.) are all good tools to be able to peruse the web.

Also, ASK! PEOPLE! QUESTIONS! If you don't, the person next to you is 10 steps ahead, cause they asked the person who's 11. If you manage to find something that nobody has documented 

And, as I steal this from somebody on the internet: Take care, adventurer.

## CircuitPython_Servo
  **Servo time! (with a *touch* of love)**
### Description & Code

```python
Code goes here

```

### Evidence
| [Code .py file](https://github.com/hheisig51/VigilantWaddle/blob/main/Code/9.15.21%20-%20CircuitPython%20Servo.py)  |
| ---- |
| [Youtube playlist of videos](https://www.youtube.com/playlist?list=PLWQhE570pqHqSyWS2b8-lJPu_HJ_XI2gx)  |


https://user-images.githubusercontent.com/71345201/134691396-404dfc4b-370d-4e89-9533-c13554280411.mp4


https://user-images.githubusercontent.com/71345201/134691403-e6190f6b-589d-4bf4-b237-5a373c5ada7f.mp4


### Wiring

!(CircuitPython_Servo.png)

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection

## Special Thanks
Thank you to [Mr. Helmstetter](https://github.com/Helmstk1) and [Mr. Dierolf](https://github.com/david-dierolf) at [Charlottesville High School](https://github.com/chssigma/) for being super helpful 

Thank you to Github (do you really need a link?), [Mu](https://codewith.mu/), [OBS](https://obsproject.com/), [FFmpeg](https://www.ffmpeg.org/), and [QWinFF](https://qwinff.github.io/) for being awesome software resources.

And of course - shoutout to all my classmates, and my lab partner of two years; [Shrey P.](https://github.com/shrey45)
