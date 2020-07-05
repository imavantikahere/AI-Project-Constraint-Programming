##-Avantika Poddar-73131-
##Mariam Tanzeel-61915-
##Shatha Abduh-66003-
##Mohammed AlZaabi-65549 

import constraint


problem = constraint.Problem()
problem.addVariable(("I"),range(1,4))
problem.addVariable(("G"),range(1,4))
problem.addVariable(("M"),range(1,4))


def position(i,g,m):
    if (i !=1 and abs(i-g)!=1):
        return True


problem.addConstraint(position,"IGM")
problem.addConstraint(constraint.AllDifferentConstraint())

solutions = problem.getSolutions()
print("Number of solutions found: {}\n".format(len(solutions)))

# .getSolutions() returns a dictionary
for s in solutions:
    print("Ice Swan = {}, Gold Lion = {}, Marble Pyramid = {}"
        .format(s['I'], s['G'], s['M']))

