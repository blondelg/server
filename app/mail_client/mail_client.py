import smtplib
import ssl
import os


class Client:
    def __init__(self):
        smtp_adress = 'smtp.gmail.com'
        smtp_port = 465
        username = os.getenv('EMAIL_USERNAME')
        password = os.getenv('EMAIL_PASSWORD')
        context = ssl.create_default_context()

    def send(self, recipient, subject, message):
        message = f"Subject: {subject}\n\n{message}"
        with smtplib.SMTP_SSL(self.smtp_adress, self.smtp_port, context=self.context) as server:
            server.login(self.username, self.password)
            server.sendmail(self.username, recipient, message)
            server.quit()
