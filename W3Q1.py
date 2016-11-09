string = str(input("Enter string: ")).split(" ")

def reverse(string):
    l = len(string)
    x = (l - 1)
    s = " "
    if (l <= 1):            #if list empty or 1 long, then return string
        return(s.join(string)) #convert list back to string
    else:
        return(s.join(string[::-1])) #reverses list, converts to string
print(reverse(string))
