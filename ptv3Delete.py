import os
import sys
from Ptv3Foo import *

while (True):
    menuOption = deleteMenu()

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

    fName = getAllNameFromRecord()[int(menuOption)-1]

    confirm = input("Are You Sure!!! (Y/N): ").lower()
    
    if confirm == 'y':
        os.remove(getFileName(fName))
        trackerNameList = getAllNameFromRecord()
        fh = open(recordFile,"w")
        for item in trackerNameList:
            if item == fName:
                continue
            fh.write(f'{item}\n')
        fh.close()

    if exitWithPrompt():
            break
    else:
        continue

exitWait()


