import os
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

fRoot = getRootAddress(fNameFile)

watchedList = getWatchedList(fNameFile)

notWatchedList = getNotWatchedList(fRoot,watchedList)

print("You Watched:")
for item in watchedList:
    print(item.split("/")[-1])

print("*"*50)

for item in notWatchedList:
    while True:
        try:
            print(item.split('/')[-1])
            choice = input("Already Watched(1) / Want to Watch(0) / Exit(x or q or exit or quit): ")
            if choice == '0':
                os.system(f'start "ptv3" "{item}"')
                confirm = input("Watched? Yes(0)/No(1): ")
                if confirm == '0':
                    writeInTrackingFile(fNameFile,item)
                    break
                continue
            elif choice == '1':
                writeInTrackingFile(fNameFile,item)
                break
            elif choice.lower() in exitOptionList:
                sys.exit()
            else:
                continue
        except Exception as e:
            print(e)
            continue

print("----------Watchlist is Completed----------")
exitWait()