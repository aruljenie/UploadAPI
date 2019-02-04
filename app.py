import cv2
import numpy as np
import pytesseract
from PIL import Image
from flask import Flask, url_for, send_from_directory, request
import logging
import os
from werkzeug import secure_filename


app = Flask(__name__)
file_handler = logging.FileHandler('Upload.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/', methods = ['POST'])
def api_root():
    """This function performs the upload of image and returns string"""
    app.logger.info(PROJECT_HOME)
    if request.method == 'POST' and request.files['image']:
        app.logger.info(app.config['UPLOAD_FOLDER'])
        img = request.files['image']
        img_name = secure_filename(img.filename)
        #Create upload folder for storing image files
        create_new_folder(app.config['UPLOAD_FOLDER'])
        #Get the full file path
        saved_path = get_filepath(img_name)
        app.logger.info("saving {}".format(saved_path))
        # Save operatioin
        img.save(saved_path)
        # OCR - Get string from image
        result_string = get_stringfromimage(saved_path)
        return result_string
    else:
        return "Could not extract any text from Image."

def get_stringfromimage(image_path):
    """This function performs the operation of converting text in image to string."""
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    # Generate filename and filepath the image after processing
    gray_filename = "threshold_"+os.path.split(image_path)[-1]
    gray_filepath = get_filepath(gray_filename)
    # Save the Image file after processing
    cv2.imwrite(gray_filepath, img)
    # OCR operation
    result = pytesseract.image_to_string(Image.open(gray_filepath))
    remove_file(image_path)
    remove_file(gray_filepath)
    return result

def create_new_folder(local_dir):
    """This function create folder at the path specified."""
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath

def get_filepath(filename):
    """This function return full file path of the image uploaded"""
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return filepath

def remove_file(filepath):
    """This function removes a specified file based on the parameter value."""
    os.remove(filepath)


if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=False)
    app.run(debug=True)