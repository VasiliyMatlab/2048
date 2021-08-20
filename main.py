import sys
import random
import pygame


COLORS = {
    0:  (130, 130, 130),
    2:  (255, 255, 255),
    4:  (255, 255, 128),
    8:  (255, 255, 0),
    16: (255, 235, 255),
    32: (255, 235, 128),
    64: (255, 235, 0)
}
WHITE = (255, 255, 255)
GRAY  = (130, 130, 130)
BLACK = (0, 0, 0)

SIZE = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = SIZE*SIZE_BLOCK + (SIZE+1)*MARGIN
HEIGHT = WIDTH + SIZE_BLOCK
TITLE_RECT = pygame.Rect(0,0, WIDTH, SIZE_BLOCK)


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

# Движение ячеек влево
def move_left(mas: list) -> list:
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != SIZE:
            row.append(0)
    for i in range(SIZE):
        for j in range(SIZE - 1):
            if mas[i][j] == mas[i][j+1] and mas[i][j] != 0:
                mas[i][j] *= 2
                mas[i].pop(j+1)
                mas[i].append(0)
    return mas

# Движение ячеек вправо
def move_right(mas: list) -> list:
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != SIZE:
            row.insert(0, 0)
    for i in range(SIZE):
        for j in range(SIZE-1, 0, -1):
            if mas[i][j] == mas[i][j-1] and mas[i][j] != 0:
                mas[i][j] *= 2
                mas[i].pop(j-1)
                mas[i].insert(0, 0)
    return mas

# Движение ячеек вверх
def move_up(mas: list) -> list:
    for j in range(SIZE):
        col = list()
        for i in range(SIZE):
            if mas[i][j] != 0:
                col.append(mas[i][j])
        while len(col) != SIZE:
            col.append(0)
        for i in range(SIZE - 1):
            if col[i] == col[i+1] and col[i] != 0:
                col[i] *= 2
                col.pop(i+1)
                col.append(0)
        for i in range(SIZE):
            mas[i][j] = col[i]
    return mas

# Движение ячеек вниз
def move_down(mas: list) -> list:
    for j in range(SIZE):
        col = list()
        for i in range(SIZE):
            if mas[i][j] != 0:
                col.append(mas[i][j])
        while len(col) != SIZE:
            col.insert(0, 0)
        for i in range(SIZE - 1, 0, -1):
            if col[i] == col[i-1] and col[i] != 0:
                col[i] *= 2
                col.pop(i-1)
                col.insert(0, 0)
        for i in range(SIZE):
            mas[i][j] = col[i]
    return mas

# Отрисовка интерфейса
def draw_interface():
    pygame.draw.rect(screen, WHITE, TITLE_RECT)
    font = pygame.font.SysFont("stxingkai", 70)
    pretty_print(mas)
    for row in range(SIZE):
        for col in range(SIZE):
            value = mas[row][col]
            text = font.render(str(value), True, BLACK)
            w = col*SIZE_BLOCK + (col+1)*MARGIN
            h = row*SIZE_BLOCK + (row+1)*MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w,h, SIZE_BLOCK,SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK-font_w)/2
                text_y = h + (SIZE_BLOCK-font_h)/2
                screen.blit(text, (text_x, text_y))


if __name__ == "__main__":
    mas = [[0]*SIZE for n in range(SIZE)]
    mas[1][2] = 2
    mas[3][0] = 4

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048")
    draw_interface()
    pygame.display.update()

    while is_zero_in_mas(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mas = move_left(mas)
                elif event.key == pygame.K_RIGHT:
                    mas = move_right(mas)
                elif event.key == pygame.K_UP:
                    mas = move_up(mas)
                elif event.key == pygame.K_DOWN:
                    mas = move_down(mas)
                empty = get_empty_list(mas)
                random.shuffle(empty)
                random_num = empty.pop()
                x, y = get_index_from_number(random_num)
                mas = insert_2_or_4(mas, x, y)
                draw_interface()
                pygame.display.update()