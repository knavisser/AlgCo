import fileinput
import itertools

# Class for brute-forcing the algorithm.
class bruteSolver:
    def __init__(self):
        self.variables = []
        self.condition = []
        self.stats = []

    # Helper functions below
    def addStats(self, stats):
        self.stats = stats

    def addVar(self, var):
        self.variables.append(var)

    def addCondition(self, n):
        self.condition.append(n)

    # Function that verifies a solution; returns true or false
    def checkSolution(self, vars):
        for cond in self.condition:
            cor = 0
            for entry in cond:
                if "~" in entry:
                    name = entry.replace('~', '')
                    if vars[name] == 0:
                        cor = 1
                else:
                    if vars[entry] == 1:
                        cor = 1
            if cor == 0:
                return False
        return True

    # Function that finds all possible solutions for a SAT problem and returns output for each solution as specified in PDF
    def findSolution(self):
        lst = list(itertools.product([0, 1], repeat=len(self.variables)))
        vervuld = False
        for item in lst:
            vars = dict()
            for i in range(len(self.variables)):
                vars[self.variables[i]] = item[i]
            if self.checkSolution(vars) == True:
                vervuld = True
                print(str(self.stats[0]) + " " + str(self.stats[1]))
                for item in vars:
                    print(item + " " + str(vars[item]))
                for cond in self.condition:
                    print(*cond)
                print('\n')
        if vervuld == False:
            print("Niet vervulbaar")


class smartSolver:
    def __init__(self):
        self.variables = []
        self.condition = []
        self.stats = []
        self.solution = dict()

    # Helper functions below
    def addStats(self, stats):
        self.stats = stats

    def addVar(self, var):
        self.variables.append(var)
        self.solution[var] = 2

    def addCondition(self, n):
        self.condition.append(n)

    # Function to verify if a solution is correct
    def checkSolution(self, vars):
        print("Checking for " + str(vars))
        for cond in self.condition:
            cor = 0
            for entry in cond:
                if "~" in entry:
                    name = entry.replace('~', '')
                    if vars[name] == 0:
                        cor = 1
                else:
                    if vars[entry] == 1:
                        cor = 1
            if cor == 0:
                return False
        return True

    # Function to remove single unit clauses from condition and add them as predetermined variables
    def propagateUnits(self):
        for cond in self.condition:
            if not isinstance(cond, list):
                if "~" in cond:
                    notCond = cond.replace("~", "")
                    self.solution[notCond] = 0
                else:
                    notCond = "~" + cond
                    self.solution[cond] = 1
                self.condition = [item for item in self.condition if cond not in item]

    # Function to find pure literals and eliminate them before making them unit clauses
    def pureElim(self):
        for var in self.variables:
            notVar = "~" + var
            matchingVar = [y for y in self.condition if var in y]
            matchingNotVar = [y for y in self.condition if notVar in y]
            if len(matchingVar) == 0 and len(matchingNotVar) != 0:
                self.condition = [item for item in self.condition if notVar not in item] 
                self.addCondition(notVar)
            if len(matchingVar) != 0 and len(matchingNotVar) == 0:
                self.condition = [item for item in self.condition if var not in item]
                self.addCondition(var)
        self.propagateUnits()

    def findSolution(self):
        solved = 0
        unknownVars = dict()
        solution = dict()
        self.pureElim()
        for var in self.solution:
            if self.solution[var] == 2:
                unknownVars[var] = 0
        for var in unknownVars:
                solution[var] = unknownVars[var]
        print(self.searchRec(unknownVars, solution))
        
        
    def searchRec(self, unk, sol):
        print(unk)
        print(sol)
        self.pureElim()
        self.checkSolution(sol)
        if len(unk) == 0:
            print("No more unknown to report")
            return self.checkSolution(sol)
        key = list(unk)[0]
        sol[key] = 1
        del unk[key]
        self.searchRec(unk, sol)

        
        


# Handling input
rawData = []
for line in fileinput.input():
    x = [str(i) for i in line.split()]
    rawData.append(x)

# Create solver class and handle input
solver = smartSolver()
solver.addStats(rawData[0])
numVar = int(rawData[0][0])
del rawData[0]

for i in range(numVar):
    solver.addVar(rawData[i][0])

for i in range(numVar):
    del rawData[0]

for line in rawData:
    solver.addCondition(line)

solver.findSolution()

# Find solution
# solver.findSolution()


