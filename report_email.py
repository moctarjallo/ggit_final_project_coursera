#! /usr/bin/env python3

from datetime import date
import os

import reports
import run
import emails

DESCRIPTIONS_DIR="supplier-data/descriptions/"

def process_data(data):
    return ["name: {}<br/>weight: {}\n".format(item[0], item[1]) for item in data]

if __name__ == '__main__':
    # Build report 
    paragraph_data = [run.parse_text(description_file) for description_file in os.listdir(DESCRIPTIONS_DIR)]
    paragraph = process_data(paragraph_data)
    title = "Processed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
    attachement='/tmp/processed.pdf'
    reports.generate_report(attachement, title, paragraph)

    # Build and send message
    message = emails.generate_email(sender="automation@example.com",
                                    recipient="student-00-7132de281614@example.com",
                                    subject="Upload Completed - Online Fruit Store",
                                    body="All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                                    attachement_path='/tmp/processed.pdf')
    emails.send_email(message=message)