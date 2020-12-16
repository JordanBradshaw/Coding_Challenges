adapterList = []
valid1JoultAdapters = []
valid3JoultAdapters = []
with open("inputDay10.txt", "r") as f:
    for line in f.readlines():
        adapterList.append(int(line.strip()))

adapterList.sort()
print(adapterList)
previousAdapter = 0
for currentAdapter in adapterList:
    if currentAdapter <= previousAdapter + 1:
        valid1JoultAdapters.append(currentAdapter)
        previousAdapter = currentAdapter
    elif currentAdapter <= previousAdapter + 3:
        valid3JoultAdapters.append(currentAdapter)
        previousAdapter = currentAdapter
    else:
        break
print(valid1JoultAdapters)
print(valid3JoultAdapters)
print("Valid 1 count * Valid 3 count:")
print(f"{len(valid1JoultAdapters)} : {len(valid3JoultAdapters)+1}")
print(len(valid1JoultAdapters) * (len(valid3JoultAdapters) + 1))
