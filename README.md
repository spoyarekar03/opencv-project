# Fabric Defect Detection
This project aims to detect defects in fabric images using a cascaded classifier approach.

## Prerequisites
To run this project, you will need to download and include the following files in the required files directory: 

- cascade_level01 (used pretrained xml file) Pretrained xml file used for the fabric detection.

- cascade_level02 (used pretrained xml file) Pretrained xml file used for the fabric detection.

In addition, you will need to provide some sample images in the images directory, including both positive (defective) and negative (non-defective) images. You will need to provide the path to the input image in the fabric_defect_image.py file.

If you want to train the cascade model, use the cascadeutils.py script. The instructions for training the model are provided in the script itself.

## Installation 
To install the required packages, run the following command in your terminal:

```
pip install -r requirements.txt
```


## Running the project
To run the project, execute the following command in your terminal:
```
python 'fabric_defect_image.py'
```

Alternatively, you can use the defect_detect_image.py file to detect defects in multiple images at once. Use the following command to run the script:
```
python 'defect_detect_image.py'
```

If you want to train the cascade model, use the following command:
```
python 'cascadeutils.py'
```

## Troubleshooting
If you encounter any issues while running the project, try the following:

Make sure that you have installed all the required packages listed in requirements.txt.

Double-check that you have included all the required files in the required files directory.

If you are still encountering issues, please refer to the project's documentation or raise an issue in the project's GitHub repository.