import fileinput

class inputCompare:
    def __init__(self):
        self.correct = ""
        self.maxRuns = 0
        self.inputs = []
        self.output = []

    def addInput(self, input):
        self.inputs.append(input)

    def findSequence(self, input):
        correct = str(self.correct)
        len1 = len(correct)
        len2 = len(input)
        matrix = [[0 for x in range(len1 + 1)] for x in range(len2 + 1)]
        for x in range(len1 + 1):
            for y in range(len2 + 1):
                if x == 0 or y == 0:
                    matrix[x][y] = 0
                elif correct[x - 1] == input[y - 1]:
                    matrix[x][y] = matrix[x - 1][y - 1] + 1
                else:
                    matrix[x][y] = max(matrix[x - 1][y], matrix[x][y - 1])
        index = matrix[len2][len1]
        seq = [""] * (index + 1)
        seq[index] = ""

        index1 = len2
        index2 = len1
        while index1 > 0 and index2 > 0:
            if correct[index1 - 1] == input[index2 - 1]:
                seq[index - 1] = correct[index1 - 1]
                index1 -= 1
                index2 -= 1
                index -= 1
            elif matrix[index1 - 1][index2] > matrix[index1][index2 - 1]:
                index1 -= 1
            else:
                index2 -= 1
                
        print("".join(seq))
        # Printing the sub sequences
        #print("Correc sequence is: " + correct + "\nInput sequence is: " + input)
        #print("Longest common subsequence is: " + "".join(seq))

comparator = inputCompare()
for line in fileinput.input():
    x = [int(i) for i in line.split()]
    comparator.addInput(x)

comparator.correct = comparator.inputs[0][1]
comparator.maxRuns = comparator.inputs[0][0]
del comparator.inputs[0]
for input in comparator.inputs:
    comparator.findSequence(str(input[0]))


    