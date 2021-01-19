import os
from ptv3Func import *

while True:

    try:
        menuOption = deleteMenu()
        fName = getAllTrackerNameList()[int(menuOption)-1]
    except Exception as e:
        print("Please Enter Valid Option!")
        option = input(exitPromptText)
        if option in exitOptionList:
            break
        else:
            continue

    confirm = input("Are You Sure!!! (Y/N): ").lower()
    
    if confirm == 'y':
        os.remove(getFileName(fName))
        trackerNameList = getAllTrackerNameList()
        fh = open(nameFile,"w")
        for item in trackerNameList:
            if item == fName:
                continue
            fh.write(f'{item}\n')
        fh.close()
        break
    
    else:
        option = input(exitPromptText)
        if option in exitOptionList:
            break
        else:
            continue


exitWait()


