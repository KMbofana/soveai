import mongoengine as db

class alphabet(db.Document):
    letter=db.StringField()

    def to_json(self):
        return{
            "letter":self.letter
        }
