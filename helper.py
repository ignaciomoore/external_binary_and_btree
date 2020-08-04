import random
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import BinaryTree2
import BTree


def createRandomNumbers(size, outputFile):
    data = []
    for j in range(size):
        data.append(random.randint(1, size))
    data.sort()

    file = open(outputFile, "w")
    for num in data[:-1]:
        file.write(str(num) + "\n")
    file.write(str(data[-1]))
    file.close()


def createTree(inputFileName, blockSize):
    tree = BTree.BTree(blockSize)
    file = open(inputFileName, "r")
    input = []
    while True:
        num = file.readline()
        if not num:
            break
        num = int(num.replace("\n", ""))
        input.append(num)
    random.shuffle(input)
    for j in input:
        tree.insert(j)
    #tree.write()
    aux1 = inputFileName.split(".")
    aux2 = aux1[0].split("_")
    outName = "output/" + aux2[0] + "_B" + str(blockSize) + "_B-Tree." + aux1[1]
    tree.write(outName)
    return outName, tree.root.id


inputSizes = [pow(10, 2), pow(10, 3), pow(10, 4), pow(10, 5)]

blockSizes = [pow(2, 4), pow(2, 5), pow(2, 6), pow(2, 7), pow(2, 8),
              pow(2, 9), pow(2, 10), pow(2, 11), pow(2, 12)]

fileNames = []
for i in range(inputSizes.__len__()):
    fileNames.append("10^" + str(i + 2) + "_input.txt")

for i in range(inputSizes.__len__()):
    createRandomNumbers(inputSizes[i], fileNames[i])


def getData(num):

    dataInputSizes = []
    dataBlockSizes = []
    dataTreeType = []
    dataExeTime = []
    dataIOCount = []
    dataResults = []
    dataSearchedNum = []

    for inputIndex in range(inputSizes.__len__()):

        randomNumber = random.randint(1, inputSizes[inputIndex])

        for blockSize in blockSizes:

            outName, rootID = createTree(fileNames[inputIndex], blockSize)

            ''' B-TREE SEARCH ANALYSIS '''

            dataInputSizes.append(inputSizes[inputIndex])
            dataBlockSizes.append(blockSize)

            btreeStartTime = time.time()

            btreeResult, btreeIO = BTree.searchBTree(randomNumber, outName)
            btreeExeTime = time.time() - btreeStartTime

            dataExeTime.append(btreeExeTime * 1000)
            dataIOCount.append(btreeIO)
            dataResults.append(btreeResult)
            dataTreeType.append("B-Tree")
            dataSearchedNum.append(randomNumber)

        ''' BINARY SEARCH ANALYSIS '''

        dataInputSizes.append(inputSizes[inputIndex])
        dataBlockSizes.append(1)

        binaryStartTime = time.time()

        binaryResult, binaryIO = BinaryTree2.busquedaBinaria(randomNumber, fileNames[inputIndex], 1)
        binaryExeTime = time.time() - binaryStartTime

        dataExeTime.append(binaryExeTime * 1000)
        dataIOCount.append(binaryIO)
        dataResults.append(binaryResult)
        dataTreeType.append("Binary")
        dataSearchedNum.append(randomNumber)

    data = {"InputSize": dataInputSizes,
            "BlockSize": dataBlockSizes,
            "TreeType": dataTreeType,
            "ExecutionTime": dataExeTime,
            "InOutCount": dataIOCount,
            "Result": dataResults,
            "SearchedNum": dataSearchedNum}

    df = pd.DataFrame(data, columns=["InputSize", "BlockSize", "TreeType", "ExecutionTime", "InOutCount", "Result", "SearchedNum"])
    df.to_csv("analysis_%d.csv" % num)


def getGraphs():
    df = pd.read_csv("analysis_1.csv", header=0)

    for j in range(2,11):
        name = "analysis_" + str(j) + ".csv"
        df_aux = pd.read_csv(name)
        df = pd.concat([df, df_aux])

    df["Base10"] = np.log10(df["InputSize"])

    dfBinary = df.loc[df.TreeType == "Binary", ["InputSize", "BlockSize", "TreeType", "Base10", "ExecutionTime", "InOutCount"]]
    dfBinary = dfBinary.groupby(["InputSize", "BlockSize", "TreeType"])["Base10", "ExecutionTime", "InOutCount"].mean()
    dfBinary = dfBinary[["Base10", "ExecutionTime", "InOutCount"]]

    dfB16 = df.loc[df.BlockSize == 16, ["InputSize", "BlockSize", "TreeType", "Base10", "ExecutionTime", "InOutCount"]]
    dfB16 = dfB16.groupby(["InputSize", "BlockSize", "TreeType"])["Base10", "ExecutionTime", "InOutCount"].mean()
    dfB16 = dfB16[["Base10", "ExecutionTime", "InOutCount"]]

    dfB32 = df.loc[df.BlockSize == 32, ["InputSize", "BlockSize", "TreeType", "Base10", "ExecutionTime", "InOutCount"]]
    dfB32 = dfB32.groupby(["InputSize", "BlockSize", "TreeType"])["Base10", "ExecutionTime", "InOutCount"].mean()
    dfB32 = dfB32[["Base10", "ExecutionTime", "InOutCount"]]

    dfB64 = df.loc[df.BlockSize == 64, ["InputSize", "BlockSize", "TreeType", "Base10", "ExecutionTime", "InOutCount"]]
    dfB64 = dfB64.groupby(["InputSize", "BlockSize", "TreeType"])["Base10", "ExecutionTime", "InOutCount"].mean()
    dfB64 = dfB64[["Base10", "ExecutionTime", "InOutCount"]]

    dfB128 = df.loc[df.BlockSize == 128, ["InputSize", "BlockSize", "TreeType", "Base10", "ExecutionTime", "InOutCount"]]
    dfB128 = dfB128.groupby(["InputSize", "BlockSize", "TreeType"])["Base10", "ExecutionTime", "InOutCount"].mean()
    dfB128 = dfB128[["Base10", "ExecutionTime", "InOutCount"]]

    dfB256 = df.loc[df.BlockSize == 256, ["InputSize", "BlockSize", "TreeType", "Base10", "ExecutionTime", "InOutCount"]]
    dfB256 = dfB256.groupby(["InputSize", "BlockSize", "TreeType"])["Base10", "ExecutionTime", "InOutCount"].mean()
    dfB256 = dfB256[["Base10", "ExecutionTime", "InOutCount"]]

    dfB512 = df.loc[df.BlockSize == 512, ["InputSize", "BlockSize", "TreeType", "Base10", "ExecutionTime", "InOutCount"]]
    dfB512 = dfB512.groupby(["InputSize", "BlockSize", "TreeType"])["Base10", "ExecutionTime", "InOutCount"].mean()
    dfB512 = dfB512[["Base10", "ExecutionTime", "InOutCount"]]

    dfB1024 = df.loc[df.BlockSize == 1024, ["InputSize", "BlockSize", "TreeType", "Base10", "ExecutionTime", "InOutCount"]]
    dfB1024 = dfB1024.groupby(["InputSize", "BlockSize", "TreeType"])["Base10", "ExecutionTime", "InOutCount"].mean()
    dfB1024 = dfB1024[["Base10", "ExecutionTime", "InOutCount"]]

    dfB2048 = df.loc[df.BlockSize == 2048, ["InputSize", "BlockSize", "TreeType", "Base10", "ExecutionTime", "InOutCount"]]
    dfB2048 = dfB2048.groupby(["InputSize", "BlockSize", "TreeType"])["Base10", "ExecutionTime", "InOutCount"].mean()
    dfB2048 = dfB2048[["Base10", "ExecutionTime", "InOutCount"]]

    dfB4096 = df.loc[df.BlockSize == 4096, ["InputSize", "BlockSize", "TreeType", "Base10", "ExecutionTime", "InOutCount"]]
    dfB4096 = dfB4096.groupby(["InputSize", "BlockSize", "TreeType"])["Base10", "ExecutionTime", "InOutCount"].mean()
    dfB4096 = dfB4096[["Base10", "ExecutionTime", "InOutCount"]]

    lines = [dfB16, dfB32, dfB64, dfB128, dfB256, dfB512, dfB1024, dfB2048, dfB4096]
    colours = ["tab:red", "tab:green", "tab:orange", "tab:purple", "tab:pink",
               "tab:olive", "tab:cyan", "tab:brown", "tab:gray"]

    ''' FIRST GRAPH '''

    ax = plt.gca()
    dfBinary.plot(kind="line", x="Base10", y="InOutCount", ax=ax, color="tab:blue", label="Binary Search")

    for j in range(len(lines)):
        label = "B = " + str(int(pow(2, j + 4)))
        lines[j].plot(kind="line", x="Base10", y="InOutCount", color=colours[j], ax=ax, label=label)

    ax.set(ylabel="Average I/Os", xlabel="Input Size (Log-Base 10)")
    plt.savefig("InOut with Binary.png")
    plt.show()

    ''' SECOND GRAPH '''

    ax2 = plt.gca()
    dfBinary.plot(kind="line", x="Base10", y="ExecutionTime", ax=ax2, color="tab:blue", label="Binary Search")

    for j in range(len(lines)):
        label = "B = " + str(int(pow(2, j + 4)))
        lines[j].plot(kind="line", x="Base10", y="ExecutionTime", color=colours[j], ax=ax2, label=label)

    ax2.set(ylabel="Average Execution Time (Milliseconds)", xlabel="Input Size (Log-Base 10)")
    plt.savefig("Time with Binary.png")
    plt.show()

    ''' THIRD GRAPH '''

    ax3 = plt.gca()
    for j in range(len(lines)):
        label = "B = " + str(int(pow(2, j + 4)))
        lines[j].plot(kind="line", x="Base10", y="InOutCount", color=colours[j], ax=ax3, label=label)

    ax3.set(ylabel="Average I/Os", xlabel="Input Size (Log-Base 10)")
    plt.savefig("InOut without Binary.png")
    plt.show()

    ''' FOURTH GRAPH '''

    ax4 = plt.gca()
    for j in range(len(lines)):
        label = "B = " + str(int(pow(2, j + 4)))
        lines[j].plot(kind="line", x="Base10", y="ExecutionTime", color=colours[j], ax=ax4, label=label)

    ax4.set(ylabel="Average Execution Time (Milliseconds)", xlabel="Input Size (Log-Base 10)")
    plt.savefig("Time without Binary.png")
    plt.show()


start = time.time()

for i in range(10):
    getData(i + 1)

getGraphs()
print("Execution Time: %d seconds" % round(time.time() - start, 2))
