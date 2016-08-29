
import random


# rooms = [4,3,5,7,10,3,10,3,7]
# size = [3,10,7,9,16,1,9,12,12]

def greedy(rooms,size):
    spaceNeeded = 0
    deltaSpace = 0
    for i in range(len(rooms)):
        deltaSpace += size[i] - rooms[i]
    print("Delta: ", deltaSpace)
    while rooms:
        curMax = rooms.index(max(rooms))
        if size[curMax] - max(rooms) > 0:
            deltaSpace -= size[curMax] - max(rooms)
        else:
            deltaSpace += size[curMax] - max(rooms)
        print("DeltaSpace: ",deltaSpace)
        if max(rooms) > deltaSpace + spaceNeeded:
            spaceNeeded += max(rooms) - (deltaSpace + spaceNeeded)
            print("SpaceNeeded: ",spaceNeeded)
        del rooms[curMax]
        del size[curMax]
    return spaceNeeded

for a in range(1,10):
    n = random.randint(1,10)
    roomtest = []
    sizetest = []
    print("\nCase:",a)
    for b in range(1,n):
        size = random.randint(1,10)
        roomtest.append(size)
        sizetest.append(random.randint(-size,10)+size)
    print(roomtest)
    print(sizetest)
    print(greedy(roomtest,sizetest))







