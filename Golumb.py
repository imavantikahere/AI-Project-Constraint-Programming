
import constraint

#Golumbs Puzzle
#A Golomb Ruler of order M and length L consists of M marks placed at unique intervals (i.e. integer positions) along an imaginary ruler such that the differences
#in spacing between every pair of marks are all distinct, i.e. no two pairs of marks are the same distance apart. The number of marks on the ruler
#is its order, and the largest distance between two of its marks is its length. A CSP solution gives the goloumb rulers (both optimal and imperfect) for a given
#M and L. An external loop also finds the optimal length for an M


import itertools

def solve(M,L): 
    
    problem = constraint.Problem()

    space= range(M)

    #print(space)
    problem.addVariables(space, range(L+1))

    problem.addConstraint(constraint.AllDifferentConstraint(), space)

    problem.addConstraint(lambda e: e == 0, [space[0]])

    problem.addConstraint(lambda e: e == L, [space[M-1]])

    pairs= list(itertools.combinations(space,2))


    for a in pairs:
        
            for b in pairs:

                if(a!=b):

                    problem.addConstraint(lambda x,y,r,t: abs(x-y)!= abs(r-t),[a[0],a[1],b[0],b[1]])


    solutions = problem.getSolutions()
    return solutions



#please insert the value of M and L

M=6
L=17
_sols=[]
solutions= solve(M,L)
for sol in solutions:
    element=[]
    for i in range(len(sol)):
        element.append(sol[i])
    element.sort()    
    if element not in _sols:
        
        _sols.append(element)
print("Number of solutions for M= ",M, " and L= ",L, ":",len(_sols))
print ("Solution sets are: ",_sols)



#for optimal length
l=L
while (l>0):
    final_sol= solve(M,l)
    if (M>=l):
        l=l+1
        continue
    elif( len(final_sol)==0):
        print("Optimal length= ", l+1)
        break
   
        break
    else:
        l=l-1

