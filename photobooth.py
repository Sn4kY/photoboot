#!/usr/bin/python
from picamera import PiCamera
from time import sleep
from gpiozero import Button
from gpiozero import LED
import subprocess

# Define LED configuration
# GPIO10 = PIN19
# GPIO11 = PIN23
# GPIO17 = PIN11
# GPIO22 = PIN15
button = Button(17)
greenled = LED(10)
redled = LED(22)
blueled = LED(11)

# Define Camera
camera = PiCamera()
camera.resolution = (1875, 2170)
camera.framerate = 15
camera.annotate_text_size = 100
# hflip for the mirror effect when taking pictures
camera.hflip = True

def destroy():
  camera.stop_preview()
  redled.off()
  blueled.off()
  greenled.off()
  subprocess.call('sudo killall fbi')

def main():
  while True:
    greenled.on()
    #camera.start_preview(fullscreen=False, window = (0, 20, 480, 640))
    camera.start_preview()
    camera.annotate_text = "Appuyez sur le bouton pour debuter !"
    
    button.wait_for_press()
    button.wait_for_release()
    greenled.off()
    for snap in range(1, 5):
      camera.annotate_text = "Preparation de la photo %s" % (snap)
      blueled.blink(0.25,0.25,3,False)
      blueled.blink(0.125,0.125,6,False)
      blueled.blink(0.0625,0.0635,12,False)
      blueled.off()
      camera.annotate_text = "SMILE !!!"
      camera.annotate_text = False
      camera.stop_preview()
      #camera.capture('/home/pi/photobooth_images/shot%s.jpg' % snap)
      camera.capture('/tmp/shot.jpg')
      redled.on()
      #subprocess.call('/home/pi/scripts/process_image.sh /home/pi/photobooth_images/shot' + str(snap) + '.jpg')
      subprocess.call('./process_image.sh')
      redled.off()
      camera.start_preview()
    redled.on()
    camera.annotate_text = "MERCI !!!"
    camera.stop_preview()
    subprocess.call('./assemble.sh')
    redled.off()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    destroy()
