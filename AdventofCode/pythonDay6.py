class questionCounter:
    numOfQuestions = 0
    numOfQuestionsP2 = 0
    concatString = ""
    charRange = []
    for i in range(97, 123):
        charRange.append(chr(i))
    with open("inputDay6.txt", "r") as fp:
        for currentChar in fp.read():
            concatString += currentChar
        concatListPart1 = [i.replace("\n", "") for i in concatString.split("\n\n")]
        for element in concatListPart1:
            for question in charRange:
                numOfQuestions += 1 if element.count(question) > 0 else 0
    ## ! SO I CAN SEE HOW MANY ROWS
    concatString = concatString.replace("\n\n", "!\n\n")
    concatListPart2 = [i.replace("\n", "!") for i in concatString.split("\n\n")]
    for element in concatListPart2:
        baseRow = element.count("!")
        for question in charRange:
            numOfQuestionsP2 += 1 if element.count(question) is baseRow else 0
    print(f"Part 1 :{numOfQuestions}")
    print(f"Part 2 :{numOfQuestionsP2}")
