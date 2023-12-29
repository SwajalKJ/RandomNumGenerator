#genrate random number

#gives random float number between 0 and 1
import random
num = random.random()
print(num)

#gives random float number between 0 and range given
import random
num = random.uniform(0,100)
print(num)

#gives random int number between 0 and range given
import random
num = random.randint(0,100)
print(num)

#gives random number between 0 and range given in increment order
import random
num = random.randrange(0,100,2)
print(num)

#gives random series
import random
numlist = random.sample(range(0,100), 3)
print(numlist)