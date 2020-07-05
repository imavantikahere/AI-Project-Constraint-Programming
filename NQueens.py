##-Avantika Poddar-73131-


##Mariam Tanzeel-61915-


##Shatha Abduh-66003-


##Mohammed AlZaabi-65549

import constraint
from time import perf_counter


def printOneSolution(table):
    print("----------------------------------------------")
    for i in range(0,len(table[0]),1):
        for j in range(0,len(table[0]),1):
            if(table[i][j] == ' '):
                print('_', end =" ")
            else:
                print(table[i][j], end = " ")
        print("\n", end = "")
#Function: To print the table obtained in "tabulateAnswer"
#input: 2d list of characters representing a single solution
#output: 2d list printed in terminal
        
import random
def defineNQueenProblem(numberOfQueens):
    cols = range(numberOfQueens)
    rows = range(numberOfQueens)
    problem = constraint.Problem()
    problem.addVariables(cols, rows)
    for col1 in cols:
        for col2 in cols:
            if col1 < col2:
                problem.addConstraint(lambda row1 , row2 , col1 = col1, col2 = col2 : 
                abs(row1-row2) != abs(col1-col2) and
                row1 != row2, (col1,col2))
    
    return problem
#Function: To formulate a mutable NQueen problem
#input: number of Queens in the puzzle board
#output: NQueen Problem of with "numberOfQueens" Queen Pieces



#This is the iterative version 
def defineNQueenIterative(numberOfQueens):
    cols = range(numberOfQueens)
    rows = range(numberOfQueens)
    problem = constraint.Problem(constraint.MinConflictsSolver())
    problem.addVariables(cols, rows)
    for col1 in cols:
        for col2 in cols:
            if col1 < col2:
                problem.addConstraint(lambda row1 , row2 , col1 = col1, col2 = col2 : 
                abs(row1-row2) != abs(col1-col2) and
                row1 != row2, (col1,col2))
    
    return problem


    
###finding the solution to NQueens of 8 
##problem = defineNQueenProblem(8)
##solutions = problem.getSolutions()
##for i in range(0,len(solutions),1):
##    printOneSolution(tabulateAnswer(solutions[i]))
N=4
#performance calculation
print("Number of Queens\t\t\tElapsed time (s)")

flag=1
t1_incremental=0
print("Incremental Approach")
while True:
    problem = defineNQueenProblem(N)
    t1_start = perf_counter()
    solutions = problem.getSolution()
    t1_stop = perf_counter()
    t1_incremental= t1_stop- t1_start
    print(N,"\t\t\t",t1_incremental)
    if(t1_incremental>0.80): break
    
    N=N+1
    
print ("Iterative approach")
N=4
while True:
    problem1 = defineNQueenIterative(N)
    t2_start=perf_counter()
    solutions1= problem1.getSolution()
    t2_stop=perf_counter()
    t2_incremental= t2_stop- t2_start
    print(N,"\t\t\t", t2_incremental)
    N= N+1
    if (t2_incremental>1): break

