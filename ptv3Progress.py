import sys
import os
from ptv3Func import *

menuCore();
menuOption = input("Enter Your Choice: ")
fName = None

trackerNames = getAllTrackerNameList()

try:
    if (int(menuOption) <= len(trackerNames)):
        fName = trackerNames[int(menuOption)-1]
except Exception as e:
    print(e)
    sys.exit()

fNameFile = getFileName(fName)
fRoot = getRootAddress(fNameFile)
watchedList = getWatchedList(fNameFile)
notWatchedList = getNotWatchedList(fRoot,watchedList)
print(divider)
if '-n.txt' in fNameFile.lower():
    progressPercentage = getOverallWatchedPercentage(watchedList,notWatchedList)
    print(f'{fName} - {progressPercentage}% Completed')
    print(divider)
    exitWait()

elif '-y.txt' in fNameFile.lower():
    progerssMainPercentage = getOverallWatchedPercentage(watchedList,notWatchedList)
    subFolders = getAllSubFolders(fRoot)
    for folder in subFolders:
        totalNoOfAllFiles = getTotalNoOfFilesInFolder(f'{fRoot}/{folder}')
        totalNoOfWatchedFiles = getTotalNoOfFilesWatched(fRoot,folder,watchedList)
        subProgressPercentage = round((totalNoOfWatchedFiles/totalNoOfAllFiles)*100,2)
        print(f'{fName}: {folder} - {subProgressPercentage}% Completed')
    print(divider)
    print(f'{fName} - {progerssMainPercentage}% Completed')
    print(divider)
    exitWait()





