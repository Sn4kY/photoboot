# Photobooth

How I build my PhotoBooth for my wedding.

Build with (and for...)
* Raspberry Pi 3
* Official touchscreen display 7"
* Official camera
* Canon Selphy CP1200
- Arm Oil
- Python & bash scripting
- 3 LEDs
- 1 push button
- Home made black painted wood box

## Getting Started

These instructions will get you a copy of this wonderful project up and running on your RaspPi.

### Prerequisites

* [Official Raspberry Pi Camera](https://www.raspberrypi.org/products/camera-module-v2/)
* [Official Raspberry Pi touchscreen display 7"](https://www.raspberrypi.org/products/raspberry-pi-touch-display/)
* Raspbian installed and working (SSH is highly recommended)
* Cups with working printer. I used a Canon Selphy CP1200 with CP900 drivers.

### Installing

Clone the project
```
git clone https://github.com/Sn4kY/photobooth.git
cd photobooth/
```
Create one directory in the rootdir of your copy. It will be used to store the pictures, and the final printed render
```
mkdir archives/
```

Install some Linux Raspbian, and python specific for Raspberry Pi :
```
sudo apt-get install fbi python python-picamera python-gpiozero imagemagick
```

Wire and then enable camera (a reboot is required to enable it)
```
sudo raspi-config
```

Build the electrical circuit
* Red LED with 560 ohms resistor to pin 15 (GPIO 22) and ground
* Blue LED with 1K ohms resistor to pin 23 (GPIO 11) and gnd
* Green LED with 220 ohms resistor to pin 19 (GPIO 10) and gnd

(Please adjust resistor values with the need of the LED you used and the brightness you need)
* Button to pin 11 (GPIO 17) and gnd

All GND could be wired together

### Configuring
Create a label (1090x334 px @ 300dpi) : photobooth_label.jpg, and upload it to the "res/" directory (an example is provided)

### Run & Enjoy
```
./photobooth.py
```
