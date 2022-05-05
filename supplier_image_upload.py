#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

from changeImage import IMAGES_DIR, get_source_images

url = "http://localhost/upload/"
for source_image in get_source_images(ext='.jpeg'):
  with open(os.path.join(IMAGES_DIR, source_image), 'rb') as opened:
    r = requests.post(url, files={'file': opened})