import fileinput

class verifier:
    def __init__(self):
        self.variables = dict()
        self.condition = []

    def addVar(self, n, m):
        self.variables[n] = int(m)

    def addCondition(self, n):
        self.condition.append(n)

    def checkSolution(self):
        for cond in self.condition:
            cor = 0
            for entry in cond:
                if "~" in entry:
                    name = entry.replace('~', '')
                    if self.variables[name] == 0:
                        cor = 1
                else:
                    if self.variables[entry] == 1:
                        cor = 1
            if cor == 0:
                print("Vervult formule niet")
                return
        print("Vervult formule")


rawData = []
for line in fileinput.input():
    x = [str(i) for i in line.split()]
    print(x)
    rawData.append(x)


ver = verifier()
numVar = int(rawData[0][0])
del rawData[0]
for i in range(numVar):
    ver.addVar(rawData[i][0], rawData[i][1])

for i in range(numVar):
    del rawData[0]

for line in rawData:
    ver.addCondition(line)

print(ver.variables)
print(ver.condition)
ver.checkSolution()