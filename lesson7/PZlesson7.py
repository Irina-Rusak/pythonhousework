"""
Практическое задание к уроку 7:
"""
"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов 
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы 
складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result_string = ''
        for row in self.matrix:
            for element in row:
                result_string += f'   {element}'
            result_string += '\n'
        return result_string

    def __add__(self, other):
        result_matrix = []
        try:
            if len(self.matrix) != len(other.matrix):
                raise Exception('Проверьте данные в матрицах!')
            for row_a, row_b in zip(self.matrix, other.matrix):
                if len(row_a) != len(row_b):
                    raise Exception('Проверьте данные в матрицах!')
                result_row = []
                for element_a, element_b in zip(row_a, row_b):
                    result_row.append(int(element_a) + int(element_b))
                result_matrix.append(result_row)
            return Matrix(result_matrix)
        except Exception as e:
            print(e)
            return None


my_matrix_a = Matrix([[5, 2, 3], [7, 4, 1], [3, 5, 4]])
print(f'Matrix A:\n{my_matrix_a}')
my_matrix_b = Matrix([[1, 0, 7], [2, 4, 2], [6, 2, 3]])
print(f'Matrix B:\n{my_matrix_b}')
my_matrix_c = my_matrix_a + my_matrix_b
print(f'Result matrix:\n{my_matrix_c}')

"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта 
— одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calc_cloth(self):
        pass


class Coat(Clothes):

    def __init__(self, param):
        super().__init__(param)

    @property
    def calc_cloth(self):
        result = f'{float(float(self.param) / 6.5 + 0.5):0.2f}'
        return result


class Suit(Clothes):

    def __init__(self, param):
        super().__init__(param)

    @property
    def calc_cloth(self):
        result = f'{float(2 * float(self.param) + 0.3):0.2f}'
        return result


my_coat = Coat(44)
print(f'Расход ткани на пальто {my_coat.param} размера = {my_coat.calc_cloth}')
my_suit = Suit(1.70)
print(f'Расход ткани на костюм с ростом {my_suit.param} = {my_suit.calc_cloth}')
print(f'Общий расход ткани на пальто и костюм = {round(float(my_coat.calc_cloth) + float(my_suit.calc_cloth))}')

"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: 
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, 
умножение и обычное (не целочисленное) деление клеток, соответственно. 
В методе деления должно осуществляться округление значения до целого числа.
Подсказка: подробный список операторов для перегрузки доступен по ссылке: 
https://pythonworld.ru/osnovy/peregruzka-operatorov.html.
"""

class Cell:

    def __init__(self, count_cell):
        self.count_cell = int(count_cell)

    def __str__(self):
        return str(self.count_cell)

    def __add__(self, other):
        """
        Сложение. Объединение двух клеток.
        При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
        """
        return Cell(self.count_cell + other.count_cell)

    def __sub__(self, other):
        """
        Вычитание. Участвуют две клетки.
        Операцию необходимо выполнять только если разность количества ячеек двух клеток
        больше нуля, иначе выводить соответствующее сообщение.
        """
        return Cell(self.count_cell - other.count_cell) if self.count_cell > other.count_cell \
            else print('Вычитание клеток невозможно!')


    def __mul__(self, other):
        """
        Умножение. Создается общая клетка из двух.
        Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
        """
        return Cell(self.count_cell * other.count_cell)

    def __truediv__(self, other):
        """
        Деление. Создается общая клетка из двух.
        Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
        """
        return Cell(self.count_cell // other.count_cell)

    def make_order(self, count_cell_row):
        """
        В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
        Данный метод позволяет организовать ячейки по рядам.
        Метод должен возвращать строку вида *****\n*****\n*****...,
        где количество ячеек между \n равно переданному аргументу.
        Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
        Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
        Тогда метод make_order() вернет строку: *****\n*****\n**.
        Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
        Тогда метод make_order() вернет строку: *****\n*****\n*****.
        :return:
        """
        result_cell = ('*' * count_cell_row + '\n') * (self.count_cell // count_cell_row) +\
                      '*' * (self.count_cell % count_cell_row)
        return result_cell


cell_a = Cell(10)
cell_b = Cell(8)
print(f'Сложение клеток {cell_a} и {cell_b} = {cell_a + cell_b}')
print(f'Вычитание клеток {cell_a} - {cell_b} = {cell_a - cell_b}')
print(f'Вычитание клеток {cell_b} - {cell_a} = {cell_b - cell_a}')
print(f'Умножение клеток {cell_a} и {cell_b} = {cell_a * cell_b}')
print(f'Деление клеток {cell_a} и {cell_b} = {cell_a / cell_b}')
print(f'Организация клетки по рядам:\n{cell_a.make_order(3)}')
