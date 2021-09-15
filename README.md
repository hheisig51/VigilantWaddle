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

Here's how you make code look like code:

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
| [Code (non-spaghetti)](https://github.com/hheisig51/VigilantWaddle/blob/main/Code/9.1.21%20-%20Neopixel.py)  |
|---------------------------|
| [Video of code and explanation](https://www.youtube.com/watch?v=ur3YObRFBiA) |
| [Video of LED fading](https://www.youtube.com/watch?v=qmAAbJh5IMo) |
| [Timelapse of LED fading](https://www.youtube.com/watch?v=fOe3XIUi3Gw) |
| [Raw video files](https://github.com/hheisig51/VigilantWaddle/blob/main/Videos) |

### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

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
