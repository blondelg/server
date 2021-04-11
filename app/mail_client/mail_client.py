import smtplib
import ssl
import sys


class client:
    def __init__(self):
        smtp_adress = 'smtp.gmail.com'
        smtp_port = 465
        email_adress = 'geoffroypointblondel@gmail.com'
        email_password = ''

# on rentre les informations sur le destinataire
email_receiver = 'geoffroy.blondel@gmail.com'

# on crée la connexion
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_adress, smtp_port, context=context) as server:
  # connexion au compte
  server.login(email_adress, email_password)
  # envoi du mail
  server.sendmail(email_adress, email_receiver, 'le contenu de l\'e-mail')
