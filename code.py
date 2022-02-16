import time
import usb_hid
import board

from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import board
from supervisor import ticks_ms
# Initialize Keybaord



    
keyboard = ConsumerControl(usb_hid.devices)

button = DigitalInOut(board.GP16)
button.direction = Direction.INPUT
button.pull = Pull.UP

rotPinA = DigitalInOut(board.GP21)
rotPinA.direction = Direction.INPUT
rotPinA.pull = Pull.UP

rotPinB = DigitalInOut(board.GP20)
rotPinB.direction = Direction.INPUT
rotPinB.pull = Pull.UP


last = True

preval = True

lastTime = ticks_ms()



while True:
    if preval != rotPinA.value:
        if rotPinA.value:
            if rotPinB.value:
                keyboard.send(ConsumerControlCode.VOLUME_DECREMENT)  
            else:
                keyboard.send(ConsumerControlCode.VOLUME_INCREMENT)
        preval = rotPinA.value
    
    if last and not button.value:
        if ticks_ms() - lastTime > 200:
            keyboard.send(ConsumerControlCode.PLAY_PAUSE)
            print("BTN RELEASED")
            lastTime = ticks_ms()
    
   # time.sleep(0.05)
   


