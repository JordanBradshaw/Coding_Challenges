
def main(argv):
    # PART 1
    def checkValid1(listPass):
        currPass = listPass[3].count(listPass[2])
        if currPass >= int(listPass[0]) and currPass <= int(listPass[1]):
            return 1
        else:
            return 0

    # PART 2
    def checkValid2(listPass):
        currLetter = listPass[2]
        svar = listPass[3]
        i1 = int(listPass[0]) - 1
        i2 = int(listPass[1]) - 1
        if (svar[i1] is currLetter) ^ (svar[i2] is currLetter):
            return 1
        else:
            return 0
    # FILE WORK
    openFile = open('Day2/inputDay2.txt', 'r')
    i, i2counters = 0, 0
    for line in openFile.readlines():
        line = line.replace('-', ' ')
        line = line.replace(':', ' ')
        lineList = line.split()
        i += checkValid1(lineList)
        i2counters += checkValid2(lineList)
    print(f'Part 1 counter = {i}')
    print(f'Part 2 counter = {i2counters}')


if __name__ == "__main__":
    main(None)
