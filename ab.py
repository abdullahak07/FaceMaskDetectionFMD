import os
import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("mohammadalia61@gmail.com","pl09412371360")
server.sendmail("mohammadalia61@gmail.com","aahmad607@gmail.com","No mask?,fucx off")

server.quit()