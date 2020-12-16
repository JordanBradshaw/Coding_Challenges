# PART 2
def calcTrees2():
    totalTrees = 1
    diffSlopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for x, y in diffSlopes:
        totalTrees *= calcTrees2Function(x, y)
    return totalTrees


def calcTrees2Function(x, y):
    numTrees, index = 0, 0
    file = open("inputDay3.txt", "r")
    width = len(file.readline().strip())
    file.seek(0)
    lineList = file.readlines()
    rows = len(lineList)
    for row in range(0, rows):
        if row % y == 0:
            line = lineList[row].strip()
            print(line[:index] + " " + line[index + 1 :])
            treeOrNot = 1 if line[index] == "#" else 0
            numTrees += treeOrNot
            index = (index + x) % width
    return numTrees


### PART 1
def calcTrees1():
    numTrees = 0
    index = 0
    row = 1
    file = open("inputDay3.txt", "r")
    width = len(file.readline().strip())
    file.seek(0)
    for line in file.readlines():
        line = line.strip()
        print(line[:index] + " " + line[index + 1 :])
        treeOrNot = 1 if line[index] == "#" else 0
        numTrees += treeOrNot
        index = (index + 3) % width
        row += 1
    return numTrees


print(calcTrees2())
