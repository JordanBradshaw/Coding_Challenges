with open("inputDay9.txt") as f:
    intList = []
    for line in f.readlines():
        intList.append(int(line.strip()))


def main():
    for i in range(25, len(intList)):
        passFlag = False
        for x, y in [(x, y) for x in intList[i - 25 : i] for y in intList[i - 25 : i] if x != y]:
            if x + y == intList[i]:
                # print(x + y)
                passFlag = True
                break
        if passFlag is False:
            return intList[i]


targetInt = 20874512


def part2():  ## THE ANSWER WAS 20874512 (Part 2) Wants >2 continuous numbers that sum to this value
    contList = []
    for i in range(0, len(intList)):
        contList.clear()
        for offset in range(i, len(intList)):
            contList.append(intList[offset])
            listSum = sum(contList)
            if listSum == targetInt:
                return contList
            elif listSum > targetInt:
                break


print("Part 1:")
print(main())

print("Part 2:")
part2return = part2()
print(min(part2return) + max(part2return))
