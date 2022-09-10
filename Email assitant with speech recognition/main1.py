import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

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
    'deep': 'deepak474700@gmail.com',
    'don': 'donvellathottam9@gmail.com',
    'my': 'athullyamol17@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
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


get_email_info()
