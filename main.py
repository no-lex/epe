import math
import random
import randomint
import transforms

randomint.randomintrange(5, 0, 10)

num = 4
poslist = []
# 12/3 = 4 <- 4-deep tree
for i in range(num*3):
    emptyrow = []
    for j in range(num*3):
        emptyrow.append(0)
    poslist.append(list(emptyrow))

print(poslist)

momentalist = []
# 12/3 = 4 <- 4-deep tree
for i in range(num*3):
    emptyrow = []
    for j in range(num*3):
        emptyrow.append(0)
    momentalist.append(list(emptyrow))

print(poslist)

#momenta creation

print(transforms.momentasplit(1,0,0))