#!/bin/bash
DATE=$(date +%Y-%m-%d-%H-%M-%S)

sudo killall fbi
montage /tmp/photobooth-*.jpg -tile 2x2 -border 5 -geometry +10+10 -density 300 -units PixelsPerInch /tmp/montage2.jpg
sudo  fbi -a --noverbose -T 1 /tmp/montage2.jpg
montage /tmp/montage2.jpg res/photobooth_label.jpg -tile 1x2 -geometry +5+5 -density 300 -units PixelsPerInch /tmp/montage3.jpg
montage /tmp/montage3.jpg -border 35 -bordercolor "#ffffff" -density 300 -units PixelsPerInch -geometry +0+0 /tmp/montage4.jpg
#lp -d Canon_SELPHY_CP1200 /tmp/montage4.jpg
mv -f /tmp/montage4.jpg archives/pb_${DATE}.jpg
rm -vf /tmp/*.jpg
sleep 60
sudo killall fbi
