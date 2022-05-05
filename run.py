#! /usr/bin/env python3

import os

DESCRIPTIONS_DIR="supplier-data/descriptions/"

def parse_text(file):
  data = dict()
  data["image_name"] = file.split('.')[0]+'.jpeg'
  with open(os.path.join(DESCRIPTIONS_DIR, file)) as f:
    fields = f.readlines()
    data['name'] = fields[0].strip()
    data['weight'] = int(fields[1].split(' ')[0])
    data['description'] = fields[2].strip()
  return data

if __name__ == '__main__':
  descriptions_files = os.listdir(DESCRIPTIONS_DIR)
  #print(descriptions_files)

  description_file = descriptions_files[0]
  description_data = parse_text(description_file)
  print(description_data)
