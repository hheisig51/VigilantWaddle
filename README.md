# Engineering III Notebook

# Circuit Python: Heisig's First Adventure in Engineering III
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Hi there again! We're back, and we're better than ever. In this, I've made a LED on an Arduino (via Python) fade & flash in a rainbow-ish pattern. 

Once you import the libraries needed, it's time to set up the variables for the separate color channels of the neopixel LED

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
```


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




## CircuitPython_Servo
  **Servo time! (with a *touch* of love)**
### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

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

And of  e - shoutout to all my classmates, and my lab partner of two years; [Shrey
