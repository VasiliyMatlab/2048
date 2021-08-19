import random

SIZE = 4

# Печать массива в терминал
def pretty_print(mas: list) -> None:
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)

# Вычисление номера ячейки по индексам строки и столбца
def get_number_from_index(i: int, j: int) -> int:
    return SIZE*i + j + 1

# Вычисление индексов строки и столбца по номеру ячейки
def get_index_from_number(num: int) -> tuple:
    num -= 1
    x, y = num // SIZE, num % SIZE
    return x, y

# Список из пустых ячеек
def get_empty_list(mas: list) -> list:
    empty = list()
    for i in range(SIZE):
        for j in range(SIZE):
            if mas[i][j] == 0:
                empty.append(get_number_from_index(i, j))
    return empty

# Проверка условия, есть ли нуль в массиве
def is_zero_in_mas(mas: list) -> bool:
    for row in mas:
        if 0 in row:
            return True
    return False

# Заполнение ячейки двойкой или четверкой
def insert_2_or_4(mas: list, x: int, y: int) -> list:
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def main():
    mas = [[0]*SIZE for n in range(SIZE)]
    mas[1][2] = 2
    mas[3][0] = 4

    while is_zero_in_mas(mas):
        input()
        empty = get_empty_list(mas)
        random.shuffle(empty)
        random_num = empty.pop()
        x, y = get_index_from_number(random_num)
        mas = insert_2_or_4(mas, x, y)
        pretty_print(mas)

if __name__ == '__main__':
    main()