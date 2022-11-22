from ai import get_dicts
import pygame
import time


pygame.font.init()
pygame.init()


o_dict, x_dict = get_dicts()
clock = pygame.time.Clock()
BASE_FONT_USER = pygame.font.Font(None, 30)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND = (27, 170, 156)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (176, 224, 230)


run_total = True
FPS = 60
radius = 70
BOARD = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT + 100))
screen.fill(BACKGROUND)
pygame.draw.rect(screen, "white", (0, HEIGHT,  WIDTH, 100))
pygame.display.set_caption("tictactoe")
pygame.display.update()


class Button:
    def __init__(self, pos, text, color="white", font=BASE_FONT_USER, background_color=None):
        self.x, self.y = pos
        self.text = text
        self.color = color
        self.font = font
        self.background_color = background_color
        self.button_surf = font.render(self.text, True, self.color)
        self.rect = pygame.Rect(self.x - 10, self.y - 10, self.button_surf.get_size()[0] + 20,
                                self.button_surf.get_size()[1] + 20)

    def draw(self):
        if self.background_color is not None:
            pygame.draw.rect(screen, self.background_color, (
                self.x - 10, self.y - 10, self.button_surf.get_size()[0] + 20, self.button_surf.get_size()[1] + 20))
        screen.blit(self.button_surf, (self.x, self.y))

    def clicked(self, even):
        x, y = pygame.mouse.get_pos()
        if even.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(x, y):
                return True
        return False


def draw_buttons(*args, **kwargs):
    """
    the function display added buttons on screen
    :param args: list of buttons
    :param kwargs: parameters like color
    :return none
    """
    if len(kwargs) > 0:
        screen.fill(kwargs["color"])
    for button in args:
        button.draw()
    pygame.display.update()


def start_menu():
    global run_total
    text_on_screen("choose game-mode", y_pos=HEIGHT/3)
    pc_button = Button((1.5 * WIDTH / 5, HEIGHT / 2), "pc", background_color="lightgrey", color="black")
    friend_button = Button((3 * WIDTH / 5, HEIGHT / 2), "friend", background_color="lightgrey", color="black")
    draw_buttons(pc_button, friend_button)
    run = True
    while run and run_total:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_total = False
            if pc_button.clicked(event):
                pygame.time.delay(250)
                pc_game()
            elif friend_button.clicked(event):
                pygame.time.delay(250)
                ftp_game()

    return


def player_choice():
    global run_total
    text_on_screen("choose character", color="white", background_color="black")
    x_button = Button((WIDTH / 3, HEIGHT / 1.5), "X")
    y_button = Button((2 * WIDTH / 3, HEIGHT / 1.5), "O")
    draw_buttons(x_button, y_button)
    run = True
    while run and run_total:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_total = False
            if x_button.clicked(event):
                return 2
            if y_button.clicked(event):
                return 1


def is_clear(mouseX, mouseY):
    if mouseY > HEIGHT:
        return False
    mouseX = int(mouseX // (WIDTH / 3))
    mouseY = int(mouseY // (HEIGHT / 3))
    if BOARD[mouseY][mouseX] == 'X' or BOARD[mouseY][mouseX] == 'O':
        return False
    return True


def did_win():
    for i in range(3):
        if BOARD[i][0] == BOARD[i][1] == BOARD[i][2]:
            if BOARD[i][0] == 'X' or BOARD[i][0] == 'O':
                return True
        elif BOARD[0][i] == BOARD[1][i] == BOARD[2][i]:
            if BOARD[0][i] == 'X' or BOARD[0][i] == 'O':
                return True
    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2]:
        if BOARD[0][0] == 'X' or BOARD[0][0] == 'O':
            return True
    elif BOARD[0][2] == BOARD[1][1] == BOARD[2][0]:
        if BOARD[0][2] == 'X' or BOARD[0][2] == 'O':
            return True
    return False


def who_won():
    for i in range(0, 3):
        if BOARD[i][0] == BOARD[i][1] == BOARD[i][2] != '':
            print(BOARD[i][0], BOARD[i][1], BOARD[i][2])
            pygame.draw.rect(screen, LIGHT_BLUE, (0, int(i * (WIDTH / 3) + WIDTH / 3 / 2 - 7.5), WIDTH, 15))
            pygame.display.update()
            return BOARD[i][0]
        elif BOARD[0][i] == BOARD[1][i] == BOARD[2][i] != '':
            pygame.draw.rect(screen, LIGHT_BLUE, (int(i * (HEIGHT / 3) + HEIGHT / 3 / 2 - 7.5), 0, 15, HEIGHT))
            pygame.display.update()
            return BOARD[0][i]
    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] != '':
        pygame.draw.line(screen, LIGHT_BLUE, (0, 0), (HEIGHT, WIDTH), 17)
        pygame.display.update()
        return BOARD[0][0]
    elif BOARD[0][2] == BOARD[1][1] == BOARD[2][0] != '':
        pygame.draw.line(screen, LIGHT_BLUE, (HEIGHT, 0), (0, WIDTH), 17)
        pygame.display.update()
        return BOARD[0][2]
    else:
        return ''


def draw_shapes():
    draw_lines()  # otherwise the writing looks bad
    for W in range(3):
        for H in range(3):
            if BOARD[W][H] == 'O':
                pygame.draw.circle(screen, RED,
                                   (int(H * (HEIGHT / 3) + HEIGHT / 3 / 2), int(W * (WIDTH / 3) + WIDTH / 3 / 2)),
                                   radius,
                                   7)
                pygame.display.update()
            if BOARD[W][H] == 'X':
                pygame.draw.line(screen, RED, (int(H * (HEIGHT / 3) + 40), int(W * (WIDTH / 3) + 40)),
                                 (int(H * (HEIGHT / 3) + HEIGHT / 3 - 40), int(W * (WIDTH / 3) + WIDTH / 3 - 40)), 10)
                pygame.draw.line(screen, RED, (int(H * (HEIGHT / 3) + 40), int(W * (WIDTH / 3) + WIDTH / 3 - 40)),
                                 (int(H * (HEIGHT / 3) + HEIGHT / 3 - 40), int(W * (WIDTH / 3) + 40)), 10)
    pygame.display.update()


def edit_board(mouseX, mouseY, character):
    mouseX = int(mouseX // (WIDTH / 3))
    mouseY = int(mouseY // (HEIGHT / 3))
    BOARD[mouseY][mouseX] = character


def edit_board_pc(cord, character):
    if BOARD[cord // 3][cord - 3 * (cord // 3)] == '':
        BOARD[cord // 3][cord - 3 * (cord // 3)] = character
    else:
        raise Exception


def draw_lines():
    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, "white", (0, HEIGHT, WIDTH, 100))
    pygame.draw.rect(screen, BLACK, (WIDTH / 3 - 10, 0, 20, WIDTH))
    pygame.draw.rect(screen, BLACK, (WIDTH * 2 / 3 - 10, 0, 20, WIDTH))
    pygame.draw.rect(screen, BLACK, (0, HEIGHT / 3 - 10, HEIGHT, 20))
    pygame.draw.rect(screen, BLACK, (0, HEIGHT * 2 / 3 - 10, HEIGHT, 20))
    pygame.display.update()


def text_on_screen(text, x_pos=WIDTH / 2, y_pos=HEIGHT / 2, background_color=BACKGROUND, color="black"):
    if background_color is not None:
        screen.fill(background_color)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text_dis = font.render(text, True, color)
    screen.blit(text_dis, (x_pos - text_dis.get_width()/2, y_pos - text_dis.get_height()/2))
    pygame.display.update()


def restart():
    draw_lines()
    for h in range(3):
        for w in range(3):
            BOARD[h][w] = ''
    return 1


def is_draw():
    for i in range(3):
        for j in range(3):
            if BOARD[i][j] != 'X' and BOARD[i][j] != 'O':
                return False
    return True


def ftp_game():
    run = True
    global run_total
    restart()
    restart_button = Button((WIDTH / 4, HEIGHT + 40), "restart", color="black")
    menu_button = Button((2 * WIDTH / 3, HEIGHT + 40), "menu", color="black")
    draw_buttons(restart_button, menu_button)
    player = 1
    player_dict = {1: 2, 2: 1}
    game_over = False
    while run and run_total:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_total = False
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                if is_clear(mouseX, mouseY):
                    if player == 1:
                        edit_board(mouseX, mouseY, 'X')
                    elif player == 2:
                        edit_board(mouseX, mouseY, 'O')
                    draw_shapes()
                    draw_buttons(restart_button, menu_button)
                    player = player_dict[player]
                    if is_draw():
                        game_over = True
                        pygame.time.delay(1000)
                        text_on_screen("DRAW")
                        draw_buttons(restart_button, menu_button)
                    if did_win() and not game_over:
                        who_won()
                        game_over = True
                        pygame.time.delay(1500)
                        if who_won() == 'X':
                            text_on_screen("X WON")
                        elif who_won() == 'O':
                            text_on_screen("O WON")
                        draw_buttons(restart_button, menu_button)
            if menu_button.clicked(event):
                start_menu()
            if restart_button.clicked(event):  # need  to replace with a button
                player = restart()
                draw_buttons(restart_button, menu_button)
                game_over = False


def pc_game():
    global run_total
    pc = player_choice()
    player_dict = {1: 2, 2: 1}
    sign_dict = {1: 'X', 2: 'O'}
    run = True
    player = 1
    game_over = False
    menu_button = Button((2 * WIDTH / 3, HEIGHT + 40), "menu", color="black")
    restart_button = Button((WIDTH / 4, HEIGHT + 40), "restart", color="black")
    restart()
    draw_buttons(restart_button, menu_button)
    if pc == 2:
        dict_in_use = o_dict
    else:
        dict_in_use = x_dict
        pygame.time.delay(550)
    while run and run_total:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run_total = False
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                if is_clear(mouseX, mouseY):
                    if player == 1 and pc != player:
                        edit_board(mouseX, mouseY, sign_dict[player])
                    elif player == 2 and pc != player:
                        edit_board(mouseX, mouseY, sign_dict[player])
                    draw_shapes()
                    draw_buttons(restart_button, menu_button)
                    player = player_dict[player]
                    if is_draw():
                        game_over = True
                        pygame.time.delay(1000)
                        text_on_screen("DRAW")
                        draw_buttons(restart_button, menu_button)
                    if did_win() and not game_over:
                        who_won()
                        game_over = True
                        pygame.time.delay(1500)
                        if who_won() == 'X':
                            text_on_screen("X WON")
                        elif who_won() == 'O':
                            text_on_screen("O WON")
                        draw_buttons(restart_button, menu_button)
                    time.sleep(1)
            if pc == player and not game_over:
                try:
                    edit_board_pc(dict_in_use[str(BOARD)], sign_dict[player])
                except:
                    pass
                draw_shapes()
                draw_buttons(restart_button, menu_button)
                player = player_dict[player]
                if is_draw():
                    game_over = True
                    pygame.time.delay(1000)
                    text_on_screen("DRAW")
                    draw_buttons(restart_button, menu_button)
                if did_win() and not game_over:
                    who_won()
                    game_over = True
                    pygame.time.delay(1500)
                    if who_won() == 'X':
                        text_on_screen("X WON")
                    elif who_won() == 'O':
                        text_on_screen("O WON")
                    draw_buttons(restart_button, menu_button)
            if menu_button.clicked(event):
                start_menu()
            elif restart_button.clicked(event):  # need  to replace with a button
                player = restart()
                pc = player_choice()
                if pc == 2:
                    dict_in_use = o_dict
                else:
                    dict_in_use = x_dict
                    pygame.time.delay(550)
                restart()
                draw_buttons(restart_button, menu_button)
                game_over = False


def main():
    global run_total
    while run_total:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_total = False
        start_menu()


if __name__ == "__main__":
    main()

