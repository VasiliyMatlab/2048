SIZE = 4

# Печать массива в терминал
def pretty_print(mas) -> None:
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)

# Вычисление номера ячейки по индексам строки и столбца
def get_number_from_index(i, j) -> int:
    return SIZE*i + j + 1

# Список из пустых ячеек
def get_empty_list(mas) -> list:
    empty = list()
    for i in range(SIZE):
        for j in range(SIZE):
            if mas[i][j] == 0:
                empty.append(get_number_from_index(i, j))
    return empty


def main():
    mas = [[0] * SIZE] * SIZE
    mas[1][2] = 2
    mas[3][0] = 4

if __name__ == '__main__':
    main()