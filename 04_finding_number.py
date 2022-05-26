import random

#Generate 3 random numbers between 1 and 1000
random.list = random.sample(range(1, 1000), 3)
print(" Pick from these three numbers. ")
print(random.list)

secret = random.randint(random.list)
print(secret)

