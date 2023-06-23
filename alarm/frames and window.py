from tkinter import *
from ctypes import alignment
from email.mime import image
import textwrap
from tkinter import ttk,messagebox,filedialog
import tkinter as tk
import time
from time import strftime
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
from PIL import Image,ImageTk
import sounddevice as sound
from scipy.io.wavfile import write
import wavio as wv
import soundfile as sf
import queue
from threading import Thread
import sounddevice as sd
from datetime import datetime



root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
#root.state('zoomed')
root.geometry("620x450")

page1 = Frame(root)
page2 = Frame(root)
page3 = Frame(root)
page4 = Frame(root)
page5 = Frame(root)
page6 = Frame(root)

for frame in (page1, page2, page3,page4,page5,page6):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(page1)

# ============= Page 1 =========
#pag1_label = Label(page1, font=('Arial', 15, 'bold'))
#pag1_label.place(x=50, y=100)
page1.config(background='black')

def clock_date():
	display_date=strftime('%B-%A-%d-%Y')
	Date.config(text=display_date)
	Date.after(1000,clock_date)

def clock_Time():
	display_time=strftime("%H:%M:%S %p")
	Time.config(text=display_time)
	Time.after(1000,clock_Time)

Date=Label(page1,font=('ds-digital',15),background="black",foreground="cyan")
Date.place(x=60,y=60)
Date.config(padx=(75),pady=(30))

Time=Label(page1,font=('ds-digital',60),background="black",foreground="cyan")
Time.place(x=20,y=114)
Time.config(pady=(50))
clock_date()
clock_Time()



pg1_button = Button(page1, text='>>>', font=('Arial', 13, 'bold'),bg='black',fg='cyan' ,command=lambda: show_frame(page2))
pg1_button.place(x=525, y=200)


pg1_button = Button(page1, text='<<<', font=('Arial', 13, 'bold'),bg='black',fg='cyan' ,command=lambda: show_frame(page6))
pg1_button.place(x=573, y=200)


#pag1_entry = Entry(page1)
#pag1_entry.place(x=170, y=106)

#pag1_label2 = Label(page1, font=('Arial', 15, 'bold'))
#pag1_label2.place(x=50, y=150)

#pag1_entry2 = Entry(page1)
#pag1_entry2.place(x=170, y=155)










# ======== Page 2 ===========

page2.config(background='black')
#pag2_label = Label(page2, font=('Arial', 30, 'bold'))
#pag2_label.place(x=50, y=100)


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



#header =Frame(root)
#header.place(x=5,y=5)

pag2 =Label(page2,text="ALARM CLOCK",font=('comic sans',20))
pag2.place(x=160,y=10)
#head.pack(fill=Y,padx=670,pady=0)

panel = Frame(page2,bg='black')
panel.place(x=0,y=50)
alpp = PhotoImage(file='ramit.png')
alp = Label(panel,image=alpp)
alp.grid(rowspan=4,column=0)

#alppp=PhotoImage(file='dial.png')
#rc = Label(page1,image=alppp)
#rc.place(x=50,y=10)

atime = Label(panel,text="Alarm Time \n(Hr:Min)",font=('comic sans',18),fg='blue',bg='black')
atime.grid(row=0,column=1,padx=10,pady=5)

hr = Entry(panel,font=('comic sans',20),width=6,fg='blue',bg='black')
hr.grid(row=0,column=2,padx=10,pady=5)

amessage = Label(panel,text="Message",font=('comic sans',20),fg='blue',bg='black')
amessage.grid(row=1,column=1,columnspan=2,padx=10,pady=5)

amsg = Entry(panel,font=('comic sans',15),width=25,fg='blue',bg='black')
amsg.grid(row=2,column=1,columnspan=2,padx=10,pady=5)


start = Button(panel,text="Start alarm",font=('comic sans',20),command=th,fg='blue',bg='black')
start.grid(row=3,column=1,columnspan=2,padx=10,pady=5)


pg2_button = Button(page2, text='>>>', font=('Arial', 13, 'bold'),bg='black',fg='blue', command=lambda: show_frame(page3))
pg2_button.place(x=525, y=200)



pg2_button = Button(page2, text='<<<', font=('Arial', 13, 'bold'),bg='black',fg='cyan' ,command=lambda: show_frame(page1))
pg2_button.place(x=573, y=200)



# ======== Page 3 ===========
page3.config(background='black')
#pag3_label = Label(page3, font=('Arial', 30, 'bold'))
#pag3_label.place(x=50, y=100)

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

playlist=Listbox(page3,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),width=45)
playlist.place(x=0,y=50)

#os.chdir(r'C:\Users\dell\Desktop\songs')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

head =Label(page3,text="Music Player",font=('comic sans',20))
head.place(x=160,y=10)

playbtn=Button(page3,text="Play",command=playsong)
playbtn.config(font=('arial',20),bg="black",fg="cyan",padx=24,pady=7)
playbtn.place(x=0,y=295)

pausebtn=Button(page3,text="Pause",command=pausesong)
pausebtn.config(font=('arial',20),bg="black",fg="cyan",padx=15,pady=7)
pausebtn.place(x=122,y=295)

stopbtn=Button(page3,text="Stop",command=stopsong)
stopbtn.config(font=('arial',20),bg="black",fg="cyan",padx=24,pady=7)
stopbtn.place(x=250,y=295)

Resumebtn=Button(page3,text="Resume",command=resumesong)
Resumebtn.config(font=('arial',20),bg="black",fg="cyan",padx=1,pady=7)
Resumebtn.place(x=376,y=295)

pg3_button = Button(page3, text='>>>', font=('Arial', 13, 'bold'), command=lambda: show_frame(page4))
pg3_button.place(x=525, y=200)


pg3_button = Button(page3, text='<<<', font=('Arial', 13, 'bold'),bg='black',fg='cyan' ,command=lambda: show_frame(page2))
pg3_button.place(x=573, y=200)


# ======== Page 4 ===========

page4.config(background='black')


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
head =Label(page4,text="CALCULATOR",font=('comic sans',20))
head.place(x=160,y=10)
screen=Entry(page4,textvar=scvalue,font="lucida 25 bold")
screen.place(x=80,y=60)

f=Frame(page4,bg="grey")
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




f=Frame(page4,bg="grey")
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






f=Frame(page4,bg="grey")
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





f=Frame(page4,bg="grey")
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






f=Frame(page4,bg="grey")
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






f=Frame(page4,bg="grey")
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

pg4_button = Button(page4, text='>>>', font=('Arial', 13, 'bold'),bg='black',fg='white', command=lambda: show_frame(page5))
pg4_button.place(x=525, y=200)



pg4_button = Button(page4, text='<<<', font=('Arial', 13, 'bold'),bg='black',fg='cyan' ,command=lambda: show_frame(page3))
pg4_button.place(x=573, y=200)



# ======== Page 5 ===========

page5.config(background='black')

def showimage():
	filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",filetype=(("JPG File","*.jpg"),("PNG file","*.png"),("All file","how are you.txt")))
	img=Image.open(filename)
	img=ImageTk.PhotoImage(img)
	lbl.configure(image=img)
	lbl.image=img
fram=Frame(page5)
fram.place(x=10,y=10)
lbl=Label(page5)
lbl.place(x=10,y=10)

btn=Button(page5,text="Select Image",command=showimage)
btn.place(x=500,y=720)

btn2=Button(page5,text="Exit",command=lambda:exit())
btn2.place(x=580,y=720)

pg5_button = Button(page5, text='>>>', font=('Arial', 13, 'bold'), bg='black',fg='blue',command=lambda: show_frame(page6))
pg5_button.place(x=525, y=200)


pg5_button = Button(page5, text='<<<', font=('Arial', 13, 'bold'),bg='black',fg='cyan' ,command=lambda: show_frame(page4))
pg5_button.place(x=573, y=200)

# ======== Page 6 ===========

page6.config(background='black')

class Record:
	def __init__(self, can_record):
		self.can_record = can_record
		self.queue = queue.Queue()

class TempLabel:
	def __init__(self, label):
		self.label = label

l = TempLabel(None)
r = Record(True)

def recordStart():
	with sf.SoundFile(str(datetime.now()).replace(":", "-")+".wav", mode='x', samplerate=16000, channels=2) as file:
		with sd.InputStream(samplerate=16000, channels=2, callback=callback):
			while r.can_record:
				file.write(r.queue.get())

def callback(indata, frames, time, status):
    r.queue.put(indata.copy())

def record():
	l.label = Label(page6, text="Recording...", font=("Comic Sans MS", 10))
	l.label.pack()
	l.label.place(x=150, y=160)
	l2.configure(text="Stop")
	l2.configure(command=stop)
	t = Thread(target=recordStart).start()


def stop():
	r.can_record = not r.can_record
	l.label.destroy()
	l2.configure(text="Record")
	l2.configure(command=record)

l = Label(page6, text="Sound Recorder", font=("Comic Sans MS", 22))
l.pack()

l2 = Button(page6, text="Record", font=("Arial", 16), command=record)
l2.pack()
l2.place(x=185, y=100, anchor="center")




pg6_button = Button(page6, text='>>>', font=('Arial', 13, 'bold'), bg='black',fg='blue',command=lambda: show_frame(page1))
pg6_button.place(x=525, y=200)



pg6_button = Button(page6, text='<<<', font=('Arial', 13, 'bold'),bg='black',fg='cyan' ,command=lambda: show_frame(page5))
pg6_button.place(x=573, y=200)



root.mainloop()