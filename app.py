from flask import Flask, render_template, request

def levenshtein(s1, s2):
    #Create the cot matrix to store the results of the subproblems.
    #Dimensions are (len(s1) + 1) x (len(s2) + 1).
    D = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    #Initialization of the first row and first column.
    #The distance from a string to an empty string is its own size (only insertions/deletions).
    for i in range(len(s1) + 1):
        D[i][0] = i
    for j in range(len(s2) + 1):
        D[0][j] = j

    #Fill the rest of the matrix
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            #Cost of substitution (0 if the characters are equal, 1 if different)
            cost = 0 if s1[i -1] == s2[j - 1] else 1

            #The distance dp[i][j] is the minimum between three possible operations:
            #1. Deletion: dp[i-1][j] + 1
            #2. Insertion: dp[i][j-1] + 1
            #3. Replacement: dp[i-1][j-1] + cost
            D[i][j] = min(D[i - 1][j] + 1,          #Deletion
                          D[i][j -1] + 1,           #Insertion
                          D[i - 1][j - 1] + cost)   #Replacement
                            
    #The final result is in the lower right corner of the matrix
    return D[len(s1)][len(s2)]