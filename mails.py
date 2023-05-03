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

def generate_template(file: str, variables: dict[str: str]) -> str:
    resp: str
    with codecs.open(f"templates/mails/{file}.html", 'r') as template:
        resp = template.read()
        for k,v in variables.items():
            resp = resp.replace(f"{'{{'} {k} {'}}'}", v)

        return resp
