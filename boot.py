import storage

from digitalio import DigitalInOut, Direction, Pull
import board
import usb_midi


button = DigitalInOut(board.GP12)
button.direction = Direction.INPUT
button.pull = Pull.UP

if button.value:
    storage.disable_usb_drive()
    usb_midi.disable()
else:
    storage.enable_usb_drive()
    



