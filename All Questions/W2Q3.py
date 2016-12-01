m1 = [[1,2,3],[4,5,6]]
m2 = [[7,8,9],[10,11,12]]

ADDITION(i,j)
    for each row in m1:
        for each column in m1:
            addition[i][j] <- m1[i][j] + m2[i][j]
    return(addition)

//big O for addition is O(n)^2

SUBTRACTION(i,j)
    for each row in m1:
        for each column in m2:
            subtract[i][j] <- m1[i][j] - m2[i][j]
    return(subtract)

//big O for subtraction is O(n)^2

MULTIPLICATION(i,j)
    //A=B*C-2*(B+C)
    //result = m1*m2-2*(m1+m2)
    for each row (i) in B:
        for each column (j) in C:
            for each row (k) in C:
                A[i][j] +<- B[i][k] * C[k][j]
    return(A)

//big O for multiplication is O(n)^3


