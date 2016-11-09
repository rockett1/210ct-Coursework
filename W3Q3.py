s = str(input("Enter a string: ")).lower()
print(s[1:len(s)])
def removev(s):
    if len(s) == 0:
        return ("") #if empty return back nothing
    else:
        newstr = s[1:len(s)] #ignores 1st element in list
        char = s[0]
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            return removev(newstr) # if vowel, dont add to newstr and repeat
        else:
            return char + removev(newstr) # if not vowel, add to newstr and repeat

print(removev(s))
