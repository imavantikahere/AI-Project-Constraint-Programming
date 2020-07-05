
##-Avantika Poddar-73131-

##Mariam Tanzeel-61915-

##Shatha Abduh-66003-
##Mohammed AlZaabi-65549

import constraint

problem = constraint.Problem()
#Let the times be 1,2,3,4

problem.addVariables("A", [1,3,4])
problem.addVariables("B", [1,2,3])
problem.addVariables("C", [1,2,3])
problem.addVariables("D", [1,4])

# Telling Python that we need TWO + TWO = FOUR
def constraint1(a,b,c,d):
    if(a != b !=c !=d):
        return True

# Adding our custom constraint. The
# order of variables is important!
problem.addConstraint(constraint1, "ABCD")

# All the characters must represent different digits,
# there's a built-in constraint for that
problem.addConstraint(constraint.AllDifferentConstraint())

solutions = problem.getSolutions()
print("Number of solutions found: {}\n".format(len(solutions)))

# .getSolutions() returns a dictionary
for s in solutions:
    print("Ali = {}:00 PM, Bob = {}:00 PM, Cyl = {}:00 PM, Dan = {}:00 PM"
        .format(s['A'], s['B'], s['C'], s['D']))


#Preferences for Cyl
sol={}
min_time=1
for s in solutions:
    if(s['C'] <= min_time):
        min_time=s['C']
        sol= s

print("\nUpdated schedule with prefernce to Cyl\n")
print("Ali = {}:00 PM, Bob = {}:00 PM, Cyl = {}:00 PM, Dan = {}:00 PM"
        .format(sol['A'], sol['B'], sol['C'], sol['D']))

