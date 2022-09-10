from tkinter import *
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage




# Adding functions
def output(receiver):

    #txt1.delete('0', 'end-1c')
    txt1.insert(0,receiver)


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
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
    'a': 'deepak474700@gmail.com',
    'don': 'donvellathottam9@gmail.com',
    'my': 'athullyamol17@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    output(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


# main Screen

win = Tk()
win.title('Email Assistant')
win.geometry('600x500')


# Adding Elements to the Window

# heading
h1 = Label(win, text="Email Assistant With Speech Recognition", font=('Times new Roman', 20))
h1.grid(row=1, column=0)
h1.place(x=80, y=40)

# Label For enter Email
To = Label(win, text="To", font=('Times new Roman', 15))
To.grid()
To.place(x=150, y=130)
txt1 = Entry(win, width=50)
txt1.place(x=200, y=130)
sub = Label(win, text="Subject", font=('Times new Roman', 15))
sub.grid()
sub.place(x=150, y=130)
txt2 = Entry(win, width=50)
txt2.place(x=200, y=130)
get_email_info()



win.mainloop()






