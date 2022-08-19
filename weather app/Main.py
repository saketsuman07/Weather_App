from cgitb import text
import json
from logging import root
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import pytz
import requests
from PIL import Image, ImageTk


root = Tk()
root.title("Weather App")
root.geometry("890x470+100+100")
# root.configure(bg="")
bk_img = ImageTk.PhotoImage(file = "Images/bg_3.png")
bk_img_label = Label(root,image= bk_img)
bk_img_label.place(x=0, y=0)
root.resizable(False, False)

def getweather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    Timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}° / {round(location.longitude,4)}°")

    # home = pytz.timezone(result)
    # local_time = datetime.now(home)
    # current_time = local_time.strftime("%I:%M:%p")
    # clock.config(text=current_time)

    # weather
    api_key = "1df75e289146bf8214ea82e4bf521acf"
    api = f"https://api.openweathermap.org/data/2.5/onecall?lat={location.latitude}&lon={location.longitude}&units=metric&exclude=hourly&appid={api_key}"

    json_data = requests.get(api).json()

    # current
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']
    print(temp,humidity,pressure,wind,description)


    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=(description))

    # first cell
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']
    photo1 = ImageTk.PhotoImage(file=f"icons/{firstdayimage}.png")
    firstimage.config(image=photo1)
    firstimage.image = photo1

    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']
    day1_temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")

    # second cell
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']
    img = (Image.open(f"icons/{seconddayimage}.png"))
    resized_image = img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image = photo2

    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']
    day2_temp.config(text=f"Day:{tempday2}\n Night:{tempnight2}")

    # third cell
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']
    img = (Image.open(f"icons/{thirddayimage}.png"))
    resized_image = img.resize((50,50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3

    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']
    day3_temp.config(text=f"Day:{tempday3}\n Night:{tempnight3}")

    # fourth cell
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']
    img = (Image.open(f"icons/{fourthdayimage}.png"))
    resized_image = img.resize((50,50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']
    day4_temp.config(text=f"Day:{tempday4}\n Night:{tempnight4}")

    # fifth cell
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
    img = (Image.open(f"icons/{fifthdayimage}.png"))
    resized_image = img.resize((50,50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']
    day5_temp.config(text=f"Day:{tempday5}\n Night:{tempnight5}")

    # sixth cell
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']
    img = (Image.open(f"icons/{sixthdayimage}.png"))
    resized_image = img.resize((50,50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']
    day6_temp.config(text=f"Day:{tempday6}\n Night:{tempnight6}")

    # seventh cell
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']
    img = (Image.open(f"icons/{seventhdayimage}.png"))
    resized_image = img.resize((50,50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image = photo7

    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']
    day7_temp.config(text=f"Day:{tempday7}\n Night:{tempnight7}")


    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))






# -----------    icons    ---------------
image_icon = PhotoImage(file="Images/logo2.png")
root.iconphoto(False,image_icon)

Round_box = PhotoImage(file="images/BOX.png")
Label(root, image=Round_box).place(x=30, y=110)

# -------------- Labels ------------------------

label1 = Label(root,text="Temperature",font=('Helvatica',10),fg="white",bg="black")
label1.place(x=50, y=120)

label2 = Label(root,text="Humidity",font=('Helvatica',10),fg="white",bg="black")
label2.place(x=50, y=140)

label3 = Label(root,text="Pressure",font=('Helvatica',10),fg="white",bg="black")
label3.place(x=50, y=160)

label4 = Label(root,text="Wind Speed",font=('Helvatica',10),fg="white",bg="black")
label4.place(x=50, y=180)

label5 = Label(root,text="Description",font=('Helvatica',10),fg="white",bg="black")
label5.place(x=50, y=200)


# -------------Searchimage.png Box------------------
search_img = PhotoImage(file="Images/Search_btn.png")
my_img = Label(image=search_img,bg="#8d8d8d")
my_img.place(x=405,y=127)


weat_image = ImageTk.PhotoImage(file="Images/drops.jpg")
weather_image = Label(root,image=weat_image, bg="black")
weather_image.place(x=413, y=131)

textfield = tk.Entry(root,justify="center",width=15, font=('poppins',20,"bold"),bg="black",border=0,fg="white")
textfield.place(x=485,y=137)
textfield.focus()


search_icon = PhotoImage(file="Images/btn1.png")
my_icon = Button(image=search_icon, borderwidth=0,cursor="hand2",bg="black",command=getweather)
my_icon.place(x=690,y=129)

# _________________Bottom Box___________
frame = Frame(root,width=900,height=180)
frame.pack(side=BOTTOM)

# ,bg="#212120"

# bottom boxes
firstbox = PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Images/Rounded Rectangle 2 copy.png")
Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=400,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=500,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=700,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=800,y=30)

# clock(place time here)
# clock = Label(root,font=("Helvatica",20,"bold"), fg="black",bg="#F0F0F0")  
# clock.place(x=15,y=15)

# timezone
Timezone = Label(root,font=("Helvatica",16,"bold"), fg="white",bg="#808080")
Timezone.place(x=650,y=15)

long_lat = Label(root,font=("Helvatica",10,"bold"), fg="white",bg="#808080")
long_lat.place(x=650,y=45)

# thpwd
t = Label(root,font=('Helvatica',10),fg="white",bg="black")
t.place(x=150,y=120)
h = Label(root,font=('Helvatica',10),fg="white",bg="black")
h.place(x=150,y=140)
p = Label(root,font=('Helvatica',10),fg="white",bg="black")
p.place(x=150,y=160)
w = Label(root,font=('Helvatica',10),fg="white",bg="black")
w.place(x=150,y=180)
d = Label(root,font=('Helvatica',10),fg="white",bg="black")
d.place(x=150,y=200)

# first cell
firstframe = Frame(root,width=230,height=132,bg="#282829")
firstframe.place(x=35,y=315)

day1 = Label(firstframe,font=("arial",20),bg="#282829",fg="#fff")
day1.place(x=110,y=5)

firstimage = Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)

day1_temp = Label(firstframe,bg="#282829",fg="#57adff",font="arial 15 bold")
day1_temp.place(x=98,y=50)

# second cell
secondframe = Frame(root,width=70,height=115,bg="#282829")
secondframe.place(x=305,y=325)

day2 = Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=10,y=5)

secondimage = Label(secondframe,bg="#282829")
secondimage.place(x=7,y=23)

day2_temp = Label(secondframe,bg="#282829",fg="#fff")
day2_temp.place(x=10,y=70)

# third cell
thirdframe = Frame(root,width=70,height=115,bg="#282829")
thirdframe.place(x=405,y=325)

day3 = Label(thirdframe,bg="#282829",fg="#fff")
day3.place(x=10,y=5)

thirdimage = Label(thirdframe,bg="#282829")
thirdimage.place(x=7,y=23)

day3_temp = Label(thirdframe,bg="#282829",fg="#fff")
day3_temp.place(x=10,y=70)

# fourth cell
fourthframe = Frame(root,width=70,height=115,bg="#282829")
fourthframe.place(x=505,y=325)

day4 = Label(fourthframe,bg="#282829",fg="#fff")
day4.place(x=10,y=5)

fourthimage = Label(fourthframe,bg="#282829")
fourthimage.place(x=7,y=23)

day4_temp = Label(fourthframe,bg="#282829",fg="#fff")
day4_temp.place(x=10,y=70)

# fifth cell
fifthframe = Frame(root,width=70,height=115,bg="#282829")
fifthframe.place(x=605,y=325)

day5 = Label(fifthframe,bg="#282829",fg="#fff")
day5.place(x=10,y=5)

fifthimage = Label(fifthframe,bg="#282829")
fifthimage.place(x=7,y=23)

day5_temp = Label(fifthframe,bg="#282829",fg="#fff")
day5_temp.place(x=10,y=70)

# sixth cell
sixthframe = Frame(root,width=70,height=115,bg="#282829")
sixthframe.place(x=705,y=325)

day6 = Label(sixthframe,bg="#282829",fg="#fff")
day6.place(x=10,y=5)

sixthimage = Label(sixthframe,bg="#282829")
sixthimage.place(x=7,y=23)

day6_temp = Label(sixthframe,bg="#282829",fg="#fff")
day6_temp.place(x=10,y=70)

# seventh cell
seventhframe = Frame(root,width=70,height=115,bg="#282829")
seventhframe.place(x=805,y=325)

day7 = Label(seventhframe,bg="#282829",fg="#fff")
day7.place(x=10,y=5)

seventhimage = Label(seventhframe,bg="#282829")
seventhimage.place(x=7,y=23)

day7_temp = Label(seventhframe,bg="#282829",fg="#fff")
day7_temp.place(x=10,y=70)


root.mainloop()