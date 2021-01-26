import os
import re
import SortFoo

recordFile = "bin/zzRecordFile.txt"
exitOptionList = ['x','q','exit','quit']
exitPromptText = "Exit (x,q,exit,quit) or Continue: "
divider = '*'*50
divider2 = '-'*50
enterValidOptionPrompt = "Please Enter Valid Option!"

def removeAllSlashes(s):
    return ''.join(s.split('/'))

def initBinFolder():
    try:
        os.mkdir("bin")
    except:
        return

def initRecordFile():
    fh = open(recordFile,"a+")
    fh.close()

def naturalSort(l):
    def convert(x):
        return int(x) if x.isdigit() else removeAllSlashes(x.lower())
    def alphanumKey(string):
        return [convert(x) for x in re.split('([0-9]+)',string)]
    l.sort(key=alphanumKey)
    return l

# def nsort(l):
#     convert = lambda text: int(text) if text.isdigit() else text.lower()
#     alphanumKey = lambda key: [convert(c) for c in re.split('([0-9]+)',key)]
#     l.sort(key=alphanumKey)

def naturalSortAlternate(l): #This Natural Sort to ignore '/' in the sorting comparisons
    def convert(x):
        return int(x) if x.isdigit() else x.lower() if x!='/' else ''
    def alphanumKey(string):
        return [convert(x) for x in re.split('([0-9]+)',string)]
    l.sort(key=alphanumKey)
    return l

def writeInRecordFile(fName):
    fh = open(recordFile,"a+",encoding="utf-8")
    fh.write(fName+'\n')
    fh.close()

def fixPathAddress(path):
    return path.replace("\\","/").strip()

def getRootAddress(file):
    fh = open(file,"r",encoding="utf-8")
    fRoot = fh.readlines()[0]
    fh.close()
    return fRoot.strip()

def getFileName(fName):
    with os.scandir('./bin/') as entries:
        for entry in entries:
            if fName == (entry.name).split('-N')[0] or fName == (entry.name).split('-Y')[0]:
                return "./bin/"+entry.name
    
def getWatchedList(file):
    fh = open(file,"r",encoding="utf-8")
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
    return SortFoo.naturalSortForTheFileLocation(allFiles,fRoot)

def writeInTrackingFile(file,item):
    fh = open(file,"a",encoding="utf-8")
    fh.write(item+"\n")
    fh.close()

def menuCore():
    fh = open(recordFile,"r",encoding="utf-8")
    allTrackers = fh.readlines()
    for i in range(len(allTrackers)):
        print(f'{i+1}. {allTrackers[i].strip()}')

def menu():
    menuCore()
    print('N. New Entry')
    return input("Enter Your Choice or (x) to exit: ")

def deleteMenu():
    menuCore()
    return input("Enter Your Choice (to Delete) or (x) to exit:")

def getAllNameFromRecord():
    fh = open(recordFile,"r",encoding="utf-8")
    return [item.strip() for item in fh.readlines()]

def findIndexOfFile(list,item):
    for i in range(len(list)):
        if item in list[i].split('/')[-1]:
            return i

def exitWait():
    input("Hit Enter to Exit/Quit: ")

def getAllSubFolders(fRoot):
    allSubFolders = []
    with os.scandir(fRoot) as entries:
        for entry in entries:
            if entry.is_dir():
                allSubFolders.append(entry.name)
    return SortFoo.naturalSortForTheFileLocation(allSubFolders,fRoot)
    # return naturalSortAlternate(allSubFolders)

def getTotalNoOfFilesInFolder(fRoot):
    count = 0
    with os.scandir(fRoot) as entries:
        for entry in entries:
            count+=1
    return count

def getTotalNoOfFilesWatched(fRoot,folderName,watchedList):
    count = 0
    for item in watchedList:
        folderNameInItem = item.split(fRoot)[1].split('/')[1]
        if folderNameInItem == folderName:
            count+=1
    return count

def getOverallWatchedPercentage(watched,notWatched):
    totalFiles = len(watched)+len(notWatched)
    return round((len(watched)/totalFiles)*100,2)

def exitWithPrompt():
    option = input(exitPromptText)
    if option in exitOptionList:
        return True
    else:
        return False