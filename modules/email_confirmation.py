# modules/email_confirmation.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()


def send_confirmation_email(to_email: str, name: str, patient_id: str, fee: str):
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")

    subject = "Patient Registration Confirmation"
    body = f"Dear {name},\n\nThank you for registering. Your Patient ID is {patient_id}.\nPaid Fees: ₹{fee}.\n\nRegards,\nHospital Team"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Confirmation email sent.")
    except Exception as e:
        print(f"Error sending email: {e}")
