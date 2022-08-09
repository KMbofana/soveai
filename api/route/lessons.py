from flask import Flask, Blueprint, jsonify, request
from flask_cors import cross_origin, CORS
from api.controllers.lessonsController import Lessons


lessons=Blueprint('lessons',__name__)

@lessons.route("/alphabet", methods=["GET", "POST"])
@cross_origin()
def retAlphabet():
    result=Lessons().learnAphabet()
    return jsonify(result)
