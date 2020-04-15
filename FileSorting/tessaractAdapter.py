from ImageToText import ImageToText
from tessaract import Tesseract
class TessaractAdapter(ImageToText):
    tesseract: Tesseract

    def __init__(self, tesseract: Tesseract ):
        self.tesseract = tesseract


    def toText(self, filename):
        
        text = self.tesseract.imgToString(filename)

        return text
        
       