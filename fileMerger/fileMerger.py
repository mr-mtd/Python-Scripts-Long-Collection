

#!/usr/bin/env python
import sys
import logging
import logging.handlers
import shutil
import time
import datetime
import glob
import os
import xml.etree.cElementTree as ET

from collections import defaultdict

restrictFileSizeTo = 0


# Method to collect the files and send to merge
def collectFiles(scanPath, archivePath, destinationPath, batchCount):
    logger.info("collecting all the files ")
    logger.info("The process id for this script : " + str(os.getpid()))
    foundFilesLists = run(scanPath)

    logger.info("now go ahead and merge the files")

    appendCount = 0;
    appendCount = len(foundFilesLists)

    logger.info ("length of found filess lists is " + str(len(foundFilesLists)))

    vendorNameToAssociatedXMLSMap = groupFilesBasedOnName(foundFilesLists)
    mergeXMLFiles(vendorNameToAssociatedXMLSMap, scanPath, destinationPath, archivePath, appendCount)

    logger.info("completed merging the files received ")






# groups files based on vendor name and adds them to a map<vendorName, List<fileNames>>
def groupFilesBasedOnName(xmlFiles):

    vendorNameToAssociatedXMLSMap = defaultdict(set)

    for filename in xmlFiles:
        temp = filename.split("_")
        vendorNameToAssociatedXMLSMap[temp[0]].add(filename)

    return vendorNameToAssociatedXMLSMap




#Methd to merge xml files, save merged files and move old files to archive directory
def mergeXMLFiles(mapOfFiles, scanPath, destinationPath, archivePath, appendCount):


    for key in mapOfFiles:
        element = None
        tree = None
        listOfFiles = mapOfFiles.get(key)

        for file in listOfFiles:
            fileLocation = scanPath + file
            tree = ET.parse(fileLocation).getroot()

            #change book to 'X12'
            for el in tree.findall('book'):
                if element is None:
                    element = tree
                    break
                else:
                    element.append(el)
            try:
                logger.info("moving file " + fileLocation + " to path " + archivePath)
                shutil.move(fileLocation, archivePath)
                logger.info("File move is success")
            except IOError, e:
                logger.info("IO ERROR:Unable to move file")
            except:
                logger.info("Unexpected error occured")
        tree = ET.ElementTree(element)
        print("destinationPath is " + destinationPath)
        timestr = time.strftime("%Y%m%d%H%M%S")
        tree.write(destinationPath + key + "_" + timestr + ".xml")







# method to query the directory for files and assign to lists
def run(scanPath):
    logger.info("Scan directory path : " + scanPath)
    filesInDirectory = []
    for file in os.listdir(scanPath):
            if file.endswith(".xml"):
                filesInDirectory.append(file)
                logger.info("XML File Found: " + file)

    return filesInDirectory


if __name__ == "__main__":
    print "#################XMLMergerCronScript started#####################"
    if len(sys.argv) < 5:
        print "ERROR: Invalid arguments. Need to enter 5 arguments"
        print "1. scan directory(individual files) | 2. output directory (merged files) " \
              "| 3. archive directory (to save scan files) | 4. log directory | 5. Maximum No of files to batch " \
              "| 6. (optional) Max output file size for batching"
        print "Please run again...terminating the script"
    else:
        scanPath = str(sys.argv[1])
        print("Scan directory for taking individual files : " + scanPath)
        destinationPath = str(sys.argv[2])
        print("Output directory (which will be the scan for 214 inbound) : " + destinationPath)
        archivePath = str(sys.argv[3])
        print("Archive path to save the individual files : " + archivePath)
        logPath = str(sys.argv[4])
        print("Path to save the log file : " + logPath)
        batchCount = int(sys.argv[5])
        print("No of files to batch : " + str(batchCount))
        # global restrictFileSizeTo
        restrictFileSizeTo = int(sys.argv[6])
        print("Max file size for batching : " + str(restrictFileSizeTo))

        # logPath="C:/projects/Python project/logs/"
        logPath = logPath + str("XMLMergerCronScript.log")
        logger = logging.getLogger("XMLMerger")
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = logging.handlers.RotatingFileHandler(logPath, maxBytes=3000000, backupCount=10)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        # logging.basicConfig(filename=logPath,level=logging.INFO)
        logger.info("#########starting the main code########### ")
        starttime = time.strftime("%Y%m%d%H%M%S")
        logger.info("Start time : " + starttime)


        collectFiles(scanPath, archivePath, destinationPath, batchCount)


        endtime = time.strftime("%Y%m%d%H%M%S")
        logger.info("End time : " + endtime)
        logger.info("#########finished the main code########### ")
    print "#################XMLMergerCronScript Completed#####################"

