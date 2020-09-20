class Matrix(object):
    # Function that creates matrix mxn
    def __init__(self, file):
        self.file = file
        f = open(file)
        lines = f.readlines()
        f.close()
        self.matrix = []
        for line in lines:
            self.row = line.split(" ")
            for i in range(len(self.row)):
                self.row[i] = int(self.row[i])
            self.matrix.append(self.row)
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    # Function that creates Identity matrix nxn
    def Identity(self):
        count = 1
        self.identity = []
        for i in range(self.cols):
            self.identity.append([])
            for j in range(self.cols):
                if j+1 == count:
                    self.identity[i].append(1)
                else:
                    self.identity[i].append(0)
            count += 1

    # Function that implements addition of two matrices
    def Add(self, matrix1):
        if self.rows != matrix1.rows or self.cols != matrix1.cols:
            print("They don't have same size")
            return 0
        else:
            self.addMatrix = [[0 for col in range(self.cols)] for row in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.cols):
                    self.addMatrix[i][j] = self.matrix[i][j] + matrix1.matrix[i][j]
            return self.addMatrix

    # Function that implements multiplication of two matrices
    def Multiply(self, matrix1):
        if self.cols != matrix1.rows:
            print("They cannot be multiplied")
            return 0
        else:
            self.multiMatrix = [[0 for col in range(matrix1.cols)] for row in range(self.rows)]
            for i in range(self.rows):
                for j in range(matrix1.cols):
                    self.multi = 0
                    for a in range(self.cols):
                        self.multi += self.matrix[i][a] * matrix1.matrix[a][j]
                    self.multiMatrix[i][j] = self.multi
            return self.multiMatrix

    # Function that returns transpose matrix
    def Transpose(self):
        self.transMatrix = [[0 for col in range(self.rows)] for row in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.transMatrix[j][i] = self.matrix[i][j]
        return self.transMatrix

    # Function that determines the matrix is symmetric or not
    def IsSymmetric(self):
        if self.matrix == self.Transpose():
            return True
        else:
            return False

    # Function that determines the two matrices are same or not
    def IsSame(self, matrix1):
        if self.rows != matrix1.rows or self.cols != matrix1.cols:
            return False
        elif self.matrix != matrix1.matrix:
            return False
        else:
            return True

    # Function that returns n power of matrix
    def Power(self, n):
        self.originalmatrix = Matrix(self.file)
        if n == 1:
            return self
        else:
            self.matrix = self.originalmatrix.Multiply(self.Power(n-1))
            return self


import time
start = time.time()

matrix1 = Matrix('problem1-1-1.txt')
matrix2 = Matrix('problem1-1-2.txt')
matrix3 = Matrix('problem1-2-1.txt')
matrix4 = Matrix('problem1-2-2.txt')
matrix5 = Matrix('problem2-1.txt')
matrix6 = Matrix('problem2-2.txt')
matrix7 = Matrix('problem3-2.txt')

print("The solution of part3 - problem1(1) is")
AddResult = matrix1.Add(matrix2)
for i in range(len(AddResult)):
    print(AddResult[i])
print("\n")

print("The solution of part3 - problem1(2) is ")
MultiplyResult = matrix3.Multiply(matrix4)
for j in range(len(MultiplyResult)):
    print(MultiplyResult[j])
print("\n")

print("The solution of part3 - problem2 is")
matrix5.Identity()
matrix6.Identity()
print(matrix5.Multiply(matrix6) == matrix5.identity and matrix6.Multiply(matrix5) == matrix6.identity)
print("\n")

print("The solution of part3 - problem3(2) is")
PowerResult = matrix7.Power(10).matrix
for k in range(len(PowerResult)):
    print(PowerResult[k])
print("\n")

end = time.time()
elapsed_time = end - start
print("The time elasped for execution is", elapsed_time)