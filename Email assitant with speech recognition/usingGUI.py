from tkinter import *
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

app = Tk()

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            statusvar.set(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('twilightwacky272@gmail.com', 'vbbolbhkqlgnkvjm')
    email = EmailMessage()
    email['From'] = 'twilightwacky272@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    talk('Can I send this message?')
    res = get_info()
    if 'yes' in res:
        server.send_message(email)
    else:
        talk('Is there any changes to make!')


email_list = {
    'rj': 'rjajesh272@gmail.com',
    'deep': 'deepak474700@gmail.com',
    'don': 'donvellathottam9@gmail.com',
    'my': 'athullyamol17@gmail.com'
}

def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    address_entry.insert(0, receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    subject_entry.insert(0, subject)
    talk('Tell me the text in your email')
    message = get_info()
    body_entry.insert(0, message)
    send_email(receiver, subject, message)
    talk('Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    app.after(1000, get_email_info)

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

address_field.place(x=15, y=70)
subject_field.place(x=15, y=140)
body_field.place(x=15, y=240)

address = StringVar()
sub = StringVar()
body = StringVar()

address_entry = Entry(textvariable=address, width="50")
subject_entry = Entry(textvariable=sub, width="50")
body_entry = Entry(textvariable=body, width="50")

address_entry.place(x=15, y=100, height=20)
subject_entry.place(x=15, y=180, height=40)
body_entry.place(x=15, y=280, height="100")

button = Button(app, text="Send Message", command=send_email, width="30", height="2", bg="grey")

button.place(x=15, y=400)

app.after(1000, get_email_info)
mainloop()
