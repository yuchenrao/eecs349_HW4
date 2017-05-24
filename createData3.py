
from random import randint
import copy

randomDict = {1:[0,0],2:[0,1],3:[1,0],4:[1,1]}

data = []
f = open('q2.csv','w')
header = ','.join('Column ' + str(x) for x in range(0,100))
f.write(header + ',ClassLabel\n')

for i in range(0,999):
    dictIndex = randint(1, 4)
    randArray = copy.deepcopy(randomDict[dictIndex])
    for j in range(0,98):
        if j % 2 == 0:
            randArray.append(randArray[0])
        else:
            randArray.append(randArray[1])
    randArray.append(dictIndex)
    strVal = ','.join(str(x) for x in randArray)
    print strVal

    f.write(strVal + '\n')

f.close()


