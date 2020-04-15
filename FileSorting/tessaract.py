from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe' # Add path where tesseract is installed in computer
class Tesseract:
    def __init__(self):
        pass


        
    def imgToString(self,filename):
        """
        This function will handle the core OCR processing of images.
        """
        path = "images/{}".format(filename)
        text = pytesseract.image_to_string(Image.open(path),config='-l eng ')  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
        return text


