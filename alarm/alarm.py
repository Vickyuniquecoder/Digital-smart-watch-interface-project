from ctypes import alignment
from email.mime import image
import textwrap
from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import time
import datetime
import threading
from token import RIGHTSHIFT
import turtle
from pygame import mixer
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import requests
import pytz
import os
import math

root= Tk()
root.title("Alarm")
root.geometry("1920x1080")


root.configure(background='black')
def click(event):
	text=event.widget.cget("text")
	print(text)
	if text=="=":
		if scvalue.get().isdigit():
			value=int(scvalue.get())
		else:
			try:
			    value=eval(screen.get())
			except Exception as e:
				  print(e)
				  value="Error"
		scvalue.set(value)
		screen.update()		  


			
	elif text=="C":
		scvalue.set("")
		screen.update()
	else:
		scvalue.set(scvalue.get()+text)
		screen.update()




scvalue=StringVar()
scvalue.set("")
head =Label(root,text="CALCULATOR",font=('comic sans',20))
head.place(x=160,y=10)
screen=Entry(root,textvar=scvalue,font="lucida 25 bold")
screen.place(x=80,y=60)

f=Frame(root,bg="grey")
b=Button(f,text="9",padx=10,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=10,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=10,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

f.place(x=185,y=110)




f=Frame(root,bg="grey")
b=Button(f,text="6",padx=10,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=10,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=10,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

f.place(x=185,y=152)






f=Frame(root,bg="grey")
b=Button(f,text="3",padx=10,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=10,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

b=Button(f,text="1",padx=10,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

f.place(x=185,y=194)





f=Frame(root,bg="grey")
b=Button(f,text="0",padx=10,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=12,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=11,pady=5,font="lucida 13 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

f.place(x=185,y=236)






f=Frame(root,bg="grey")
b=Button(f,text="/",padx=12,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

b=Button(f,text="%",padx=7,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=10,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

f.place(x=185,y=278)






f=Frame(root,bg="grey")
b=Button(f,text="C",padx=8,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

b=Button(f,text=" . ",padx=8,pady=5,font="lucida 13 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

b=Button(f,text="00",padx=5,pady=5,font="lucida 12 bold")
b.pack(side=LEFT,padx=1,pady=1)
b.bind("<Button-1>",click)

f.place(x=185,y=320)















mixer.init()

def th():
	t1 = threading.Thread(target=a, args=())
	t1.start()


def a():

	a = hr.get()
	if a == "":
		msg = messagebox.showerror('Invalid data','Please enter valid time')
	else:
		Alarmtime= a
		CurrentTime = time.strftime("%H:%M")

		while Alarmtime != CurrentTime:
			CurrentTime = time.strftime("%H:%M")
			
		if Alarmtime == CurrentTime:
			mixer.music.load('tone.mp3')
			mixer.music.play()
			msg = messagebox.showinfo('It is time',f'{amsg.get()}')
			if msg == 'ok':
				mixer.music.stop()



header =Frame(root)
header.place(x=5,y=5)

head =Label(root,text="ALARM CLOCK",font=('comic sans',20))
head.place(x=150,y=377)
#head.pack(fill=Y,padx=670,pady=0)

panel = Frame(root)
panel.place(x=0,y=425)
alpp = PhotoImage(file='ramit.png')
alp = Label(panel,image=alpp)
alp.grid(rowspan=4,column=0)

alppp=PhotoImage(file='dial.png')
rc = Label(root,image=alppp)
rc.place(x=540,y=50)

atime = Label(panel,text="Alarm Time \n(Hr:Min)",font=('comic sans',18))
atime.grid(row=0,column=1,padx=10,pady=5)

hr = Entry(panel,font=('comic sans',20),width=6)
hr.grid(row=0,column=2,padx=10,pady=5)

amessage = Label(panel,text="Message",font=('comic sans',20))
amessage.grid(row=1,column=1,columnspan=2,padx=10,pady=5)

amsg = Entry(panel,font=('comic sans',15),width=25)
amsg.grid(row=2,column=1,columnspan=2,padx=10,pady=5)


start = Button(panel,text="Start alarm",font=('comic sans',20),command=th)
start.grid(row=3,column=1,columnspan=2,padx=10,pady=5)


#music player



def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()    


mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#playlist---------------

playlist=Listbox(root,selectmode=SINGLE,bg="#ffff40",fg="blue",font=('arial',15),width=60)
playlist.place(x=1000,y=55)

os.chdir(r'C:\Users\Dell\Documents\auto call record')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

head =Label(root,text="Music Player",font=('comic sans',20))
head.place(x=1190,y=10)

playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=28,pady=7)
playbtn.place(x=1000,y=300)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=18,pady=7)
pausebtn.place(x=1132,y=300)

stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=26,pady=7)
stopbtn.place(x=1268,y=300)

Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
Resumebtn.place(x=1400,y=300)




#analog watch


def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))
    # updating seconds hand
    seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)
    # updating minutes hand
    minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    # updating hours hand
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30)) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30)) + center_y
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    root.after(1000, update_clock)
canvas = Canvas(root, width=200, height=200,bd=0)
canvas.configure(bg='black',highlightbackground='black',highlightthickness=3)
canvas.place(x=640,y=150)

head =Label(root,text="CLOCK",font=('comic sans',20))
head.place(x=700,y=10)
# create background
#alppp = PhotoImage(file="dial.png",name="dial")
#canvas.create_image(200, 200, image=alppp)
# create clock hands
# seconds hand
center_x = 100
center_y = 105
seconds_hand_len = 100
minutes_hand_len = 100
hours_hand_len = 60
seconds_hand = canvas.create_line(200, 200, 200 + seconds_hand_len, 200 + seconds_hand_len, width=1.5, fill='red')
# minutes hand
minutes_hand = canvas.create_line(200, 200, 200 + minutes_hand_len, 200 + minutes_hand_len, width=2, fill='white')
# hours hand
hours_hand = canvas.create_line(200, 200, 200 + hours_hand_len, 200 + hours_hand_len, width=4, fill='white')
update_clock()
root.mainloop()