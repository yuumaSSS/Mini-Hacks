import smtplib

to_address = 'someone@gmail.com'
from_address = 'you@gmail.com' 
message = "You've been bombed"

with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login('you@gmail.com', 'your google App Password')

    for i in range(100): # iterations
        smtpserver.sendmail(fromaddrs, toaddrs, message)
        print(i)