# Создайте класс Матрица.
# Добавьте методы для: вывода на печать, сравнения, сложения, *умножения матриц
import sys, logging
import argparse

class Matrix:

    def __init__(self, matr):
        self._matr = matr
        self.logger = logging.getLogger('Matrix')
        self.logger.info('Создан объект "матрица"')

    def get_matrix(self):
        return self._matr

    def __eq__(self, other):
        self.logger.debug('Запуск сравнения двух матриц')
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            self.logger.error('Попытка сравнить матрицы разных размеров!')
            return f'Error: матрицы разных размеров'
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        self.logger.debug('Сравниваемые матрицы не равны')
                        return False
                    self.logger.debug('Сравниваемые матрицы равны')
                    return True

    def __add__(self, other):
        self.logger.debug('Запуск сложения двух матриц')
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            self.logger.error('Попытка сложить матрицы разных размеров!')
            return f'Error: матрицы разных размеров'
        else:
            self.logger.debug('Операция сложения выполнена')
            return Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in
                           range(len(self._matr))])

    def __mul__(self, other):
        self.logger.debug('Запуск перемножения двух матриц')
        if len(self._matr) != len(other._matr):
            self.logger.error('Попытка перемножить несовместимые матрицы!')
            return f'Error: невозможно перемножить матрицы'
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in
                        self._matr]
            self.logger.debug('Операция умножения выполнена')
            return Matrix(new_matr)

    def __str__(self):
        self.logger.debug('Запуск преобразования матрицы в строку')
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i]) + '\n'
        self.logger.debug('Операция преобразования в строку выполнена')
        return s


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='task1.log')
namespace = parser.parse_args(sys.argv[1:])

logging.basicConfig(filename=namespace.filename, filemode='w', level=logging.DEBUG)

a1 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
a2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a3 = [1, 2, 4, 5, 0], [5, 6, 8, 0, 0], [5, 0, -7, 1, 0]
a4 = [1, 2, 4], [5, 6, 8], [2, 5, -2]

m_1 = Matrix(a1)
m_2 = Matrix(a2)
m_3 = Matrix(a3)
m_4 = Matrix(a4)

print("Cравнение матриц:")

print(m_1 == m_1)
print(m_1 == m_2)

print("Cложение матриц:")
matrix_sum = m_1 + m_2
print(matrix_sum)

print("Умножение матриц:")
matrix_mul = m_1 * m_3
print(matrix_mul)
print(m_1 * m_4)