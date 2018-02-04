#!/usr/bin/python
from picamera import PiCamera
from gpiozero import Button
from gpiozero import LED

button = Button(17)
greenled = LED(10)
redled = LED(22)
blueled = LED(11)

camera = PiCamera()

camera.stop_preview()
greenled.off()
redled.off()
blueled.off()
