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
#root.configure(bg="white")



#search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center", width=20,font=("Sitka Small",20),bg="white",border=0,fg="Black")
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

t=Label(font=("arial",70,"bold"), fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)




root.mainloop()
              

