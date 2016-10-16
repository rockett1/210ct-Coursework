n = int(input("input a number to factorialise: "))

def factorialise(n):
    x = 1
    for i in range(n,0,-1):
        x = x * i
    print(x)

def counting0(n):
    y = 1
    z = 0
    while (n >= y):
        y *= 5 #each iteration changes y value by multiplying by 5
        z += (n // y) #each iteration adds up n//y
    print("The number of trailing 0's is: " + str(z))

factorialise(n)
counting0(n)




