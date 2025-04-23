class Matrix:
    def __init__(self, data):
        if len(data) != 3 or any(len(row) != 3 for row in data):
            raise ValueError("Matrix must be 3x3")
        self.data = data

    def __add__(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                s = 0
                for k in range(3):
                    s += self.data[i][k] * other.data[k][j]
                row.append(s)
            result.append(row)
        return Matrix(result)

    def transpose(self):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.data[j][i])
            result.append(row)
        return Matrix(result)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

# Test code
m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2 = Matrix([[9,8,7],[6,5,4],[3,2,1]])

print("Matrix 1:")
print(m1)
print("\nMatrix 2:")
print(m2)
print("\nAddition:")
print(m1 + m2)
print("\nMultiplication:")
print(m1 * m2)
print("\nTranspose of Matrix 1:")
print(m1.transpose())
