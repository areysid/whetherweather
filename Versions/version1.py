from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root=Tk()
root.title("WhetherWeather")
root.geometry("900x500+300+200")
root.resizable(False,False)
#root.config(bg="light blue")
root.config(bg="light green")


def getWeather():
    city=textfield.get()
    geolocator= Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude, lat=location.latitude)
    print(result)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time,bg="light green")
    name.config(text="CURRENT WEATHER",bg="light blue")
    clk.config(text="CURRENT TIME",bg="light blue")
    

    #weather
    api="https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=068db937946d13af4fef57bcf43fe739"

    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=float(json_data['main']['pressure'])
    humidity=float(json_data['main']['humidity'])
    wind=json_data['wind']['speed']

    t.config(text=(temp,"°"),bg="light green")
    c.config(text=(condition, "|", "FEELS", "LIKE", temp,"°"),bg="light green")

    w.config(text=(wind))
    h.config(text=(humidity))
    d.config(text=(description))
    p.config(text=(pressure))
    

#search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image,bg="light green")
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center", width=20,font=("Sitka Small",20),bg="white",border=0,fg="Black")
textfield.place(x=55,y=40)
textfield.focus()


Search_icon=PhotoImage(file="search2.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040", command=getWeather)
myimage_icon.place(x=380,y=39)


#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image,bg="light green")
logo.place(x=150,y=140)

#bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image,bg="light green")
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"),bg="light green")
name.place(x=400,y=120)
clk=Label(root,font=("arial",15,"bold"),bg="light green")
clk.place(x=30,y=100)
clock=Label(root, font=("Helvetica",20),bg="light green")
clock.place(x=30,y=130)

#label

label1=Label(root, text="WIND", font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label1=Label(root, text="HUMIDITY", font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=250,y=400)

label1=Label(root, text="DESCRIPTION", font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=430,y=400)

label1=Label(root, text="PRESSURE", font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=650,y=400)


t=Label(font=("arial",70,"bold"), fg="#ee666d",bg="light green")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"),bg="light green")
c.place(x=400,y=250)

w=Label(text="...",font=("roboto",18,"bold"),bg="#1ab5ef")
w.place(x=125,y=430)
h=Label(text="...",font=("roboto",18,"bold"),bg="#1ab5ef")
h.place(x=270,y=430)
d=Label(text="...",font=("roboto",18,"bold"),bg="#1ab5ef")
d.place(x=430,y=430)
p=Label(text="...",font=("roboto",18,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)













root.mainloop()
              
