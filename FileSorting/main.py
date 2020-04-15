
import os

import datetime

import datefinder

from ImageToText import ImageToText
from tessaract import Tesseract
from tessaractAdapter import TessaractAdapter

from sortFile import SortFile


tesseract : Tesseract = Tesseract()

imageToText : ImageToText = TessaractAdapter(tesseract)


allFiles = os.listdir("images")




fileList = []


for file in allFiles:
    
    try:
        txt = imageToText.toText(file)

        dates = datefinder.find_dates(txt)

        dateSet = set(dates)
        
  
        for d in dateSet:

               
            formatedDate = d.strftime("%Y-%m-%d")
            tempDict = {
                'fileName': file,
                'date': formatedDate
            }

            fileList.append(tempDict)

            
    except :
        
        print("error")


sortFile = SortFile()

sortFile.sort(fileList)



   
    