# PART 1
fileOpen = open('Day1/inputDay1.txt', 'r')
listInt = [int(i) for i in fileOpen.readlines()]
twoValuesMult = [x * y for x in listInt for y in listInt if x + y == 2020]
print((set(twoValuesMult)).pop())
# PART 2
threeValuesMult = [
    x * y * z for x in listInt for y in listInt for z in listInt if x + y + z == 2020]
print((set(threeValuesMult)).pop())
