import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('twilightwacky272@gmail.com', 'vbbolbhkqlgnkvjm')
    smtp.sendmail('twilightwacky272@gmail.com',
                     'athullyamol17@gmail.com',
                     'Hi WELCOME TO MY EMAIL ASSISTANT'
                    )
