import re


def passPortScanner():
    def validRanges(flag, value):
        eyeColorLibrary = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if flag == "byr":
            return 1 if (1920 <= int(value) <= 2002) else 0
        elif flag == "iyr":
            return 1 if (2010 <= int(value) <= 2020) else 0
        elif flag == "eyr":
            return 1 if (2020 <= int(value) <= 2030) else 0
            ## HEIGHT WILL HAVE TO DOUBLE CHECK
        elif flag == "hgt":
            ## IF CM 150 <= 193
            if value.find("cm") != -1:
                return 1 if (150 <= int(value[:-2]) <= 193) else 0
            ## IF IN 59 <=76
            elif value.find("in") != -1:
                return 1 if (59 <= int(value[:-2]) <= 76) else 0
            else:
                return 0

            ##SPECIAL REGEX TOO
        elif flag == "hcl":
            return 1 if re.search(r"^[#][0-9a-f]{6}$", value) else 0
        elif flag == "ecl":
            return 1 if eyeColorLibrary.count(value) != 0 else 0
        elif flag == "pid":
            return 1 if re.search(r"^[0-9]{9}$", value) else 0
        return 0

    def confirmValid(currPassport):
        returnVal = 1
        flags = {"byr": 0, "iyr": 0, "eyr": 0, "hgt": 0, "hcl": 0, "ecl": 0, "pid": 0}
        for currField in currPassport:
            if currField[0] != "cid":
                flags[str(currField[0])] = validRanges(str(currField[0]), currField[1])
        for items in flags.values():
            returnVal = returnVal & items
        print(flags)
        return returnVal

    allPassports = []
    validPassports = 0
    with open("inputDay4.txt", "r") as fp:
        lineBuilder = ""
        for line in fp:
            if line != "\n":
                lineBuilder += line.strip() + " "
            else:
                allPassports.append(lineBuilder[:-1])
                lineBuilder = ""
        allPassports.append(lineBuilder[:-1])
    for currLine in allPassports:
        preList = [preLine.split(":") for preLine in currLine.split(" ")]
        validPassports += confirmValid(preList)
    print(validPassports)


passPortScanner()
