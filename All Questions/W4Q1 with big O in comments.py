lists = input("enter a list to binary search through (seperated with spaces): ").split(" ")
target = input("enter target to find:" )

def bsearch(lists, target):
    first = 0
    end = len(lists)-1
    while True:                                 #O(n)
        midpoint = first + ((end-first) // 2)   #n      sets midpoint to midway on each iteration
        if lists[midpoint] == target:           #n      checks if found target
            return(True)                        
            break
        elif lists[end] == target:              #n
            return(True)
            break
        elif lists[midpoint] < target:          #n      if not target change variables and carry on looping through
            first = midpoint
        elif lists[midpoint] > target:          #n
            end = midpoint

print(bsearch(lists, target))

