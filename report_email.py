#! /usr/bin/env python3

import os

import reports
import run
import emails

DESCRIPTIONS_DIR="supplier-data/descriptions/"

if __name__ == '__main__':
    paragraph = [run.parse_text(description_file) for description_file in os.listdir(DESCRIPTIONS_DIR)]
    reports.generate_report(attachment='/tmp/processed.pdf', title="Processed Update on ", paragraph=paragraph)
    message = emails.generate_email(sender="automation@example.com",
                                    recipient="student-00-7132de281614@example.com",
                                    subject="Upload Completed - Online Fruit Store",
                                    body="All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                                    attachement_path='/tmp/processed.pdf')