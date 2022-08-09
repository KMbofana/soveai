from flask import Flask, Blueprint, jsonify,request
from flask_cors import cross_origin, CORS
from api.controllers.messagesController import getMessages

message=Blueprint("message",__name__)

@message.route('/messages', methods=["GET", "POST"])
@cross_origin()
def retMessages():
    result=getMessages().received()

    return jsonify(result)

@message.route("/send_message", methods=["POST"])
@cross_origin()
def sendMessage():
    result=getMessages.sentMessages()
    return jsonify(result)