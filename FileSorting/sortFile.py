class SortFile:
    def __init__(self):
        pass

    
    def sort(self, fileInfoList):
        datefile = open("DateWiseSortedFileInfo.txt","w")
        sortedList = sorted(fileInfoList, key= lambda i: i["date"])

        for file in sortedList :
            fileInfoString = "Image name: {}     date: {} \n".format(file['fileName'], file['date'])
            datefile.write(fileInfoString)
            print(fileInfoString)

        datefile.close()
        

    