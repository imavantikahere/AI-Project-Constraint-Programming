
##-Avantika Poddar-73131-
##Shatha


import constraint


problem = constraint.Problem()
#name the circles as A,B,C,D,E,F,G,H,I FROM 1-9
problem.addVariable(("A"),range(1,10))
problem.addVariable(("B"),range(1,10))
problem.addVariable(("C"),range(1,10))
problem.addVariable(("D"),range(1,10))
problem.addVariable(("E"),range(1,10))
problem.addVariable(("F"),range(1,10))
problem.addVariable(("G"),range(1,10))
problem.addVariable(("H"),range(1,10))
problem.addVariable(("I"),range(1,10))

#this method is used for sum of each side so that each side has same sum
def sum1(a,b,c,d,e,f,g,h,i):

    if(a+b+c+d==d+e+f+g and d+e+f+g==g+h+i+a and a+b+c+d==g+h+i+a):
        return True

problem.addConstraint(sum1,"ABCDEFGHI")
problem.addConstraint(constraint.AllDifferentConstraint())
solutions = problem.getSolutions()



 #flag used to indicate if a valid sums have started or finished. Initially,
#when no of solutions are 0, flag is 0. When solutions start puring in, it becomes 1

sum_array=[]
for s in solutions:
    sum1= (s['A']+s['B'] +s['C']+ s['D'])
    if sum1 not in sum_array:
        sum_array.append(sum1)

count_array=[]
for s in sum_array:
    c=0
    for sol in solutions:
        if s==(sol['A']+sol['B'] +sol['C']+ sol['D']):
             c= c+1
    count_array.append(c)

c=0
for s in sum_array:
    print("Sum:",s)
    print("Number of solutions:", count_array[c])
    c=c+1
    for sol in solutions:
        if s==(sol['A']+sol['B'] +sol['C']+sol['D']):
             print("A = {}, B = {}, C = {},D = {}, E = {}, F = {}, G={}, H= {}, I={}"

               .format(sol['A'], sol['B'], sol['C'],sol['D'], sol['E'], sol['F'], sol['G'],sol['H'],sol['I']))
             break

 



