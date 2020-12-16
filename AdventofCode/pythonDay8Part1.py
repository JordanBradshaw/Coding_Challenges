accumCounter = 0
listIndex = 0
hashList = []


with open("inputDay8.txt", "r") as f:
    fileList = []
    for i in f.readlines():
        listTuple = i.replace("\n", "").split(" ")
        fileList.append(listTuple)
print(fileList)

while True:
    if fileList[listIndex][0] == "acc":
        if hashList.count(listIndex) == 0:
            hashList.append(listIndex)
            accumCounter += int(fileList[listIndex][1])
            print(fileList[listIndex])
            listIndex += 1
        else:
            break
    if fileList[listIndex][0] == "jmp":
        if hashList.count(listIndex) == 0:
            hashList.append(listIndex)
            print(fileList[listIndex])
            listIndex += int(fileList[listIndex][1])
        else:
            break
    if fileList[listIndex][0] == "nop":
        if hashList.count(listIndex) == 0:
            hashList.append(listIndex)
            print(fileList[listIndex])
            listIndex += 1
        else:
            break
print(accumCounter)
