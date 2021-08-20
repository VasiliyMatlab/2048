import unittest
from main import *

class Test_2048(unittest.TestCase):

    def test_1(self):
        self.assertIsNot(1, SIZE)
        self.assertIsNot(2, SIZE)

    def test_2(self):
        i = list()
        j = list()
        for k in range(SIZE):
            for z in range(SIZE):
                i.append(k)
                j.append(z)
        for k in range(1, SIZE*SIZE + 1):
            self.assertAlmostEqual(k, get_number_from_index(i[k-1], j[k-1]))

    def test_3(self):
        i = list()
        j = list()
        for k in range(SIZE):
            for z in range(SIZE):
                i.append(k)
                j.append(z)
        for k in range(1, SIZE*SIZE + 1):
            x, y = get_index_from_number(k)
            self.assertAlmostEqual((i[k-1], j[k-1]), (x, y))

    def test_4(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        rez = list(range(1, SIZE*SIZE + 1))
        self.assertAlmostEqual(rez, get_empty_list(mas))
    
    def test_5(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        for i in range(SIZE):
            for j in range(SIZE):
                mas[i][j] = 2
                rez = list(range(1, SIZE*SIZE + 1))
                rez.remove(get_number_from_index(i, j))
                self.assertAlmostEqual(rez, get_empty_list(mas))
                mas[i][j] = 0
    
    def test_6(self):
        mas = [[2]*SIZE for n in range(SIZE)]
        rez = list()
        self.assertAlmostEqual(rez, get_empty_list(mas))
    
    def test_7(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        self.assertAlmostEqual(True, is_zero_in_mas(mas))
    
    def test_8(self):
        mas = [[2]*SIZE for n in range(SIZE)]
        for i in range(SIZE):
            for j in range(SIZE):
                mas[i][j] = 0
                self.assertAlmostEqual(True, is_zero_in_mas(mas))
                mas[i][j] = 2
    
    def test_9(self):
        mas = [[2]*SIZE for n in range(SIZE)]
        self.assertAlmostEqual(False, is_zero_in_mas(mas))
    
    def test_10(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        self.assertAlmostEqual(mas, move_left(mas))
    
    def test_11(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        self.assertAlmostEqual(mas, move_right(mas))
    
    def test_12(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        self.assertAlmostEqual(mas, move_up(mas))
    
    def test_13(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        self.assertAlmostEqual(mas, move_down(mas))
    
    def test_14(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        for k in range(SIZE):
            number = k*SIZE + (k+1)
            i, j = get_index_from_number(number)
            mas[i][j] = 2
        rez = [[0]*SIZE for n in range(SIZE)]
        for i in range(SIZE):
            rez[i][0] = 2
        self.assertAlmostEqual(rez, move_left(mas))

    def test_15(self):
        mas = [[2]*SIZE for n in range(SIZE)]
        half = SIZE // 2
        rez = [[0]*SIZE for n in range(SIZE)]
        for i in range(SIZE):
            for j in range(half):
                rez[i][j] = 4
        if SIZE % 2 == 1:
            for i in range(SIZE):
                rez[i][half] = 2
        self.assertAlmostEqual(rez, move_left(mas))
    
    def test_16(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        half = SIZE // 2
        rez = [[0]*SIZE for n in range(SIZE)]
        for i in range(SIZE):
            mas[i][half-1] = 4
            mas[i][SIZE-1] = 8
            rez[i][0] = 4
            rez[i][1] = 8
        self.assertAlmostEqual(rez, move_left(mas))
    
    def test_17(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        for k in range(SIZE):
            number = k*SIZE + (k+1)
            i, j = get_index_from_number(number)
            mas[i][j] = 2
        rez = [[0]*SIZE for n in range(SIZE)]
        for i in range(SIZE):
            rez[i][SIZE-1] = 2
        self.assertAlmostEqual(rez, move_right(mas))

    def test_18(self):
        mas = [[2]*SIZE for n in range(SIZE)]
        half = SIZE // 2
        rez = [[0]*SIZE for n in range(SIZE)]
        for i in range(SIZE):
            for j in range(SIZE-1, half-1, -1):
                rez[i][j] = 4
        if SIZE % 2 == 1:
            for i in range(SIZE):
                rez[i][half] = 2
        self.assertAlmostEqual(rez, move_right(mas))
    
    def test_19(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        half = SIZE // 2
        rez = [[0]*SIZE for n in range(SIZE)]
        for i in range(SIZE):
            mas[i][0] = 4
            mas[i][half] = 8
            rez[i][SIZE-2] = 4
            rez[i][SIZE-1] = 8
        self.assertAlmostEqual(rez, move_right(mas))
    
    def test_20(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        for k in range(SIZE):
            number = k*SIZE + (k+1)
            i, j = get_index_from_number(number)
            mas[i][j] = 2
        rez = [[0]*SIZE for n in range(SIZE)]
        for j in range(SIZE):
            rez[0][j] = 2
        self.assertAlmostEqual(rez, move_up(mas))
    
    def test_21(self):
        mas = [[2]*SIZE for n in range(SIZE)]
        half = SIZE // 2
        rez = [[0]*SIZE for n in range(SIZE)]
        for i in range(half):
            for j in range(SIZE):
                rez[i][j] = 4
        if SIZE % 2 == 1:
            for j in range(SIZE):
                rez[half][j] = 2
        self.assertAlmostEqual(rez, move_up(mas))
    
    def test_22(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        half = SIZE // 2
        rez = [[0]*SIZE for n in range(SIZE)]
        for j in range(SIZE):
            mas[half-1][j] = 4
            mas[SIZE-1][j] = 8
            rez[0][j] = 4
            rez[1][j] = 8
        self.assertAlmostEqual(rez, move_up(mas))
    
    def test_23(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        for k in range(SIZE):
            number = k*SIZE + (k+1)
            i, j = get_index_from_number(number)
            mas[i][j] = 2
        rez = [[0]*SIZE for n in range(SIZE)]
        for j in range(SIZE):
            rez[SIZE-1][j] = 2
        self.assertAlmostEqual(rez, move_down(mas))
    
    def test_24(self):
        mas = [[2]*SIZE for n in range(SIZE)]
        half = SIZE // 2
        rez = [[0]*SIZE for n in range(SIZE)]
        for i in range(SIZE-1, half-1, -1):
            for j in range(SIZE):
                rez[i][j] = 4
        if SIZE % 2 == 1:
            for j in range(SIZE):
                rez[half][j] = 2
        self.assertAlmostEqual(rez, move_down(mas))
    
    def test_25(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        half = SIZE // 2
        rez = [[0]*SIZE for n in range(SIZE)]
        for j in range(SIZE):
            mas[0][j] = 4
            mas[half][j] = 8
            rez[SIZE-2][j] = 4
            rez[SIZE-1][j] = 8
        self.assertAlmostEqual(rez, move_down(mas))

    def test_26(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        self.assertAlmostEqual(True, can_move(mas))
    
    def test_27(self):
        mas = [[2]*SIZE for n in range(SIZE)]
        self.assertAlmostEqual(True, can_move(mas))

    def test_28(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        for i in range(SIZE):
            for j in range(SIZE):
                mas[i][j] = get_number_from_index(i, j)
        self.assertAlmostEqual(False, can_move(mas))


tests = {
    1:  f"Неверное значение константы {SIZE}",
    2:   "Неверная работа функции 'get_number_from_index'",
    3:   "Неверная работа функции 'get_index_from_number'",
    4:   "Функция 'get_empty_list' возвращает неправильный список при нулевом массиве",
    5:   "Функция 'get_empty_list' возвращает неправильный список при наличии ненулевых элементов в нулевом массиве",
    6:   "Функция 'get_empty_list' возвращает непустой список при ненулевом массиве",
    7:   "Функция 'is_zero_in_mas' неверно определяет наличие нулей в нулевом массиве",
    8:   "Функция 'is_zero_in_mas' неверно определяет наличие нуля среди ненулевых элементов в массиве",
    9:   "Функция 'is_zero_in_mas' неверно определяет отсутствие нулей в ненулевом массиве",
    10:  "Ошибка заполнения ячеек в функции 'move_left' при нулевом массиве",
    11:  "Ошибка заполнения ячеек в функции 'move_right' при нулевом массиве",
    12:  "Ошибка заполнения ячеек в функции 'move_up' при нулевом массиве",
    13:  "Ошибка заполнения ячеек в функции 'move_down' при нулевом массиве",
    14:  "Ошибка движения ячеек в функции 'move_left' при диагональном массиве",
    15:  "Ошибка движения/складывания ячеек в функции 'move_left' при ненулевом однородном массиве",
    16:  "Ошибка движения/нескладывания ячеек в функции 'move_left' при заполнении массива такими значениями, сложение которых невозможно",
    17:  "Ошибка движения ячеек в функции 'move_right' при диагональном массиве",
    18:  "Ошибка движения/складывания ячеек в функции 'move_right' при ненулевом однородном массиве",
    19:  "Ошибка движения/нескладывания ячеек в функции 'move_right' при заполнении массива такими значениями, сложение которых невозможно",
    20:  "Ошибка движения ячеек в функции 'move_up' при диагональном массиве",
    21:  "Ошибка движения/складывания ячеек в функции 'move_up' при ненулевом однородном массиве",
    22:  "Ошибка движения/нескладывания ячеек в функции 'move_up' при заполнении массива такими значениями, сложение которых невозможно",
    23:  "Ошибка движения ячеек в функции 'move_down' при диагональном массиве",
    24:  "Ошибка движения/складывания ячеек в функции 'move_down' при ненулевом однородном массиве",
    25:  "Ошибка движения/нескладывания ячеек в функции 'move_down' при заполнении массива такими значениями, сложение которых невозможно",
    26:  "Неверная работа функции 'can_move' при нулевом массиве",
    27:  "Неверная работа функции 'can_move' при ненулевом однородном массиве",
    28:  "Неверная работа функции 'can_move' при ненулевом массиве (все элементы разные)"
}


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            try:
                num = int(sys.argv[1])
            except ValueError:
                raise ValueError(f"{sys.argv[1]} is not a number") from None
            print("----------------------------------------------------------------------")
            try:
                tests[num]
            except KeyError:
                raise KeyError(f"invalid test number {num}") from None
            print(tests[num])
        else:
            raise ValueError("too many arguments")
    else:
        print("При возникновении непройденных тестов, запустить отладку с номерами непрошедших тестов в порядке возрастания")
        unittest.main()