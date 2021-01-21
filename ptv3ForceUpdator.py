import sys
from ptv3Func import *
    
initBinFolder()
initTrackerFile()

menuOption = menu()
fName = None

if menuOption.lower() == 'n':
    fName = input("Enter Name: ")
    fRoot = input("Enter Path: ")
    fRoot = fixPathAddress(fRoot)
    inSeasoned = input("Seasoned / Have Folders (Y/N): ").upper()
    inSeasoned = 'N' if inSeasoned != 'Y' else inSeasoned
    fh = open(f"./bin/{fName}-{inSeasoned}.txt","a+")
    fh.write(fRoot+"\n")
    fh.close()
    writeInTracker(fName)

else:
    trackerNames = getAllTrackerNameList()
    
    try:
        if (int(menuOption) <= len(trackerNames)):
            fName = trackerNames[int(menuOption)-1]
    except Exception as e:
        print(e)
        sys.exit()

fNameFile = getFileName(fName)

fRoot = getRootAddress(fNameFile).strip()

lastFile = input("Enter Last File you Watched: ")

watchedList = getWatchedList(fNameFile)

notWatchedList = getNotWatchedList(fRoot,watchedList)

lastFileIndex = findIndexOfFile(notWatchedList,lastFile)

fileListToAppendInTracker = notWatchedList[0:lastFileIndex+1]

for item in fileListToAppendInTracker:
    writeInTrackingFile(fNameFile,item)
