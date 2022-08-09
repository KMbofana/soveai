import mongoengine as db

class notifications(db.Document):
    senderName=db.StringField()
    senderMessage=db.StringField()
    phone=db.StringField()
    time=db.StringField()

    def to_josn(self):
        return {
            "senderName":self.senderName,
            "senderMessage":self.senderMessage,
            "phone":self.phone,
            "time":self.time
        }