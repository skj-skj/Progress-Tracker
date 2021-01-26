import sys
from Ptv3Foo import *

while (True):
    menuCore();
    menuOption = input("Enter Your Choice or (x) to exit:")

    #To check for Exit Option
    if menuOption in exitOptionList:
        sys.exit()
        
    NamesInRecordFile = getAllNameFromRecord()
    fName = None

    #to check user enter valid option (to avoid 0, -ve numbers and number greater than in NameFile)
    if (menuOption.isdigit()):
        menuOption = int(menuOption)
        if (menuOption<1 or menuOption>len(NamesInRecordFile)):
            print(enterValidOptionPrompt)
            continue
    else:
        print(enterValidOptionPrompt)
        continue
    
    fName = NamesInRecordFile[int(menuOption)-1]
    
    #fName is name of the Main Folder
    fNameFile = getFileName(fName) #fNameFile is location of .txt file of the fName stored in bin folder
    fRoot = getRootAddress(fNameFile) #fRoot is the location of the Main Folder stored in the first line of the .txt file (fNameFile)
    watchedList = getWatchedList(fNameFile) #gets the watchList from the .txt file (fNameFile) excluding first line
    notWatchedList = getNotWatchedList(fRoot,watchedList) # gets notWatchList by scanning the fRoot location in the PC and comparing to watchList
    print(divider) #****

    # if the Series is not Seasoned
    if '-n.txt' in fNameFile.lower():
        #Gets overall percentage by calculating using the length of watchedList and notWatchedList
        progressPercentage = getOverallWatchedPercentage(watchedList,notWatchedList)
        print(f'{fName} - {progressPercentage}% Completed')
        print(divider)

    # if the Series is Seasoned
    elif '-y.txt' in fNameFile.lower():
        #Gets overall percentage by calculating using the length of watchedList and notWatchedList
        progerssMainPercentage = getOverallWatchedPercentage(watchedList,notWatchedList)
        subFolders = getAllSubFolders(fRoot)

        #Gets subFolders percentage 
        #calculate by total no of file in that subfolder and no of file watched in that subfolder
        for folder in subFolders:
            totalNoOfAllFiles = getTotalNoOfFilesInFolder(f'{fRoot}/{folder}')
            totalNoOfWatchedFiles = getTotalNoOfFilesWatched(fRoot,folder,watchedList)
            subProgressPercentage = round((totalNoOfWatchedFiles/totalNoOfAllFiles)*100,2)
            print(f'{fName}: {folder} - {subProgressPercentage}% Completed')
        print(divider) #****
        print(f'{fName} - {progerssMainPercentage}% Completed')
        print(divider) #****

    #Show prompt to exit the system
    if exitWithPrompt():
        break
    else:
        continue

#Wait for user to hit enter
exitWait()





