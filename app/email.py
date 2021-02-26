from flask_mail import Message
from app import mail
from threading import Thread


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(subject, sender, recepients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg_html = html_body
    Thread(target=send_async_email, args=(apps, msg)).start()

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_mail('[Microblog] Reset your Password',
    sender=app.config['ADMINS'][0],
    recipients=[user.email],
    text_body=render_template('email/reset_password.txt',
            user=user, token=token),
    html_body=render_template('email/reset_password.html',
            user=user, token=token))