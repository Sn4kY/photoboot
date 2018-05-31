#!/usr/bin/env python
from Tkinter import *
import tkFont
from picamera import PiCamera


camera = PiCamera()
camera.resolution = (1875, 2205)
camera.framerate = 15
camera.annotate_text_size = 100
camera.hflip = True

win = Tk()
win.overrideredirect(True)
#win['bg']='white'

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

def exitProgram():
	print("Exit Button pressed")
	win.quit()

#win.title("First GUI")
#win.geometry('480x800')
win.geometry("{0}x{1}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight()))

pbLabel = PhotoImage(file="res/photobooth_label.gif")
#canvas = Canvas(win,width=win.winfo_screenwidth(), height=win.winfo_screenheight(),background="white")
canvasTop = Canvas(win,width=480,height=120,background="white")
canvasTop.create_image(240, 0, anchor=N, image=pbLabel)
canvasTop.image = pbLabel
canvasBottom = Canvas(win,width=480,height=120,background="white")
canvasBottom.create_image(240, 0, anchor=N, image=pbLabel)
canvasBottom.image = pbLabel
canvasTop.pack(side=TOP)
canvasBottom.pack(side=BOTTOM)


text = Label(win, text="Bonjour !")
exitButton = Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6) 
text.pack()
exitButton.pack()

camera.start_preview()
win.mainloop()

