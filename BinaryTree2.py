from itertools import islice
from math import floor, ceil


def busquedaBinaria(num, fileName, blockSize):
    file = open(fileName, "r")
    max = 0
    for ignoredLine in file:
        max += 1
    max -= 1
    numberOfBlocks = ceil((max + 1) / blockSize)
    IOCount = 0
    return search(num, 0, numberOfBlocks - 1, file, blockSize, max, IOCount)


def readBlock(index, file, blockSize, maxIndex):
    file.seek(0)
    for ignoredLine in islice(file, index * blockSize):
        pass
    block = []
    for i in range(blockSize):
        if index * blockSize + i > maxIndex:
            break
        number = file.readline()
        block.append(int(number))
    return block


def search(num, min, max, file, blockSize, maxIndex, IOCount):
    if max < min:
        return False, IOCount

    middleIndex = floor((max + min) / 2)
    middleBlock = readBlock(middleIndex, file, blockSize, maxIndex)
    IOCount += 1

    if num < middleBlock[0]:
        return search(num, min, middleIndex - 1, file, blockSize, maxIndex, IOCount)
    if num > middleBlock[-1]:
        return search(num, middleIndex + 1, max, file, blockSize, maxIndex, IOCount)
    for number in middleBlock:
        if number == num:
            return True, IOCount
    return False, IOCount
