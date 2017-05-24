from random import randint
import numpy as np

data = []
f = open('qtest.csv','w')
header = ','.join('Column ' + str(x) for x in range(0,2))
f.write(header + ',ClassLabel\n')

for i in range(0,1000):
    randArray = [randint(0, 5),randint(0, 5)]
    # for j in range(0,1):
    #     randArray.append(randint(0,5))
    randArray.append(randArray[0] + randArray[1])
    strVal = ','.join(str(x) for x in randArray)
    print strVal
    f.write(strVal + '\n')
f.close()


