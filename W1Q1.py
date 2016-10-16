import random

numarray = input("enter a list of numbers seperated by comma's: ").split(",")

length = len(numarray)
x = (length - 1)
z = random.randint(0,x)

for i in range(x,-1,-1):
    numarray[z],numarray[i] = numarray[i],numarray[z]
print(numarray)


    



