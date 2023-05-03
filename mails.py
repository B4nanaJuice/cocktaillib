import smtplib
from email.message import EmailMessage
import config
import codecs

def send_mail(to: list[str], subject: str, content: str) -> None:
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = "noreply.cocktaillib@gmail.com"
    message['To'] = to

    message.set_content(content, subtype = "html")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(config.MAIL, config.MAIL_PASSWORD)
        smtp.send_message(message)

def generate_template() -> str:
    with codecs.open("templates/mails/confirm_mail.html", 'r') as template:
        return template.read().replace("{{ content }}", "Coucou toi")

send_mail(["griesmaxime2@gmail.com"], "tuyt", generate_template())