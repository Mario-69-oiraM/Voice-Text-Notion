
from os import listdir
from os.path import isfile, join, exists 
import logging
logger = logging.getLogger(__name__)
logger = logging
logger.basicConfig()

#function to return files in a directory
def fileInDirectory(my_dir: str):
    onlyfiles = [f for f in listdir(my_dir) if isfile(join(my_dir, f))]
    return(onlyfiles)

#function comparing two lists
def listComparison(OriginalList: list, NewList: list):
    differencesList = [x for x in NewList if x not in OriginalList] #Note if files get deleted, this will not highlight them
    return(differencesList)

def savefilelist(dataPath, fileList):
    logfile = dataPath + 'files.csv'
    with open(logfile, 'w') as f:
        for line in fileList:
            f.write(f"{line}\n")

def readfilelist(dataPath):
    logfile = dataPath + 'files.csv'
    f = open(logfile, "r")
    reader = [line.rstrip() for line in f]
    return(reader)

def findFilesToProcess(audioPath, dataPath):
    listOfFilesonDisk = fileInDirectory(audioPath)
    listOfFilesInFile = readfilelist(dataPath)
        
    for row in listOfFilesonDisk:
        if row[0] not in listOfFilesInFile:
            listOfFilesInFile.append(row + ', ')
            logger.info('adding file to list ' + row)
        
    savefilelist(dataPath, listOfFilesInFile)
    
    for lin in listOfFilesInFile:
        if lin.split()

    return(listOfFilesInFile)
 
