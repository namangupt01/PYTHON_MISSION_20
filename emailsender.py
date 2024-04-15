import smtplib

to = input("Enter the email of the recipent:\n")

content = input("Enter the content for email")

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com','1234')
    server.sentmail('senderemail@gmail.com',to,content)
    server.close()


sendemail(to,content)




