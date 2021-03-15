import re


def naturalSortForTheFileLocation(l, fRoot):
    def removeNullStringFromTheList(listContainingNullString):
        _ = []
        for item in listContainingNullString:
            if item == '':
                continue
            else:
                _.append(item)
        return _

    def parseIntTo8DigitString(i):
        digit = 8
        iDigits = len(str(i))
        bufferZero = '0'*(8-iDigits)
        return bufferZero+str(i)

    def convert(x):
        return int(x) if x.isdigit() else x.lower()

    def alphaNumList(string):
        return [convert(x) for x in re.split('([0-9]+)', string)]

    def extractSubfolderLengthFromString(string):
        subFolderString = string.split(fRoot+"/")[1].split('/')[0]
        alphaNumSubFolderList = removeNullStringFromTheList(
            alphaNumList(subFolderString))
        return len(alphaNumSubFolderList)

    def getMaxSubFolderLength():
        _ = None
        for item in l:
            itemLen = extractSubfolderLengthFromString(item)
            if (_ == None or _ < itemLen):
                _ = itemLen
        return _

    def getListForSorting(string):
        _ = string.split(fRoot+"/")[1].split('/')
        _ = [alphaNumList(x) for x in _]
        tempList = []
        for item in _:
            tempList += item
        return removeNullStringFromTheList(tempList)

    maxSubFolderLength = getMaxSubFolderLength()

    def parseIntInTheList(listContainingInt):
        _ = []
        for item in listContainingInt:
            if isinstance(item, int):
                _.append(parseIntTo8DigitString(item))
            else:
                _.append(item)
        return _

    def generateListWithBuffer(item, maxLenght=maxSubFolderLength):
        itemList = getListForSorting(item)
        subFolderLength = extractSubfolderLengthFromString(item)
        for _ in range(maxLenght-subFolderLength):
            itemList.insert(subFolderLength, '')
        itemList = parseIntInTheList(itemList)
        return itemList

    l.sort(key=generateListWithBuffer)
