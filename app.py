from flask import Flask
from flask_mail import Mail
from api.route.userreg import user
from api.route.lessons import lessons
from api.route.message import message


from flask_mongoengine import MongoEngine
mail = Mail()

def create_app():
    app= Flask(__name__)

    app.config['MONGODB_SETTINGS']={
        "db":"sove",
        "host":"localhost",
        "port":27017
    }
    app.config['MAIL_SERVER']='smtp.mailtrap.io'
    app.config['MAIL_PORT']=2525
    app.config['MAIL_USERNAME']='a9216845cd4eac'
    app.config['MAIL_PASSWORD']='835ed149a24532'
    app.config['MAIL_USE_TLS']=True
    app.config['MAIL_USE_SSL']=False

    app.register_blueprint(user)
    app.register_blueprint(lessons)
    app.register_blueprint(message)
    db = MongoEngine()
    db.init_app(app)
    mail.init_app(app)
    return app

if __name__=='__main__':
    app = create_app()
    app.run(host="localhost", port=5000, debug=True)