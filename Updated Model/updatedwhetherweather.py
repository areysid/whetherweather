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
root.geometry("900x500+0+0")
root.resizable(False,False)
#root.config(bg="light blue")
#root.configure(bg="white")



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
    current_datetime = datetime.now(home)
    current_date = current_datetime.date()
    formatted_date = current_datetime.strftime("%d-%m-%Y")
    date.config(text=("Date:",formatted_date))
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
    clk.config(text="CURRENT TIME")

    #weather
    api="https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=068db937946d13af4fef57bcf43fe739"

    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=float(json_data['main']['pressure'])
    humidity=float(json_data['main']['humidity'])
    wind=json_data['wind']['speed']
    sunrise=json_data['sys']['sunrise']
    sunset=json_data['sys']['sunset']

    t.config(text=(temp,"°"))
    c.config(text=(condition, "|", "FEELS", "LIKE", temp,"°"))

    w.config(text=(wind))
    h.config(text=(humidity))
    d.config(text=(description.capitalize()))
    p.config(text=(pressure))

    #setting time
    """sunrise_time_utc = datetime.fromtimestamp(sunrise)
    sunrise_time_local = sunrise_time_utc.astimezone(home)
    formatted_sunrise_time = sunrise_time_local.strftime('%I:%M %p')
    sun.config(text=f"Sunrise: {formatted_sunrise_time}")"""
    '''dt_object = datetime.utcfromtimestamp(sunrise)
    dt_object_local=dt_object.astimezone(home)
    formatted_time = dt_object_local.strftime('%H:%M')
    sun.config(text=(formatted_time))'''
    sunrise_time_utc = datetime.fromtimestamp(sunrise)
    preferred_timezone = pytz.timezone(result)
    sunrise_time_local = sunrise_time_utc.astimezone(preferred_timezone)
    formatted_sunrise_time = sunrise_time_local.strftime('%I:%M %p')
    sun.config(text=f"Sunrise: {formatted_sunrise_time}")
    sunset_time=datetime.fromtimestamp(sunset)
    tz=pytz.timezone(result)
    sunset_time_local=sunset_time.astimezone(tz)
    formatted_sunset_time = sunset_time_local.strftime('%I:%M %p')
    sunt.config(text=f"Sunset: {formatted_sunset_time}")
    

#search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="left", width=20,font=("Sitka Small",20),bg="white",border=0,fg="Black")
textfield.place(x=55,y=40)
textfield.focus()


Search_icon=PhotoImage(file="search2.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040", command=getWeather)
myimage_icon.place(x=380,y=39)


#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=140)

#bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=400,y=120)
clk=Label(root,font=("arial",15,"bold"))
clk.place(x=30,y=100)
clock=Label(root, font=("Helvetica",20))
clock.place(x=30,y=130)
date=Label(root, font=("roboto",18,"bold"))
date.place(x=688,y=0)

#label

label1=Label(root, text="WIND", font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label1=Label(root, text="HUMIDITY", font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=250,y=400)

label1=Label(root, text="DESCRIPTION", font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=430,y=400)

label1=Label(root, text="PRESSURE", font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=650,y=400)


t=Label(font=("arial",70,"bold"), fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text=" ",font=("roboto",18,"bold"),bg="#1ab5ef")
w.place(x=125,y=430)
h=Label(text=" ",font=("roboto",18,"bold"),bg="#1ab5ef")
h.place(x=270,y=430)
d=Label(text=" ",font=("roboto",18,"bold"),bg="#1ab5ef")
d.place(x=430,y=430)
p=Label(text=" ",font=("roboto",18,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)
sun=Label(justify="right", text=" ",font=("roboto",18,"bold"),bg="#F0F0F0")
sun.place(x=680,y=45)
sunt=Label(justify="right", text=" ",font=("roboto",18,"bold"),bg="#F0F0F0")
sunt.place(x=685,y=75)












root.mainloop()
              

