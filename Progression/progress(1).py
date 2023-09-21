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
#root.configure(bg="white")

#search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center", width=17,font=("Times New Roman",25,"bold"),bg="light blue",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()


Search_icon=PhotoImage(file="sww.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="light blue")
myimage_icon.place(x=400,y=34)





root.mainloop()
              

