#! /usr/bin/env python3
from datetime import date
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate(attachement='/tmp/processed.pdf', title="Processed Update on ", data=None):
    title = title + date.today().strftime("%d-%m-%Y")
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachement)
    report_title = Paragraph(title, styles["h1"])
    report_body = [report_title]
    for item in data:
        report_text = "name: {} {} weight: {}".format(item['name'], '<br/><br/>', item['weight'])
        report_data = Paragraph(report_text, styles['BodyText'])
        empty_line = Spacer(1, 20)
        report_body.extend([empty_line, report_data])
    report.build(report_body)
    