lists = input("enter a list to binary search through (seperated with spaces): ").split(" ")
target = input("enter target to find:" )

def bsearch(lists, target):
    first = 0
    end = len(lists)-1
    while True:                                 #O(n)
        midpoint = first + ((end-first) // 2)   #n
        if lists[midpoint] == target:           #n
            return(True)                        
            break
        elif lists[end] == target:              #n
            return(True)
            break
        elif lists[midpoint] < target:          #n
            first = midpoint
        elif lists[midpoint] > target:          #n
            end = midpoint

print(bsearch(lists, target))

