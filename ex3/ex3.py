import fileinput

class inputCompare:
    def __init__(self):
        self.correct = 0
        self.maxRuns = 0
        self.inputs = []

    def addInput(self, input):
        self.inputs.append(input)

    def compareInputs(self):
        self.maxRuns = self.inputs[0][0]
        self.correct = self.inputs[0][1]
        del self.inputs[0]
        print("Iterating over " + str(self.maxRuns) + " entries. Comparing with: " + str(self.correct))

comparator = inputCompare()
for line in fileinput.input():
    x = [int(i) for i in line.split()]
    comparator.addInput(x)

comparator.compareInputs()

    