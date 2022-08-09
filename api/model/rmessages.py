import mongoengine as db

class rmessages(db.Document):
    # senderID=db.StringField()
    messageto=db.StringField()
    messagefrom=db.StringField()
    message=db.StringField()
    time=db.StringField()
    date=db.StringField()

    def to_json(self):
        return {
            # "senderId":self.senderID,
            "messageto":self.messageto,
            "messagefrom":self.messagefrom,
            "message":self.message,
            "time":self.time,
            "date":self.date
        }