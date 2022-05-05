#!/usr/bin/env python3

import os
from PIL import Image

IMAGES_DIR="supplier-data/images"

def get_source_images(ext='.tiff'):
  source_images = [source_image for source_image in os.listdir(IMAGES_DIR) if source_image.endswith(ext)]
  return source_images

#source_images = get_source_images()
#print(source_images)

def transform_image(source_image, to_size=(600,400)):
  source_image_path = os.path.join(IMAGES_DIR, source_image)
  image = Image.open(source_image_path).convert('RGB').resize(to_size)
  return image

def save_image(image, image_name, to_format='jpeg'):
  image_name = image_name.split('.')[0]
  dest_image = os.path.join(IMAGES_DIR, image_name+'.jpeg')
  image.save(dest_image, format=to_format)

#example_source_image = '003.tiff'
#image_transformed = transform_image(example_source_image)
#print(image_transformed.size)
#print(image_transformed.format)

#save_image(image_transformed, example_source_image)

if __name__ == '__main__':
  for source_image in get_source_images():
    transformed_image = transform_image(source_image)
    save_image(transformed_image, source_image)