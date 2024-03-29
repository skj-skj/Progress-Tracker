import sys
import Ptv3Const as ptv3
from Ptv3Foo import *

initDataFolder()
initRecordFile()


while (True):

    menuOption = menu()

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
    # to check user enter valid option (option other than 'n')
    elif (not menuOption.lower() == 'n'):
        print(ptv3.enterValidOptionPrompt)
        continue

    # wrapping menuOption in str as it was converted in int for valid number option
    if str(menuOption).lower() == 'n':
        fName = input("Enter Name: ")
        fRoot = input("Enter Path: ")
        fRoot = fixPathAddress(fRoot)
        inSeasoned = input("Seasoned / Have Folders (Y/N): ").upper()
        inSeasoned = 'N' if inSeasoned != 'Y' else inSeasoned
        fh = open(f"./bin/{fName}-{inSeasoned}.txt", "a+")
        fh.write(fRoot+"\n")
        fh.close()
        writeInRecordFile(fName)

    else:
        fName = NamesInRecordFile[int(menuOption)-1]

    # fName is name of the Main Folder
    # fNameFile is location of .txt file of the fName stored in bin folder
    fNameFile = getFileName(fName)
    # fRoot is the location of the Main Folder stored in the first line of the .txt file (fNameFile)
    fRoot = getRootAddress(fNameFile).strip()
    # lastFile stores the last file user watched
    lastFile = input("Enter Last File you Watched: ")

    # gets the watchList from the .txt file (fNameFile) excluding first line
    watchedList = getWatchedList(fNameFile)
    # gets notWatchList by scanning the fRoot location in the PC and comparing to watchList
    notWatchedList = getNotWatchedList(fRoot, watchedList)

    lastFileIndex = findIndexOfFile(notWatchedList, lastFile)
    fileListToAppendInTracker = notWatchedList[0:lastFileIndex+1]

    for item in fileListToAppendInTracker:
        writeInTrackingFile(fNameFile, item)

    if exitWithPrompt():
        break
    else:
        continue

exitWait()
