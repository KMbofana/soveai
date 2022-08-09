from flask import Flask, request
from api.model.rmessages import rmessages
from api.model.user import users
from api.model.notifications import notifications

class getMessages:
    def received(self):
        messageData=request.json
        mFrom=messageData["phone"]

        if rmessages.objects(messagefrom=mFrom):
            message=rmessages.objects()
        else:
            message="0 Messages"
        
        return message
    
    def sentMessages():
        sentData=request.json
        # sentTo=sentData["phone"]

        send=rmessages(message=sentData["message"],
                        time=sentData["time"],
                        date=sentData["date"],
                        messagefrom=sentData["messagefrom"],
                        messageto=sentData["messageto"])
        #we want to take user name from users collection
        senderDetails= users.objects(phone=sentData["messagefrom"]).first() #returns a a json object
        senderMessage=sentData["message"]
        noty=notifications(senderName=senderDetails["name"],senderMessage=senderMessage,phone=senderDetails["phone"],time="today")

        if send:
            send.save()
            noty.save()
            # create notification with name of sender, message, and time
            status={
                "status":1,
                "message":"message sent"
            }
        else:
            status={
                "status":"0",
                "message":"message could not be sent"
            }
    
        return status
