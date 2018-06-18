#!/bin/bash
DATE=$(date +%Y-%m-%d-%H-%M-%S)

sudo killall fbi
sudo fbi -a --noverbose -T 1 /tmp/shot.jpg
sleep 1
#convert -resize 125x147 -gravity center /home/pi/photobooth_images/shot.jpg /home/pi/temp/photobooth-${DATE}.jpg
# Adding dpi to 300 to fit printer characteristics
#convert -density 300 -resize 520x612 -gravity center /home/pi/photobooth_images/shot.jpg /home/pi/temp/photobooth-${DATE}.jpg
# Adding flip image vertically
convert -density 300 -resize 520x602 -gravity center -flop /tmp/shot.jpg /tmp/photobooth-${DATE}.jpg
mv /tmp/shot.jpg archives/shot_${DATE}.jpg
sudo killall fbi
