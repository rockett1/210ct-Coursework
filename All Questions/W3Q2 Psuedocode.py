n1 <- input("enter a number to check if its prime: ")

l1 <- n1 - 1
PRIME(n, n2):
    if (n <= 1):
	    RETURN("Not prime")
    else:
	    if (n modulo n2 = 0):
		    RETURN("not prime")
	    elif (n modulo n2 ≠ 0 and n2 ≠ 2):
		    PRIME(n, n2 - 1) #if remainder not equal to 0 and n2 not equal to 2, n2 -1 and recurse
	    elif (n modulo n2 ≠ 0 and n2 = 2):
		    RETURN("Prime")   #if n2 is 2 and remainder not 0, number is prime

