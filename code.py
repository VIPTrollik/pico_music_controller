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


#pinout:
# GP16 -> play / stop button
# GP17 -> shuffle button
# GP18 -> forward
# GP19 -> backward
# GP20, GP21 -> encoder


#play/stop button
playStopButton = DigitalInOut(board.GP16)
playStopButton.direction = Direction.INPUT
playStopButton.pull = Pull.UP

#shuffleButton
shuffleButton = DigitalInOut(board.GP17)
shuffleButton.direction = Direction.INPUT
shuffleButton.pull = Pull.UP

#forwardButton
forwardButton = DigitalInOut(board.GP18)
forwardButton.direction = Direction.INPUT
forwardButton.pull = Pull.UP

#backwardButton
backwardButton = DigitalInOut(board.GP19)
backwardButton.direction = Direction.INPUT
backwardButton.pull = Pull.UP

#encoder pin A
rotPinA = DigitalInOut(board.GP20)
rotPinA.direction = Direction.INPUT
rotPinA.pull = Pull.UP

#encoder pin B
rotPinB = DigitalInOut(board.GP21)
rotPinB.direction = Direction.INPUT
rotPinB.pull = Pull.UP




last = True
preval = True
keyboard = ConsumerControl(usb_hid.devices)

playStopButtonLast = True
shuffleButtonLast = True
forwardButtonLast = True
backwardButtonLast = True


while True:
    if preval != rotPinA.value:
        if rotPinA.value:
            if rotPinB.value:
                keyboard.send(ConsumerControlCode.VOLUME_DECREMENT)  
            else:
                keyboard.send(ConsumerControlCode.VOLUME_INCREMENT)
        preval = rotPinA.value
        
    #play/stop
    playStopButtonNew = playStopButton.value
    if playStopButtonLast and not playStopButtonNew:
        keyboard.send(ConsumerControlCode.PLAY_PAUSE)
        lastTime = ticks_ms()
    playStopButtonLast = playStopButtonNew
    #shuffle
    shuffleButtonNew = shuffleButton.value
    if shuffleButtonLast and not shuffleButtonNew:
        keyboard.send(ConsumerControlCode.MUTE)
        lastTime = ticks_ms()
    shuffleButtonLast = shuffleButtonNew
    #forward
    forwardButtonNew = forwardButton.value
    if forwardButtonLast and not forwardButtonNew:
        keyboard.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        lastTime = ticks_ms()
    forwardButtonLast = forwardButtonNew
    #backward
    backwardButtonNew = backwardButton.value
    if backwardButtonLast and not backwardButtonNew:
        keyboard.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        lastTime = ticks_ms()
    backwardButtonLast = backwardButtonNew
    
   
    
   # time.sleep(0.05)
   


