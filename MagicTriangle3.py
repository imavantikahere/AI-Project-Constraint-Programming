


import constraint

def solve(S):
    
    problem = constraint.Problem()

    #name the circles as A,B,C,D,E,F FROM 1-6

    problem.addVariable(("A"),range(1,7))

    problem.addVariable(("B"),range(1,7))

    problem.addVariable(("C"),range(1,7))

    problem.addVariable(("D"),range(1,7))

    problem.addVariable(("E"),range(1,7))

    problem.addVariable(("F"),range(1,7))





    #this method is used for sum of each side so that each side has same sum

    def sum1(a,b,c,d,e,f):



        if(a+b+c==c+d+e==S and c+d+e==e+f+a==S and a+b+c==e+f+a==S):

            return True


    problem.addConstraint(sum1,"ABCDEF")

    problem.addConstraint(constraint.AllDifferentConstraint()) #each circle got distinct  number

    solutions = problem.getSolutions() #get solution
    return solutions



#for printing we used for loop

flag=0 #flag used to indicate if a valid sums have started or finished. Initially,
#when no of solutions are 0, flag is 0. When solutions start puring in, it becomes 1
m=6
while True:
    solutions= solve(m)
    if(flag==0 and len(solutions)==0):
        m=m+1
        continue
    elif (flag==1 and len(solutions)==0):
        m=m+1
        break
    elif (flag ==0):
        flag=1
   
    print("Sum: ", m, "\nNumber of solutions:", len(solutions))
    s= solutions[0]
    print("A = {}, B = {}, C = {},D = {}, E = {}, F = {}"

        .format(s['A'], s['B'], s['C'],s['D'], s['E'], s['F']))
    m=m+1

    

   
