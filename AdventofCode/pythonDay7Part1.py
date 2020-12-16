bagSet = {"shiny gold"}
listOfLists = []
queue = {"shiny gold"}


class main:
    with open("inputDay7.txt", "r") as fp:
        for i in fp.readlines():
            # print(i)
            listLine = i.replace(" bags", "").replace(" bag", "").strip().split(" contain ")
            listOfLists.append(listLine)

    def bagContaining(value):
        global listOfLists
        global bagSet
        for item in listOfLists:
            if item[1].find(value) != -1:
                if not bagSet.__contains__(item[0]):
                    bagSet.add(item[0])
                    queue.add(item[0])

    while len(queue) != 0:
        temp = queue.pop()
        bagContaining(temp)
    print(len(bagSet) - 1)
