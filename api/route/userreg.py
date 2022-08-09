import os
from flask import Flask, Blueprint, jsonify, request
from flask_cors import cross_origin, CORS
from api.controllers.userreg import userReg



user = Blueprint('user',__name__)
api_cors_config={
    "origins":"*",
    "methods":["GET","POST"],
    "allow_header":["Authorization","Content-Type"]
}
CORS(user, resources={"/=*":api_cors_config})

@user.route("/registration", methods=["POST"])
@cross_origin()
def test():
    u=userReg().userRegistration()

    return jsonify(u)
@user.route("/login", methods=["POST"])
@cross_origin()
def login():
    details=userReg().Login()
    return jsonify(details)

@user.route("/forgot_password", methods=["GET","POST"])
@cross_origin()
def forgot_password():
    result=userReg().forgotPassword()
    return jsonify(result)

@user.route("/otp_verify", methods=["GET","POST"])
@cross_origin()
def otp_verify():
    result=userReg().enterOtp()
    return jsonify(result)

@user.route('/users_on_app', methods=["GET"])
@cross_origin()
def showUsers():
    result=userReg().getUsers()
    return jsonify(result)
