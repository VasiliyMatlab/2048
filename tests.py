import unittest
from main import *

class Test_2048(unittest.TestCase):

    def test_1(self):
        i = list()
        j = list()
        for k in range(SIZE):
            for z in range(SIZE):
                i.append(k)
                j.append(z)
        for k in range(1, SIZE*SIZE + 1):
            self.assertAlmostEqual(k, get_number_from_index(i[k-1], j[k-1]))

    def test_2(self):
        i = list()
        j = list()
        for k in range(SIZE):
            for z in range(SIZE):
                i.append(k)
                j.append(z)
        for k in range(1, SIZE*SIZE + 1):
            x, y = get_index_from_number(k)
            self.assertAlmostEqual((i[k-1], j[k-1]), (x, y))

    def test_3(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        rez = list(range(1, SIZE*SIZE + 1))
        self.assertAlmostEqual(rez, get_empty_list(mas))
    
    def test_4(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        for i in range(SIZE):
            for j in range(SIZE):
                mas[i][j] = 1
                rez = list(range(1, SIZE*SIZE + 1))
                rez.remove(get_number_from_index(i, j))
                self.assertAlmostEqual(rez, get_empty_list(mas))
                mas[i][j] = 0
    
    def test_5(self):
        mas = [[1]*SIZE for n in range(SIZE)]
        rez = list()
        self.assertAlmostEqual(rez, get_empty_list(mas))
    
    def test_6(self):
        mas = [[0]*SIZE for n in range(SIZE)]
        self.assertAlmostEqual(True, is_zero_in_mas(mas))
    
    def test_7(self):
        mas = [[1]*SIZE for n in range(SIZE)]
        for i in range(SIZE):
            for j in range(SIZE):
                mas[i][j] = 0
                self.assertAlmostEqual(True, is_zero_in_mas(mas))
                mas[i][j] = 1
    
    def test_8(self):
        mas = [[1]*SIZE for n in range(SIZE)]
        self.assertAlmostEqual(False, is_zero_in_mas(mas))


if __name__ == "__main__":
    unittest.main()