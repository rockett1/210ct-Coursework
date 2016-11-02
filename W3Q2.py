n1 = int(input("enter a number to check if its prime: "))

l1 = n1 - 1
def prime(n, n2):
	if (n <= 1):
		print("Not prime")
	else:
		if (n % n2 == 0):
			print("not prime")
		elif (n % n2 != 0 and n2 != 2):
			prime(n, n2 - 1) #if remainder not equal to 0 and n2 not equal to 2, n2 -1 and recurse
		elif (n % n2 != 0 and n2 == 2):
			print("Prime")   #if n2 is 2 and remainder not 0, number is prime
			
prime(n1, l1)


