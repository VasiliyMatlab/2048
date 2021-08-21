import sys
import random
import pygame
import copy
import json
import os
from database import get_best, insert_result


COLORS = {
    0:      (130, 130, 130),
    2:      (255, 255, 255),
    4:      (255, 255, 128),
    8:      (255, 255, 0  ),
    16:     (255, 235, 255),
    32:     (255, 235, 128),
    64:     (255, 235, 0  ),
    128:    (255, 215, 255),
    256:    (255, 215, 128),
    512:    (255, 215, 0  ),
    1024:   (255, 195, 255),
    2048:   (255, 195, 128),
    4096:   (255, 195, 0  ),
    8192:   (255, 175, 255),
    16384:  (255, 175, 128),
    32768:  (255, 175, 0  )
}
ORANGE = (255, 127, 0)
WHITE = (255, 255, 255)
GRAY  = (130, 130, 130)
BLACK = (0, 0, 0)

SIZE = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = SIZE*SIZE_BLOCK + (SIZE+1)*MARGIN
HEIGHT = WIDTH + SIZE_BLOCK
TITLE_RECT = pygame.Rect(0,0, WIDTH, SIZE_BLOCK)
PLAYERS_DB = get_best()
USERNAME = None


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
def move_left(mas: list) -> tuple:
    origin = copy.deepcopy(mas)
    delta = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != SIZE:
            row.append(0)
    for i in range(SIZE):
        for j in range(SIZE - 1):
            if mas[i][j] == mas[i][j+1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j+1)
                mas[i].append(0)
    return mas, delta, origin != mas

# Движение ячеек вправо
def move_right(mas: list) -> tuple:
    origin = copy.deepcopy(mas)
    delta = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != SIZE:
            row.insert(0, 0)
    for i in range(SIZE):
        for j in range(SIZE-1, 0, -1):
            if mas[i][j] == mas[i][j-1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j-1)
                mas[i].insert(0, 0)
    return mas, delta, origin != mas

# Движение ячеек вверх
def move_up(mas: list) -> tuple:
    origin = copy.deepcopy(mas)
    delta = 0
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
                delta += col[i]
                col.pop(i+1)
                col.append(0)
        for i in range(SIZE):
            mas[i][j] = col[i]
    return mas, delta, origin != mas

# Движение ячеек вниз
def move_down(mas: list) -> tuple:
    origin = copy.deepcopy(mas)
    delta = 0
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
                delta += col[i]
                col.pop(i-1)
                col.insert(0, 0)
        for i in range(SIZE):
            mas[i][j] = col[i]
    return mas, delta, origin != mas

# Проверка условия, можно ли совершить какое-либо движение
def can_move(mas: list) -> bool:
    for i in range(SIZE - 1):
        for j in range(SIZE - 1):
            if mas[i][j] == mas[i][j+1] or mas[i][j] == mas[i+1][j]:
                return True
    for i in range(1, SIZE):
        for j in random(1, SIZE):
            if mas[i][j] == mas[i][j-1] or mas[i][j] == mas[i-1][j]:
                return True
    return False

# Инициализация констант (массива и счета)
def init_const():
    global score, mas
    mas = [[0]*SIZE for n in range(SIZE)]
    score = 0
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_num1 = empty.pop()
    x, y = get_index_from_number(random_num1)
    mas = insert_2_or_4(mas, x, y)
    random_num2 = empty.pop()
    x, y = get_index_from_number(random_num2)
    mas = insert_2_or_4(mas, x, y)

# Отрисовка экрана приветствия и ввода имени пользователя
def draw_intro():
    image = pygame.image.load('logo.png')
    font = pygame.font.SysFont("stxingkai", 70)
    text_welcome = font.render("Welcome!", True, WHITE)
    name = "Enter your name"
    is_entered_name = False

    while not is_entered_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == "Enter your name":
                        name = event.unicode
                    elif len(name) < 10:
                            name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    if len(name) != 0:
                        name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global USERNAME
                        USERNAME = name
                        is_entered_name = True
                        break

        text_name = font.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(image, (200, 200)), (10, 10))
        screen.blit(text_welcome, (230, 90))
        screen.blit(text_name, rect_name)
        pygame.display.update()
        screen.fill(BLACK)

# Отрисовка лучших игроков
def draw_top_gamers():
    font_top = pygame.font.SysFont("simsum", 30)
    font_player = pygame.font.SysFont("simsum", 24)
    text_top = font_top.render("Best tries: ", True, ORANGE)
    screen.blit(text_top, (300, 5))
    PLAYERS_DB = get_best()
    for index, player in enumerate(PLAYERS_DB):
        name, score = player
        s = f"{index+1}. {name} - {score}"
        text_player = font_player.render(s, True, ORANGE)
        screen.blit(text_player, (300, 30 + 30*index))

# Отрисовка интерфейса
def draw_interface(score: int, delta = 0) -> None:
    pygame.draw.rect(screen, WHITE, TITLE_RECT)
    font = pygame.font.SysFont("stxingkai", 70)
    font_score = pygame.font.SysFont("simsum", 48)
    text_score = font_score.render("Score: ", True, ORANGE)
    text_score_value = font_score.render(f"{score}", True, ORANGE)
    font_delta = pygame.font.SysFont("simsum", 32)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value, (150, 35))
    if delta > 0:
        text_delta = font_delta.render(f"+{delta}", True, ORANGE)
        screen.blit(text_delta, (145, 65))
    pretty_print(mas)
    draw_top_gamers()
    for row in range(SIZE):
        for col in range(SIZE):
            value = mas[row][col]
            text = font.render(str(value), True, BLACK)
            w = col*SIZE_BLOCK + (col+1)*MARGIN
            h = row*SIZE_BLOCK + (row+1)*MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], \
                (w,h, SIZE_BLOCK,SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK-font_w)/2
                text_y = h + (SIZE_BLOCK-font_h)/2
                screen.blit(text, (text_x, text_y))

# Отрисовка конца игры
def draw_game_over():
    global USERNAME
    image = pygame.image.load('logo.png')
    font = pygame.font.SysFont("stxingkai", 65)
    text_game_over = font.render("Game over!", True, WHITE)
    text_final_score = font.render(f"You scored {score}", True, WHITE)
    best_score = PLAYERS_DB[0][1]
    if score > best_score:
        text = "New high score!"
    else:
        text = f"Recored is {best_score}"
    text_record = font.render(text, True, WHITE)
    insert_result(USERNAME, score)

    make_dicision = False
    while not make_dicision:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # restart game with name
                    make_dicision = True
                    init_const()
                elif event.key == pygame.K_RETURN:
                    # restart game without name
                    USERNAME = None
                    init_const()
                    make_dicision = True
        screen.blit(text_game_over, (220, 90))
        screen.blit(text_final_score, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(pygame.transform.scale(image, (200, 200)), (10, 10))
        pygame.display.update()
        screen.fill(BLACK)

# Игровой цикл
def game_loop():
    global score, mas
    draw_interface(score)
    pygame.display.update()

    while is_zero_in_mas(mas) or can_move(mas):
        is_mas_moved = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game()
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT:
                    mas, delta, is_mas_moved = move_left(mas)
                elif event.key == pygame.K_RIGHT:
                    mas, delta, is_mas_moved = move_right(mas)
                elif event.key == pygame.K_UP:
                    mas, delta, is_mas_moved = move_up(mas)
                elif event.key == pygame.K_DOWN:
                    mas, delta, is_mas_moved = move_down(mas)
                else:
                    continue
                score += delta
                if is_zero_in_mas(mas) and is_mas_moved:
                    empty = get_empty_list(mas)
                    random.shuffle(empty)
                    random_num = empty.pop()
                    x, y = get_index_from_number(random_num)
                    mas = insert_2_or_4(mas, x, y)
                draw_interface(score, delta)
                pygame.display.update()

# Сохранение игры
def save_game():
    data = {
        'user':  USERNAME,
        'score': score,
        'mas':   mas
    }
    with open("saved_game.txt", 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    if SIZE < 4:
        exit()
    path = os.getcwd()
    full_path = os.path.join(path, "saved_game.txt")
    if "saved_game.txt" in os.listdir(path):
        with open("saved_game.txt", 'r') as file:
            data = json.load(file)
        USERNAME = data['user']
        score = data['score']
        mas = data['mas']
        os.remove(full_path)
    else:
        init_const()

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048")

    # Главный цикл программы
    while True:
        if USERNAME is None:
            draw_intro()
        game_loop()
        draw_game_over()