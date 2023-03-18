import os
import math
import random
import smtplib
import ssl
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"is you OTP"
msg=otp
s =  smtplib.SMTP_SSL("smtp.gmail.com",465)
s.login("harshsoni2120@gmail.com","htwslizoypyzzmzq")
s.sendmail("harshsoni2120@gmail.com","harshsoni2120@gmail.com",msg)
a= input("Enter Your OTP >> :")
if a== OTP:
    print ("CONGRATULATION!! Your OTP is Verified")
else:
    print("PLEASE cheack your OTP again and fill it properly")


























