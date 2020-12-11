import itertools
import math
import sys

import numpy as np

args = [
    "6 6",
    "1 2 3 4 5 6",
    "11 12 13 14 15 16",
    "21 22 23 24 25 26",
    "31 32 33 36 35 34",
    "41 42 43 44 45 46",
    "51 52 53 54 55 56",
    "9",
    "56 34 36 55 35 44 45 43 54",
]


def main(args):
    try:
        matrixList = list(args[0].split(" "))
        listMatrix = []
        m = int(matrixList[0])  # M = ROWS
        n = int(matrixList[1])  # N = COLUMNS
        for line in range(1, m + 1):
            listLine = list(args[line].split(" "))
            intLine = [int(i) for i in listLine]
            listMatrix.append(intLine)
        bigMatrix = np.array(listMatrix)
        print(bigMatrix)
        subMatrixSize = int(math.sqrt(int(args[m + 1])))
        subListLine = list(args[m + 2].split(" "))
        subIntLine = [int(i) for i in subListLine]
        counter = 0
        for currentPerm in list(itertools.permutations(subIntLine)):
            subMatrix = np.array(currentPerm).reshape([subMatrixSize, subMatrixSize])
            for x, y in itertools.product(range(n - subMatrixSize + 1), range(m - subMatrixSize + 1)):
                if np.array2string(subMatrix) == np.array2string(
                    bigMatrix[x : x + subMatrixSize, y : y + subMatrixSize]
                ):
                    print(bigMatrix[x : x + subMatrixSize, y : y + subMatrixSize])
                    return "Possible"
        return "Not Possible"
    except:
        return "Not Possible"


if __name__ == "__main__":
    print(main(args))
    print(quit)
