import os
import cv2
import numpy as np

# Set the desired size for the images
size = (512,512)

# Set the path to the directory containing the images
path = r""
dest_path= r""

# Loop over all the images in the directory
for file_name in os.listdir(path):
    if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
        # Load the image
        img = cv2.imread(os.path.join(path, file_name))

        # Resize the image
        img_resized = cv2.resize(img, size)

        # Convert the image to JPEG format
        img_jpeg = cv2.imencode('.jpg', img_resized)[1].tobytes()

        # Save the preprocessed image
        cv2.imwrite(os.path.join(dest_path, 'preprocessed_' + file_name), img_resized)
