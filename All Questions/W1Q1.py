import random

numarray = input("enter a list of numbers seperated by comma's: ").split(",")

length = len(numarray)
x = (length - 1)
z = random.randint(0,x)

for i in range(x,-1,-1):
    numarray[z],numarray[i] = numarray[i],numarray[z]   #swaps current position of element with random position to shuffle list
print(numarray)

'''I decided to use a for loop to swap the position of each node in the
numarray, it does this for each element atleast once, using the random
module, i use the rng to create only numbers in range of the numarray'''
    



