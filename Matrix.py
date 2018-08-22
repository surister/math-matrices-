

class Matrix:
    """ m = filas
        n = columnas """
    def __init__(self, *matrix: list):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = matrix
        self.space = '\n'
        self.matrix_str = ''
        self.result = []

    def __str__(self):
        for row in self.matrix:
            self.matrix_str += str(row) + self.space
        return self.matrix_str

    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            raise ValueError('Para sumar 2 matrices tienen que tener las mismas dimensiones')
        else:
            self.result = [[0 for _ in range(self.n)] for _ in range(self.m)]
            for row in range(self.m):
                for column in range(self.n):
                    self.result[row][column] += self.matrix[row][column] + other.matrix[row][column]
            return Matrix(*self.result)

    def __mul__(self, other):
        if isinstance(other, int):
            self.result = self.matrix
            for i in range(self.m):
                for j in range(self.n):
                    self.result[i][j] *= other
            return Matrix(*self.result)
        elif isinstance(other, Matrix):
            if self.n != other.m:
                raise ValueError('Para multiplicar 2 matrices tienen que tener Matrix.n == Other.m')
            else:
                self.result = [[0 for _ in range(other.n)] for _ in range(self.m)]
                for i in range(self.m):
                    for j in range(other.n):
                        for k in range(other.m):
                            self.result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(*self.result)

    def __repr__(self):
        return f'Matrix({self.matrix})'

    @property
    def info(self):
        return str(self) + self.space + f'm = {self.m}, n = {self.n}'


matrix_1 = Matrix([-1, -3, -1], [-1, -5, 0], [0, 1, 0])
matrix_2 = Matrix([1, 0 , 3], [-1, 1, 0], [0, 1, 2])

print(matrix_1.info)
print(matrix_2.info)
matrix2 = matrix_1 * matrix_2
print(matrix2)
