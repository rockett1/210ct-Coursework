L = [1,2,3,4,5,6,7,8,1,5,1,3,6,7,8,9,2,1]

def subseq(L):
    dic = {'Longest_Increasing_Sub-sequence':['1']}
    tempList = []
    i = 0
    while i < (len(L)-1):   
        if (L[i] < L[i+1]):
            tempList.append(L[i])
        else:
            tempList.append(L[i])   #adds last number parsed into templist to complete sub string
            if len(dic['Longest_Increasing_Sub-sequence']) < len(tempList): #compares if new substring is longer than one stored in dictionary
                print(tempList)
                dic['Longest_Increasing_Sub-sequence'] = tempList #sets dictionary key = to new longest increasing sub seq
            tempList = []
        i += 1
    print(dic)
            

subseq(L)
