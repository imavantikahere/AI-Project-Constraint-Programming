

##-Avantika Poddar-73131-



##Mariam Tanzeel-61915-



##Shatha Abduh-66003-


##Mohammed AlZaabi-65549
import constraint
import string

problem = constraint.Problem()

#factors of the problem
nationality = ["English", "Spaniard","Japanese", "Italian", "Norweign"] #storing all the nationalities in a list
pet = ["dog", "snails", "fox", "horse", "zebra"]#storing all the pets in a list
profession = ["Painter", "Sculptor", "Diplomat", "Violinist","Doctor"] #storing all professions
colour = ["red", "green", "white", "yellow", "blue"]#storing colours of houses
beverage = ["tea", "coffee", "milk", "fruit juice", "water"]#storing all drinks

criteria = nationality + pet + profession + colour + beverage #adding all the factors to a single list
problem.addVariables(criteria,[1,2,3,4,5]) #adding the factors as variables, each will be assigned a value from 1-5, alements of same factor cannot share same no, as done next

#following code means elemnts of each factor much have a distinct number from 1 to 5

problem.addConstraint(constraint.AllDifferentConstraint(), nationality)
problem.addConstraint(constraint.AllDifferentConstraint(), pet)
problem.addConstraint(constraint.AllDifferentConstraint(), profession)
problem.addConstraint(constraint.AllDifferentConstraint(), colour)
problem.addConstraint(constraint.AllDifferentConstraint(), beverage)

#inputting the information we already have in the form of consraints
problem.addConstraint(lambda e, r: e == r, ["English","red"]) #Englishman= red house

problem.addConstraint(lambda s, d: s == d, ("Spaniard","dog")) #Spaniard= dog

problem.addConstraint(lambda j, p: j == p, ("Japanese","Painter"))#Japanese= Painter

problem.addConstraint(lambda i, t: i == t, ("Italian","tea"))#Italian= tea

problem.addConstraint(constraint.InSetConstraint([1]), ["Norweign"]) #Norweign in first house-> Norweign=1

problem.addConstraint(lambda g, c: g == c, ("green","coffee")) #green house= coffee

problem.addConstraint(lambda g, w: g-w==1, ("green","white")) #green house right of white house

problem.addConstraint(lambda s, sn: s==sn, ("Sculptor","snails"))#sculptor= snails

problem.addConstraint(lambda d, y: d==y, ("Diplomat","yellow"))#diplomat= yellow

problem.addConstraint(constraint.InSetConstraint([3]), ["milk"]) #milk in middle house-> milk in 3rd house

problem.addConstraint(lambda n, b: abs(n-b)==1, ["Norweign","blue"])#Norweign next door to blue

problem.addConstraint(lambda v, f: v == f, ["Violinist","fruit juice"])#Violinist= fruit juice

problem.addConstraint(lambda f, d: abs(f-d) == 1, ("fox","Doctor"))#fox= next to doctor

problem.addConstraint(lambda h, d: abs(h-d) == 1, ("horse","Diplomat"))# horse next to diplomat

solution = problem.getSolutions() #getting all solutions
print("Number of different solutions possible: ", len(problem.getSolutions()))

#showing the complete solution
print("The complete solution for this problem is:\n")

for t in range(len(problem.getSolutions())):
        print("\t\tSolution ", t+1, "\n")
        for i in range(1,6):
               print("\nHouse ",i,":\n")
               for sol in solution[t]:
                    if solution[t][sol]==i:
                          print (sol)
               

#To show which house and who has zebra
print("So, who owns a zebra and in which house?\n")
for t in range(len(problem.getSolutions())): #iterating through all possible combination of solutions
        #the following strings are used to store the factor elements that have same value as zebra
        s1=" "
        s2="  "
        s3="  "
        s4= "  "
        print("\t\tConsidering Solution ", t+1, "\n")
        n= solution[t]['zebra'] #storing the value of key 'zebra' in the solution dictionary
        print ("House ",n ," has zebra that:")
        for s in solution[t]:#for a particular solution, checking which elements have same value
            if solution[t][s]==n:
                if s in nationality:
                    s1=s
                if s in beverage:
                    s2=s
                if s in colour:
                    s3=s
                if s in profession:
                    s4=s
        print ("Belongs to the",s1 , "who drinks",s2 ,"in a house that is", s3 ,"and who is a", s4, '\n')        

          
#To show which house and who drinks water
print("And, who drinks water and in which house?\n")
for t in range(len(problem.getSolutions())): #iterating through all possible combination of solutions
        #the following strings are used to store the factor elements that have same value as water
        s1=" "
        s2="  "
        s3="  "
        s4= "  "
        print("\t\tConsidering Solution ", t+1, "\n")
        n= solution[t]['water'] #storing the value of key 'zebra' in the solution dictionary
        print ("House ",n ," has person who drinks water:")
        for s in solution[t]:#for a particular solution, checking which elements have same value
            if solution[t][s]==n:
                if s in nationality:
                    s1=s
                if s in pet:
                    s2=s
                if s in colour:
                    s3=s
                if s in profession:
                    s4=s
        print ("who is a",s1 , "who owns a",s2 ,"in a house that is", s3 ,"and who is a", s4, '\n')        

