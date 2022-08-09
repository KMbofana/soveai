import mongoengine as db

class myotp(db.Document):
    otp=db.StringField()
    time=db.StringField()
    email=db.StringField()

    def to_json(self):
        return {
            "otp": self.otp,
            "time": self.time,
            "email": self.email
        }
        



