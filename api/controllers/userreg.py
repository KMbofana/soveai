from api.model.user import users
from flask import request
from flask_mail import Message, Mail
from api.model.otp import myotp
import pyotp
import time
import datetime

mail = Mail()

class userReg:
    def userRegistration(reg):
        regData=request.json
        reg=users(name=regData["name"], email=regData["email"], phone=regData["phone"],password=regData["password"])
        # reg="test"
        reg.save()

        if reg:
            status={
                "status": 1,
                "message": "Registered"
            }
        else:
            status={
                "status": 0,
                "message": "no registered"

            }

        return status
    def Login(*args):
        logCreds=request.json
        password=logCreds["password"]

        
        if users.objects(password=password):
            status={
                "status":1,
                "message":"authenticated user"
                }
        else:
            status={
                "status":0,
                "message":"unauthenticated user"}
        
        return status

    def forgotPassword(*args):
        # first check if the email address matched the email used to create account
        # if it macthes we want to send an email with OTP or link to reset password to to that email which we confirmed to be correct
        forgData=request.json
        forgEmail=forgData["email"]

        # creating an empty dictionary
        emails={}
        status={}
        # for em in users.objects:
        #     # filling the dictionary
        #     emails["email"]=em.email
        #     print(emails)
        # # compare the emails
        if users.objects(email=forgEmail):
            # create a logic that send an emeil
            msg=Message("test", sender="keithmbofana1@gmail.com",recipients=["a9216845cd4eac@inbox.mailtrap.io"])
            # generating otp
            totp=pyotp.TOTP('base32secret3232')
            otps=totp.now()
            msg.body="your otp is "+otps +"and will expire in 60 seconds"
            totp.verify(otps)
            ots=myotp(otp=otps, time=str(datetime.datetime.now()), email="keithmbofana1@gmail.com")
            ots.save()
            time.sleep(60)
            totp.verify(otps)
            myotp.objects(email="keithmbofana1@gmail.com").delete()
            mail.send(msg)
            status.update({"status":1,"message":"email correct"})
            
        else:
            status.update({"status":0,"message":"incorrect email"})
                
        return status
    
    def enterOtp(*args):
        getOtp=request.json
        otp=getOtp["otp"]
        dbOTP=myotp.objects(email="keithmbofana1@gmail.com").first()

        if otp==dbOTP["otp"]:
            status={
                "msg":"OTP is correct",
                "status":1
            }
        else:
            status={
                "msg":"OTP is incorrect",
                "status":0
            }

        return status

    def getUsers(*args):
        usersOnApp=users.objects()
        if usersOnApp:
            return usersOnApp
        else:
            status={
                "status":0,
                "messages":"no registered users"
            }
            return status
            