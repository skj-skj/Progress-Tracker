import os

nameFile = "bin/zzNameFile.txt"
exitOptionList = ['x','q','exit','quit']
exitPromptText = "Exit (x,q,exit,quit) or Continue: "

def initBinFolder():
    try:
        os.mkdir("bin")
    except:
        return

def initTrackerFile():
    fh = open(nameFile,"a+")
    fh.close()

def writeInTracker(fName):
    fh = open(nameFile,"a+")
    fh.write(fName+'\n')
    fh.close()

def fixPathAddress(path):
    return path.replace("\\","/").strip()

def getRootAddress(file):
    fh = open(file,"r")
    fRoot = fh.readlines()[0]
    fh.close()
    return fRoot.strip()

def getFileName(fName):
    with os.scandir('./bin/') as entries:
        for entry in entries:
            if fName == (entry.name).split('-N')[0] or fName == (entry.name).split('-Y')[0]:
                return "./bin/"+entry.name
    
def getWatchedList(file):
    fh = open(file,"r")
    watchList = fh.readlines()[1:]
    watchList = [item.strip() for item in watchList]
    fh.close()
    return watchList

def getNotWatchedList(fRoot,watched):
    allFiles = []
    for root, dirs, files in os.walk(fRoot):
        for f in files:
            if('desktop.ini' in f):
                continue
            if fixPathAddress(os.path.join(root, f)) not in watched:
                allFiles.append(fixPathAddress(os.path.join(root, f)))
    
    return allFiles

def writeInTrackingFile(file,item):
    fh = open(file,"a")
    fh.write(item+"\n")
    fh.close()

def menuCore():
    fh = open(nameFile,"r")
    allTrackers = fh.readlines()
    for i in range(len(allTrackers)):
        print(f'{i+1}. {allTrackers[i].strip()}')

def menu():
    menuCore()
    print('N. New Entry')
    return input("Enter Your Choice: ")

def deleteMenu():
    menuCore()
    return input("Enter Your Choice (to Delete):")

def getAllTrackerNameList():
    fh = open(nameFile,"r")
    return [item.strip() for item in fh.readlines()]

def findIndexOfFile(list,item):
    for i in range(len(list)):
        if item in list[i].split('/')[-1]:
            return i

def exitWait():
    input("Press any key to Exit/Quit: ")