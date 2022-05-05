#! /usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib


def generate_email(sender, recipient, subject, body, attachement_path):
    """Create an email with an attachement"""
    # Basic email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachement and add it to the email
    attachement_filename = os.path.basename(attachement_path)
    mime_type, _ = mimetypes.guess_type(attachement_filename)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachement_filename, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachement_filename)
    return message

def send_email(message):
    """Send message to the configured SMTP server"""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()