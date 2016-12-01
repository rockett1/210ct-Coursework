s = input("Enter a string: ")
convert s to lower case
RETURN("You have entered: " + s)
REMOVEVOWEL(s):
    if length of(s) = 0:
        RETURN() #if empty return back nothing
    else:
        newstr <- s[1:length of(s):1]  #removes s[0] from the list on each iteration
        char <- s[0]             #char at start of string
        if char = "a" or char = "e" or char = "i" or char = "o" or char = "u":
            RETURN(REMOVEVOWEL(newstr)) # if vowel, do not add to char and repeat
        else:
            return(char + REMOVEVOWEL(newstr)) # if vowel, add char to start of removeVowel and repeat

RETURN("your string without vowels in is: " + removeVowel(s))
