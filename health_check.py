#!/usr/bin/env python3

import shutil
import psutil
import socket

import emails

def check_cpu():
    return psutil.cpu_percent(1) > 80

def check_disk(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free < 20

def check_memory():
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory < 500

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

checks = {
    check_cpu(): "CPU usage is over 80%",
    check_disk("/"): "Available disk space is less than 20%",
    check_memory(): "Available memory is less than 500MB",
    check_localhost(): "localhost cannot be resolved to 127.0.0.1"
}

for check, error_message in checks.items():
    if not check:
        # Build and send message
        message = emails.generate_email(sender="automation@example.com",
                                        recipient="student-00-a6174b50801c@example.com",
                                        subject=error_message,
                                        body="Please check your system and resolve the issue as soon as possible.")
        emails.send_email(message=message)