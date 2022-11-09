import speech_recognition as sr
import easyimap as e
import pyttsx3
import smtplib

unm = "twilightwacky272@gmail.com"
pwd = "vbbolbhkqlgnkvjm"

r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "Speak now:"
        speak(str)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "Sorry could not recognize what you said"
            speak(str)

email_list = {
    'rj': 'rjajesh272@gmail.com',
    'deep': 'deepak474700@gmail.com',
    'don': 'donvellathottam9@gmail.com',
    'my': 'athullyamol17@gmail.com'
}

def sendmail():

    str = "To Whom you want to send email"
    speak(str)
    name = listen()
    rec = email_list[name]
    str = "You want to send mail to"
    speak(str)
    speak(rec)

    str = "What is the subject of your email?"
    speak(str)
    sub = listen()
    str = "The subject of mail is"
    speak(str)
    speak(sub)

    str = "Tell me the text in your email"
    speak(str)
    msg = listen()
    str = "Your text is"
    speak(str)
    speak(msg)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(unm, pwd)
    server.sendmail(unm, rec, msg)
    server.quit()

    str = "The email has been Sent"
    speak(str)

def readmail():

    server = e.connect("imap.gmail.com", unm, pwd)
    server.listids()

    str = "Please say the serial number of the email that you need to read"
    speak(str)

    a = listen()
    if( a == " two ") or ( a == "tu"):
        a = "2"
    b = int(a) - 1

    email = server.mail(server.listids()[b])

    str = "The email is from: "
    speak(str)
    speak(email.from_addr)
    str = "The subject of the email is:"
    speak(str)
    speak(email.title)
    str = "The body of email is:"
    speak(str)
    speak(email.body)

str = "Welcome to voice controlled email service"
speak(str)

while(1):

    str = "What do you want to do?"
    speak(str)

    str = "Speak SEND to Send email  Speak READ to Read Inbox  Speak EXIT to Exit "
    speak(str)

    ch = listen()

    if (ch == 'send' ) or (ch == 'sent'):
        str = "You have chosen to send an email"
        speak(str)
        sendmail()

    elif ( ch == 'read'):
        str = "You have chosen to read mail"
        speak(str)
        readmail()

    elif (ch == 'exit'):
        str = "You have chosen to exit, BYE BYE"
        speak(str)
        exit(1)

    else:
        str = "Invalid choice, you said"
        speak(str)
        speak(ch)







