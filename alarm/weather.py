#weather 

def getWeather():
	city=textfield.get()

	geolocator=Nominatim(user_agent="geoapiExercises")
	location=geolocator.geocode(city)
	obj=TimezoneFinder()
	result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

	home=pytz.timezone(result)
	local_time=datetime.now(home)
	current_time=local_time.strftime("%I:%M %p")
	clock.config(text=current_time)
	name.config(text="CURRENT WEATHER")


	#weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"fappid=8e354a26e5a75994c8ef080c46728c2"
	json_data=requests.get(api).json()
	condition=json_data['weather'][0]['main']
	description=json_data['weather'][0]['description']
	temp=int(json_data['main']['temp']-273.15)
	pressure=json_data['main']['pressure']
	humidity=json_data['main']['humidity']
	wind=json_data['wind']['speed']
	t.config(text=(temp,"°"))
	c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))






#search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=780,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=820,y=40)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=1155,y=34)

#logo

Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=750,y=115)

#bottom box

Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.place(x=750,y=370)
#frame_myimage.pack(padx=10,pady=10)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=1500,y=0)
clock=Label(root,font=("Helvetica",20))
clock.place(x=1300,y=20)


#label

label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=800,y=390)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=950,y=390)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=1150,y=390)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=1370,y=390)


T=Label(font=("arial",70,"bold"),fg="#ee666d")
T.place(x=800,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=850,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=800,y=420)


h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=980,y=420)


d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=1180,y=420)


p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=1380,y=420)