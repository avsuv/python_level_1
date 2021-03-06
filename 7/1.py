class Matrix:
    def __init__(self, matrix_in):
        self.matrix_in = matrix_in

    def __str__(self):
        matrix_str = ''
        for line in self.matrix_in:
            for el in line:
                matrix_str += str(el).ljust(8)
            matrix_str += '\n'
        return matrix_str

    def __add__(self, other):
        h1 = len(self.matrix_in)
        l1 = len(self.matrix_in[0])
        h2 = len(other.matrix_in)
        l2 = len(other.matrix_in[0])
        matrix_new = [[0 for _ in range(max(l1, l2))] for el in range(max(h1, h2))] # Пустая матрица, заполненная нулями
        for i in range(h1):     # Сначала складываем нулевую матрицу с первой
            for j in range(l1):
                matrix_new[i][j] += self.matrix_in[i][j]
        for i in range(h2):     # Потом результат складываем со второй матрицей
            for j in range(l2):
                matrix_new[i][j] += other.matrix_in[i][j]
        return Matrix(matrix_new)   # Создаем новый объект Matrix, для корректного отображения - не знаю,
                                    # насколько корректно так делать

matr_1 = Matrix([[31, 22],
                 [37, 43],
                 [51, 86]])

matr_2 = Matrix([[3, 5, 32],
                 [2, 4, 6]])

matr_3 = Matrix([[1, 2, 3, 4]])
print(matr_1)
print(matr_2)
print(matr_3)
print(matr_1 + matr_2)
print(matr_1 + matr_3)
matr_4 = matr_2 + matr_3
print(matr_4)