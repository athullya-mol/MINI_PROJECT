from tkinter import *
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage



app = Tk()

listener = sr.Recognizer()
engine = pyttsx3.init()

app.geometry("500x500")

app.title("Email Assistant")

heading = Label(text="Email Assistant With Speech Recognition ", bg="yellow", fg="black", font="10", width="500", height="3")

heading.pack()

statusvar = StringVar()
statusvar.set("Listening...")
sbar = Label(app, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

address_field = Label(text="Recipient Address :")
subject_field = Label(text="Subject :")
body_field = Label(text="Message :")

address_field.place(x=15, y=80)
subject_field.place(x=15, y=150)
body_field.place(x=15, y=250)

address = StringVar()
sub = StringVar()
body = StringVar()

address_entry = Entry(textvariable=address, width="50")
subject_entry = Entry(textvariable=sub, width="50")
body_entry = Entry(textvariable=body, width="50")

address_entry.place(x=15, y=110, height=20)
subject_entry.place(x=15, y=180, height=40)
body_entry.place(x=15, y=280, height=100)

button2 = Button(app, text="Clear", width=30, height=2, bg="grey")
button2.place(x=15, y=410)
#button2.invoke()
button1 = Button(app, text="Send Message" , width="30", height="2", bg="grey")
button1.place(x=15, y=440)

# app.after(1000, get_email_info)

if(address_entry.focus()):
    print("address")
if(subject_entry.focus()):
    print("subject")
if(body_entry.focus()):
    print("body")
mainloop()






