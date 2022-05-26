import random
randomlist = []
for i in range(0,5):
    n = random.randint(1,30)
randomlist.append(n)
print(randomlist)

import random
#Generate 3 random numbers between 1 and 1000
randomlist = random.sample(range(1, 1000), 3)
print(" Pick from these three numbers. ")
print(randomlist)


