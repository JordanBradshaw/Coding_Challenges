import math


class main:
    seatList = []

    with open("inputDay5.txt", "r") as fp:
        fileList = fp.readlines()

    def seatCalculation(binaryString):
        rows = list(range(127))
        for i in binaryString[:7]:
            if i == "F":
                rows = rows[: math.ceil(len(rows) / 2)]
            elif i == "B":
                rows = rows[math.ceil(len(rows) / 2) :]
            # print(rows)
        seats = list(range(8))
        for i in binaryString[7:]:
            if i == "L":
                seats = seats[: math.ceil(len(seats) / 2)]
            elif i == "R":
                seats = seats[math.ceil(len(seats) / 2) :]
        return (int(str(rows[0])) * 8) + seats[0]

    for currString in fileList:
        seatList.append(seatCalculation(currString))
    print(sorted(seatList))
    totalSeats = list(range(7, 908))
    print(set(totalSeats) - set(seatList))
