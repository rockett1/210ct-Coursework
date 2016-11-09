string <- input.split(" ")

REVERSE(string):                            
    len <- length of (string)               //(1)
    x <- (len - 1)                          //(1)
    s <- " "                                //(1)
    IF (len <= 1):                          //(1)
        RETURN s.join(string)               //(1)
    ELSE:                                   //(n)
        RETURN s.join(string[::-1])         //(n)

OUTPUT(REVERSE(string))

//Big O = O(n)
