# HELP FROM https://www.geeksforgeeks.org/find-the-first-repeated-character-in-a-string/
# https://stackoverflow.com/questions/1883980/find-the-nth-occurrence-of-substring-in-a-string
# args = ["8","abcdcbcd"]
import argparse
import sys

listSub = []
listOffset = []
args = []


def load_args():
    for current_arg in sys.argv[1:]:
        args.append(current_arg)


def firstRepeatedChar(str):
    h = {}  # Create empty hash
    for ch in str:
        if ch in h:
            return ch
        else:
            h[ch] = 0
    return "\0"


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start


def tryToAdd(substring, offset):
    for listI in zip(listSub, listOffset):
        if listI[0].find(substring) >= 0:
            endIndex = listI[1] + len(listI[0]) - 1
            endSubIndex = offset + len(substring) - 1
            if listI[1] <= offset and endIndex >= endSubIndex:
                return 0
    listSub.append(substring)
    listOffset.append(offset)


def main():
    try:
        currentSubString = list(args[1])
        for i in range(0, int(args[0])):
            currentSubString = args[1][i:]
            if firstRepeatedChar(currentSubString) != 0:
                theChar = firstRepeatedChar(currentSubString)
                if find_nth(currentSubString, theChar, 2) != -1:
                    secI = find_nth(currentSubString, theChar, 2)
                    tryToAdd(currentSubString[:secI], i)
                else:
                    tryToAdd((currentSubString), i)
        listSub.sort()
        print(" ".join(listSub))
    except:
        print("Error")


if __name__ == "__main__":
    load_args()
    main()
