import numpy as np
from random import randint
import time
import copy

randomDict = {1:[0,0],2:[0,1],3:[1,0],4:[1,1]}

data = []
f = open('randTest2.csv','w')
header = ','.join('Column ' + str(x) for x in range(0,102))
f.write(header + ',ClassLabel\n')

for i in range(0,900):
    dictIndex = randint(1, 4)
    randArray = copy.deepcopy(randomDict[dictIndex])
    for j in range(0,100):
        valIndex = randint(0, 255)
        randArray.append(valIndex)
    randArray.append(dictIndex)
    strVal = ','.join(str(x) for x in randArray)
    f.write(strVal + '\n')

f.close()


