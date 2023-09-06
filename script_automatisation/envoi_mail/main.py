import emails_config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# config_email
# config_password
# config_server
# config_server_port


def envoyer_email(destinataire, sujet, message):
    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = sujet
    multipart_message["From"] = emails_config.config_email
    multipart_message["To"] = destinataire
    multipart_message.attach(MIMEText(message, "plain"))
    server_mail = smtplib.SMTP(emails_config.config_server, emails_config.config_server_port)
    server_mail.starttls()
    server_mail.login(emails_config.config_email, emails_config.config_password)
    server_mail.sendmail(emails_config.config_email, destinataire, multipart_message.as_string())
    server_mail.quit()


envoyer_email("mathieu.vaudon@gmail.com", "Envoyé depuis Python", "Hello World")
