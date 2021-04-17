import smtplib
import ssl
import os


class Client:
    def __init__(self):
        self.smtp_adress = 'smtp.gmail.com'
        self.smtp_port = 465
        self.username = os.getenv('EMAIL_USERNAME')
        self.password = os.getenv('EMAIL_PASSWORD')
        self.context = ssl.create_default_context()

    def send(self, recipient, subject, message):
        message = f"Subject: {subject}\n\n{message}"
        with smtplib.SMTP_SSL(self.smtp_adress, self.smtp_port, context=self.context) as server:
            server.login(self.username, self.password)
            server.sendmail(self.username, recipient, message)
            server.quit()

    def _get_login_code(self):
        with smtplib.SMTP_SSL(self.smtp_adress, self.smtp_port, context=self.context) as server:
            code = server.login(self.username, self.password)[0]
            server.quit()
            return code