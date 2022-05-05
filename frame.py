from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk

mywindow = Tk()
mywindow.geometry("300x300")
mywindow.title("Game")

frame1 = Frame(mywindow)
frame1.pack(side="left")

frame2 = Frame(mywindow)
frame2.pack(side="right")

label1 = Label(frame1, text="RSTForum")
label1.pack()

image = Image.open("download1.png")
resize_image=image.resize((200,200))

img = ImageTk.PhotoImage(resize_image)

#myimg = PhotoImage(file="download1.png")
label2 = Label(frame2)
label2["image"] = img
label2.pack(anchor= CENTER)


def func123():
    print(username.get())
    print(password.get())
    print(x.get())
    print(phone.get())
    print(day.get())


# BUTTON
button1 = Button(mywindow, fg="red", bg="black", text="submit", command=func123)
myimg2 = PhotoImage(file="download(1).png")
button1["image"] = myimg2
button1.pack(anchor= CENTER,side="bottom")

# ENTRYBOX
username = StringVar()
name = Entry(mywindow, textvariable=username)
name.pack(side="top")

password = StringVar()
pwd = Entry(mywindow, textvariable=password, show="*")
pwd.pack(side="top")

# CHECKBUTTON
x = StringVar()
mycheckbox = Checkbutton(
    mywindow, text="I Agree", variable=x, onvalue="yes", offvalue="no"
)
mycheckbox.pack()

# RADIOBUTTON
phone = StringVar()
home = Radiobutton(mywindow, text="Home", variable=phone, value=2212345678)
office = Radiobutton(mywindow, text="Office", variable=phone, value=22987654321)
mobile = Radiobutton(mywindow, text="Mobile", variable=phone, value="+91123123456456")

home.pack()
office.pack()
mobile.pack()


# DROPDOWN Menu
day = StringVar()
dropdown = Combobox(
    mywindow,
    textvariable=day,
    values=[
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ],
)
dropdown.pack()


mywindow.mainloop()