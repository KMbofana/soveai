import mongoengine as db


class users(db.Document):
    name=db.StringField(required=True)
    email=db.StringField(required=True)
    phone=db.StringField()
    password=db.StringField(required=True)

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "password":self.password
        }