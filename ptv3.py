import os
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
        # Main Folder name but it could be anything, as long as user recognises it
        fName = input("Enter Name: ")
        fRoot = input("Enter Path: ")  # Main FOlder Location
        fRoot = fixPathAddress(fRoot)  # Replacing '\' to '/' in the locaiton

        # if Main Folders have Subfolders like Season 1, Season 2 etc than it 'Y'
        # if Main Folders have just files like Episode 1.mkv, Episode 2.mkv. Episode 3.pdf etc than it 'N'
        # by default its 'N' if no input or any other input which is != 'Y'
        inSeasoned = input("Seasoned / Have Folders (Y/N): ").upper()
        inSeasoned = 'N' if inSeasoned != 'Y' else inSeasoned

        # Create a .txt in data folder and write the Main Folder Location 'fRoot' in the first line of the .txt file
        fh = open(f"./{ptv3.dataFolderName}/{fName}-{inSeasoned}.txt", "a+")
        fh.write(fRoot+"\n")
        fh.close()

        # Write the fName in NameFile.txt which keeps record of the .txt file in data folder
        writeInRecordFile(fName)

    else:
        fName = NamesInRecordFile[int(menuOption)-1]

    # fName is name of the Main Folder
    # fNameFile is location of .txt file of the fName stored in data folder
    fNameFile = getFileName(fName)
    # fRoot is the location of the Main Folder stored in the first line of the .txt file (fNameFile)
    fRoot = getRootAddress(fNameFile)
    # gets the watchList from the .txt file (fNameFile) excluding first line
    watchedList = getWatchedList(fNameFile)
    # gets notWatchList by scanning the fRoot location in the PC and comparing to watchList
    notWatchedList = getNotWatchedList(fRoot, watchedList)

    # Print All Watched File
    print("You Watched:")
    for item in watchedList:
        print(item.split("/")[-1])

    print(ptv3.divider)  # ****

    # iterate for every item in notWatchList
    for item in notWatchedList:
        choice = None
        while True:
            try:
                # Print the name of the file
                print(item.split('/')[-1])
                # waiting for the user to make a choice
                choice = input(
                    "Already Watched(1) / Want to Watch(0) / Exit(x or q or exit or quit): ")

                # To open the file user want to watch
                if choice == '0':
                    os.system(f'start "ptv3" "{item}"')
                    confirm = input("Watched? Yes(0)/No(1): ")
                    if confirm == '0':
                        writeInTrackingFile(fNameFile, item)
                        break
                    continue

                # if user already watched the file
                elif choice == '1':
                    writeInTrackingFile(fNameFile, item)
                    break

                # if user choses to exit
                elif choice.lower() in ptv3.exitOptionList:
                    break

                # anything else will result to nothing
                else:
                    continue
            except Exception as e:
                print(e)
                continue
        # if user choses to exit it will break from the loop
        if (choice.lower() in ptv3.exitOptionList):
            break
        else:
            continue

    # print("----------Watchlist is Completed----------")
    print(ptv3.divider2)  # ----

    # Show prompt to exit the system
    if exitWithPrompt():
        break
    else:
        continue

# Wait for user to hit enter
exitWait()
