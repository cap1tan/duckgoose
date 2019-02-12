import os
from duckgoose import fetchImagesAndPrepForClassification

# dictionary structure `class_name => search term`
image_classes = { 'ducks' : 'ducks -rubber' , 'geese' : 'geese' }
download_path = os.path.join(os.getcwd(), 'data', 'dev', 'downloaded_from_google')
output_path = os.path.join(os.getcwd(), 'data', 'dev', 'duckgeese')
number_of_images = 15

fetchImagesAndPrepForClassification(image_classes, download_path, output_path, number_of_images, download_if_paths_exists=False)

