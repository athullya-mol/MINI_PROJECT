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
    address_entry.insert(0,receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    app.after(1000, get_email_info)

app.geometry("500x500")

app.title("Python Mail Send App")

heading = Label(text="Python Email Sending App", bg="yellow", fg="black", font="10", width="500", height="3")

heading.pack()

statusvar = StringVar()
statusvar.set("Listening...")
sbar = Label(app, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

address_field = Label(text="Recipient Address :")
email_body_field = Label(text="Message :")

address_field.place(x=15, y=70)
email_body_field.place(x=15, y=140)

address = StringVar()
email_body = StringVar()

address_entry = Entry(textvariable=address, width="50")
email_body_entry = Entry(textvariable=email_body, width="50")

address_entry.place(x=15, y=100)
email_body_entry.place(x=15, y=180)

button = Button(app, text="Send Message", command=send_email, width="30", height="2", bg="grey")

button.place(x=15, y=220)

app.after(1000, get_email_info)
mainloop()
