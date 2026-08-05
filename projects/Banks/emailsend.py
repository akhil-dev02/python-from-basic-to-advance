import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSKEY = os.getenv("PASSKEY")


def SingleEmailSend(to_email, subject, body):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()

        server.login(SENDER_EMAIL, PASSKEY)

        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())

        server.quit()

        return f"Email sent successfully to {to_email}"

    except Exception as e:
        return f"Something went wrong while sending email: {e}"