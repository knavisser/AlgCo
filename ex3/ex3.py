import fileinput

# Make necessary class that compares inputs
class inputCompare:
    def __init__(self):
        self.correct = ""
        self.maxRuns = 0
        self.inputs = []
        self.output = []


    # Function to add input
    def addInput(self, input):
        self.inputs.append(input)


    # Recrusive algorithm to compare input to correct input and return sequence
    def findSequence(self, input, lenC, lenI, matrix):
        correct = str(self.correct)
    
        if lenC == 0 or lenI == 0:
            return ['']
    
        if correct[lenC - 1] == input[lenI - 1]:
            seq = self.findSequence(input, lenC - 1, lenI - 1, matrix)
            for i in range(len(seq)):
                seq[i] = seq[i] + (correct[lenC - 1])
            return seq
    
        if matrix[lenC - 1][lenI] > matrix[lenC][lenI - 1]:
            return self.findSequence(input, lenC - 1, lenI, matrix)

        if matrix[lenC][lenI - 1] > matrix[lenC - 1][lenI]:
            return self.findSequence(input, lenC, lenI - 1, matrix)

        list1 = self.findSequence(input, lenC - 1, lenI, matrix)
        list2 = self.findSequence(input, lenC, lenI - 1, matrix)
        return list1 + list2


    # Overarching function to find the right sequence (Since there will be multiple with the same length)
    def findRightSequence(self, input):
        correct = str(self.correct)
        matrix = [[0 for x in range(len(input) + 1)] for y in range(len(correct) + 1)]
    
        for indexX in range(1, len(correct) + 1):
            for indexY in range(1, len(input) + 1):
                if correct[indexX - 1] == input[indexY - 1]:
                    matrix[indexX][indexY] = matrix[indexX - 1][indexY - 1] + 1
                else:
                    matrix[indexX][indexY] = max(matrix[indexX - 1][indexY], matrix[indexX][indexY - 1])

        seqs = self.findSequence(input, len(correct), len(input), matrix)
        seqs.sort()
        return seqs[0]


# Instantiate class and add input
comparator = inputCompare()
for line in fileinput.input():
    x = [int(i) for i in line.split()]
    comparator.addInput(x)

# Run all inputs
comparator.correct = comparator.inputs[0][1]
comparator.maxRuns = comparator.inputs[0][0]
del comparator.inputs[0]
for input in comparator.inputs:
    output = comparator.findRightSequence(str(input[0]))
    print(str(len(output)) + " " + str(output))
