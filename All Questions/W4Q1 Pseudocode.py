lists <- input
target <- input

BSEARCH(lists,target):
    first <- 0
    end <- (length of lists)-1
    while True: //infinite loop which will not end unless there is a break
        midpoint <- first + (end-first) / 2) 
        if lists[midpoint] = target:
            return(True)
            break
        else if lists[midpoint] < target:
            first <- midpoint
        else if lists[midpoint] > target:
            end <- midpoint
