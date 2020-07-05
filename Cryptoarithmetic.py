
import constraint
#SEND + MORE = MONEY
# This is for the puzzle with implicit carries

problem = constraint.Problem()


problem.addVariables("MS", range(1,10))
problem.addVariables("ENDORY", range(10))


def sum_constraint1(s,e,n,d,m,o,r,y):
    if ((s * 1000 + e * 100 + n* 10 + d) + (m*1000 + o*100 + r*10 + e))== ((m*10000 + o*1000 + n* 100 + e* 10 +y)):
        return True
    
# Adding our custom constraint. The
# order of variables is important!

problem.addConstraint(sum_constraint1, "SENDMORY")
# All the characters must represent different digits,
# there's a built-in constraint for that
problem.addConstraint(constraint.AllDifferentConstraint())


solutions = problem.getSolutions()
print("Number of solutions found for SEND + MORE = MONEY when using implicit carries: {}\n".format(len(solutions)))

 #.getSolutions() returns a dictionary
for s in solutions:
    
        print("S = {}, E = {}, N = {}, D = {}, M = {}, O = {} , R = {} , Y = {}"
            .format(s['S'], s['E'], s['N'], s['D'], s['M'], s['O'], s['R'], s['Y']))


#Explicit carries

        
problem2= constraint.Problem()
#sum constraint for explicit carries
problem2.addVariables("MS", range(1,10))
problem2.addVariables("ENDORY", range(10))
def sum_constraint2(s,e,n,d,m,o,r,y):
    carry1= (d+e)/10
    carry2= (n+r+carry1)/10
    carry3= (e+o+carry2)/10
    carry4= (s+m+carry4)/10
    if( (d+e)%10 ==y and (n+r+carry1)%10==e and (e+o+carry2)%10 == n and (s+m +carry3)%10==o and carry4==m):
        return True 
problem2.addConstraint(sum_constraint1, "SENDMORY")
# All the characters must represent different digits,
# there's a built-in constraint for that
problem2.addConstraint(constraint.AllDifferentConstraint())


solutions = problem2.getSolutions()
print("\nNumber of solutions found for SEND + MORE = MONEY when using explicit carries: {}\n".format(len(solutions)))

 #.getSolutions() returns a dictionary
for s in solutions:
    
        print("S = {}, E = {}, N = {}, D = {}, M = {}, O = {} , R = {} , Y = {}"
            .format(s['S'], s['E'], s['N'], s['D'], s['M'], s['O'], s['R'], s['Y']))


 #(73131 + 61915 + 66003 + 65549) % 16 +1 = 7--> EXTRA + DAY = LEAP + YEAR

problem7=constraint.Problem()
problem7.addVariables("EDLY", range(1,10))
problem7.addVariables("XTRAP", range(10))
def sum_constraint7(e,d,l,y,x,t,r,a,p):
    if(((e*10000 + x *1000 + t*100 + r*10 +a) + (d*100 + a*10 +y))==((l*1000 + e *100 + a * 10 + p) + (y*1000+ e*100 + a *10 +r))):
        return True


problem7.addConstraint(sum_constraint7, "EDLYXTRAP")

problem7.addConstraint(constraint.AllDifferentConstraint())

solutions7 = problem7.getSolutions()
print("\nNumber of solutions for EXTRA + DAY = LEAP + YEAR found: {}\n".format(len(solutions7)))

 #.getSolutions() returns a dictionary
for s1 in solutions7:
    print("E = {}, D = {}, L = {}, Y = {}, X = {}, T = {}, R={}, A={}, P={} "
        .format(s1['E'], s1['D'], s1['L'], s1['Y'], s1['X'], s1['T'], s1['R'],s1['A'],s1['P']))


#BASE + BALL= GAMES

problem1=constraint.Problem()
problem1.addVariables("BG", range(1,10))
problem1.addVariables("ASELM", range(10))
def sum_constraint1(b,g,a,s,e,l,m):
    if ((b*1000+a *100+s*10+e +b*1000+a*100+l*10+l)==(g*10000 + a*1000+m*100+e*10+s)):
        return True


problem1.addConstraint(sum_constraint1, "BGASELM")

problem1.addConstraint(constraint.AllDifferentConstraint())

solutions1 = problem1.getSolutions()
print("\nNumber of solutions for BASE + BALL = GAMES found: {}\n".format(len(solutions1)))

 #.getSolutions() returns a dictionary
for s1 in solutions1:
    print("B = {}, G = {}, A = {}, S = {}, E = {}, L = {}, M={} "
        .format(s1['B'], s1['G'], s1['A'], s1['S'], s1['E'], s1['L'], s1['M']))


