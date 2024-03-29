import sys
import Ptv3Const as ptv3
from Ptv3Foo import *

while (True):
    menuCore()
    menuOption = input("Enter Your Choice or (x) to exit:")

    # To check for Exit Option
    if menuOption in ptv3.exitOptionList:
        sys.exit()

    NamesInRecordFile = getAllNameFromRecord()
    fName = None

    # to check user enter valid option (to avoid 0, -ve numbers and number greater than in NameFile)
    if (menuOption.isdigit()):
        menuOption = int(menuOption)
        if (menuOption < 1 or menuOption > len(NamesInRecordFile)):
            print(ptv3.enterValidOptionPrompt)
            continue
    else:
        print(ptv3.enterValidOptionPrompt)
        continue

    fName = NamesInRecordFile[int(menuOption)-1]

    # fName is name of the Main Folder
    # fNameFile is location of .txt file of the fName stored in bin folder
    fNameFile = getFileName(fName)
    # fRoot is the location of the Main Folder stored in the first line of the .txt file (fNameFile)
    fRoot = getRootAddress(fNameFile)
    # gets the watchList from the .txt file (fNameFile) excluding first line
    watchedList = getWatchedList(fNameFile)
    # gets notWatchList by scanning the fRoot location in the PC and comparing to watchList
    notWatchedList = getNotWatchedList(fRoot, watchedList)
    print(ptv3.divider)  # ****

    # if the Series is not Seasoned
    if '-n.txt' in fNameFile.lower():
        # Gets overall percentage by calculating using the length of watchedList and notWatchedList
        progressPercentage = getOverallWatchedPercentage(
            watchedList, notWatchedList)
        watchedListLength = len(watchedList)
        notWatchedListLength = len(notWatchedList)
        totalLength = watchedListLength+notWatchedListLength
        print(
            f'{fName} - {progressPercentage}% Completed ({watchedListLength}/{totalLength})')
        print(ptv3.divider)

    # if the Series is Seasoned
    elif '-y.txt' in fNameFile.lower():
        # Gets overall percentage by calculating using the length of watchedList and notWatchedList
        progerssMainPercentage = getOverallWatchedPercentage(
            watchedList, notWatchedList)
        subFolders = getAllSubFolders(fRoot)

        # Gets subFolders percentage
        # calculate by total no of file in that subfolder and no of file watched in that subfolder
        for folder in subFolders:
            totalNoOfAllFiles = getTotalNoOfFilesInFolder(f'{fRoot}/{folder}')
            totalNoOfWatchedFiles = getTotalNoOfFilesWatched(
                fRoot, folder, watchedList)
            subProgressPercentage = round(
                (totalNoOfWatchedFiles/totalNoOfAllFiles)*100, 2)
            print(
                f'{fName}: {folder} - {subProgressPercentage}% Completed ({totalNoOfWatchedFiles}/{totalNoOfAllFiles})')
        print(ptv3.divider)  # ****
        print(f'{fName} - {progerssMainPercentage}% Completed')
        print(ptv3.divider)  # ****

    # Show prompt to exit the system
    if exitWithPrompt():
        break
    else:
        continue

# Wait for user to hit enter
exitWait()
