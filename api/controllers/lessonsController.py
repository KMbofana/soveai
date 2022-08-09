from flask import request
from api.model.alpha import alphabet


class Lessons:
    def learnAphabet(self):
        aData=request.json
        aLesson=aData["lesson"]

        if aLesson:
            less=alphabet.objects()
        else:
            less="none"

        return less
