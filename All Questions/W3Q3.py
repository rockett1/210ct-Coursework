s = str(input("Enter a string: ")).lower()
print("You have entered: " + s)
def removeVowel(s):
    if len(s) == 0:
        return ("") #if empty return back nothing
    else:
        newstr = s[1:len(s):1]  #removes s[0] from the list on each iteration
        char = s[0]             #char at start of string
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            return(removeVowel(newstr)) # if vowel, do not add to char and repeat
        else:
            return(char + removeVowel(newstr)) # if vowel, add char to start of removeVowel and repeat

print("your string without vowels in is: " + removeVowel(s))
