from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
#make sure you've allowed less secure apps in your gmail account settings
username = 'yourusernamehere'
password = 'yourpasswordhere'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS":False,
    "MAIL_USE_SSL":True,
    "MAIL_USERNAME": username,
    "MAIL_PASSWORD": password

}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    recipient = str(input('Recipient Address: '))
    sub = str(input('Subject: '))
    message = str(input('Message: '))
    with app.app_context():
        msg = Message(subject=sub,
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[recipient],
                      body=message)
        b = mail.send(msg)
        print('Done.')
