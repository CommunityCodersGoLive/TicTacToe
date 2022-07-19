import pygame
import pyautogui

def IsGameOver(combi):
    global winner, score_X, score_O
    game_over = False
    if combi == "XXX":
        game_status = False
        game_over = True
        print("game over, player X wins")
        winner = "Game Over, Player X wins"
        score_X += 1
    elif combi == "OOO":
        game_over = True
        print("Game Over, player O wins")
        winner = "Game Over, Player O wins"
        game_status = False
        score_O += 1
    return game_over

def CheckGameStatus():
    global winA, winB
    game_status = True
    game_over = False
    combi = ""
    i = 0
    j = 0
    dir = "col"
    winning_combo = []
    winning_coordinates = []

    while game_status:
        while game_over == False and ((dir == "col" and i < cols) or (dir == "row" and j < cols)):
            print(dir, i, j)

            combi = combi + matrix[i][j]
            winning_combo.append(cell_no[i][j])
            print("circle_center", circle_center)
            winning_coordinates.append(circle_center[cell_no[i][j]])

            game_over = IsGameOver(combi)
            if game_over:
                print(winning_combo, winning_coordinates, len(winning_coordinates))
                # winA = winning_coordinates[0]
                # winB = winning_coordinates[2]
                if dir == "col":
                    winA = [winning_coordinates[0][0], winning_coordinates[0][1] - 100]
                    winB = [winning_coordinates[2][0], winning_coordinates[2][1] + 100]
                elif dir == "row":
                    winA = [winning_coordinates[0][0] - 100, winning_coordinates[0][1]]
                    winB = [winning_coordinates[2][0] + 100, winning_coordinates[2][1]]


            if dir == "col":
                i += 1
            elif dir == "row":
                j += 1
        if dir == "col":
            i = 0
            j += 1
        elif dir == "row":
            i += 1
            j = 0
        combi = ""
        winning_combo = []
        winning_coordinates = []
        if dir == "col":
            if j == cols:
                # game_status = False
                dir = "row"
                i = 0
                j = 0
        elif dir == "row":
            if i == cols:
                game_status = False
                i = 0
                j = 0

    dir = "dia"
    sub_dir = "forward"
    i = 0
    j = 0
    game_status = True
    while game_status:
        while game_over == False and i < cols:
            print(dir, sub_dir, i, j)

            combi = combi + matrix[i][j]
            winning_combo.append(cell_no[i][j])
            winning_coordinates.append(circle_center[cell_no[i][j]])

            game_over = IsGameOver(combi)
            if game_over:
                print(winning_combo, winning_coordinates, len(winning_coordinates))
                winA = winning_coordinates[0]
                winB = winning_coordinates[2]
                if sub_dir == "forward":
                    winA = [winning_coordinates[0][0] - 100, winning_coordinates[0][1] - 100]
                    winB = [winning_coordinates[2][0] + 100, winning_coordinates[2][1] + 100]
                elif sub_dir == "backward":
                    winA = [winning_coordinates[0][0] + 100, winning_coordinates[0][1] - 100]
                    winB = [winning_coordinates[2][0] - 100, winning_coordinates[2][1] + 100]


            if sub_dir == "forward":
                i += 1
                j += 1
            elif sub_dir == "backward":
                i += 1
                j -= 1
        if sub_dir == "backward":
            game_status = False
        else:
            sub_dir = "backward"
            i = 0
            j = cols - 1
            combi = ""
            winning_combo = []
            winning_coordinates = []
    print("game_over:", game_over)
    return game_over    

def draw_circle_sign(x):
    center_coordinates = circle_center[x]
    radius_down = 30
    pygame.draw.circle(screen, (0, 255, 255), center_coordinates, 100 - radius_down, 10)

def draw_cross_sign(x):
    corner_coordinates = cross_coord[x]
    # pygame.draw.line(screen, (255, 0, 255), corner_coordinates[0], corner_coordinates[1], 5)
    # pygame.draw.line(screen, (255, 0, 255), corner_coordinates[2], corner_coordinates[3], 5)
    cross_down = 30
    new_corner_coordinates0 = (corner_coordinates[0][0], corner_coordinates[0][1])
    new_corner_coordinates1 = (corner_coordinates[1][0], corner_coordinates[1][1])
    new_corner_coordinates2 = (corner_coordinates[2][0], corner_coordinates[2][1])
    new_corner_coordinates3 = (corner_coordinates[3][0], corner_coordinates[3][1])
    pygame.draw.line(screen, (255, 0, 255), (new_corner_coordinates0[0] + cross_down, new_corner_coordinates0[1] + cross_down), (new_corner_coordinates1[0] - cross_down, new_corner_coordinates1[1] - cross_down), 10)
    pygame.draw.line(screen, (255, 0, 255), (new_corner_coordinates2[0] - cross_down, new_corner_coordinates2[1] + cross_down), (new_corner_coordinates3[0] + cross_down, new_corner_coordinates3[1] - cross_down), 10)


def draw_state():
    # print("draw_state", len(move_X))
    for i in range(0, len(move_X)):
        if move_state[i] == "O":
            draw_circle_sign(move_cell[i])
        elif move_state[i] == "X":
            draw_cross_sign(move_cell[i])    

def draw_game_outline():
    pygame.draw.line(screen, (255, 255, 255), (0, 200), (600, 200), 10)
    pygame.draw.line(screen, (255, 255, 255), (0, 400), (600, 400), 10)
    pygame.draw.line(screen, (255, 255, 255), (200, 0), (200, 600), 10)
    pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600), 10)


def click_cell():
    global row_index, column_index, replay_click
    global pos, X_click, Y_click, cell, move_X, move_Y, move_state, move_cell, state, rows, cols, matrix, cell_no, row_index, column_index, winA, winB, game_over, winner
    if (X_click > 0 and X_click < 200) and (Y_click > 0 and Y_click < 200):
        cell = "C1"
        row_index = 0
        column_index = 0
    elif (X_click > 200 and X_click < 400) and (Y_click > 0 and Y_click < 200):
        cell = "C2"
        row_index = 0
        column_index = 1
    elif (X_click > 400 and X_click < 600) and (Y_click > 0 and Y_click < 200):
        cell = "C3"
        row_index = 0
        column_index = 2
    elif (X_click > 0 and X_click < 200) and (Y_click > 200 and Y_click < 400):
        cell = "C4"
        row_index = 1
        column_index = 0
    elif (X_click > 200 and X_click < 400) and (Y_click > 200 and Y_click < 400):
        cell = "C5"
        row_index = 1
        column_index = 1
    elif (X_click > 400 and X_click < 600) and (Y_click > 200 and Y_click < 400):
        cell = "C6"
        row_index = 1
        column_index = 2
    elif (X_click > 0 and X_click < 200) and (Y_click > 400 and Y_click < 600):
        cell = "C7"
        row_index = 2
        column_index = 0
    elif (X_click > 200 and X_click < 400) and (Y_click > 400 and Y_click < 600):
        cell = "C8"
        row_index = 2
        column_index = 1
    elif (X_click > 400 and X_click < 600) and (Y_click > 400 and Y_click < 600):
        cell = "C9"
        row_index = 2
        column_index = 2
    else:
        cell = ""
        row_index = ""
        column_index = ""
        if (X_click > 900 and X_click < (900 + 160)) and (Y_click > (200 - 60) and Y_click < (200 + 60)):
            replay_click = True
            # initialize variables - start

            pos = [0, 0]
            X_click = 0
            Y_click = 0
            cell = ""
            move_X = []
            move_Y = []
            move_state = []
            move_cell = []
            state = "X"
            rows, cols = (3, 3)
            matrix = [["" for i in range(cols)] for j in range(rows)]
            cell_no = [["C" for i in range(cols)] for j in range(rows)]
            row_index = -1
            column_index = -1
            winA, winB = [], []
            init_dict()
            game_over = False
            winner = ""
            # initialize variables - end
    return cell











def draw_circle():
    # print(cell)

    for i in range(0, len(move_X) - 1):
        # pygame.draw.circle(screen, (0, 255, 255), (move_X[i], move_Y[i]), 100, 2)
        # print(cell)
        center_coordinates = circle_center[move_cell[i]]
        # print(type(center_coordinates))
        # pygame.draw.circle(screen, (0, 255, 255), (move_X[i], move_Y[i]), 100, 2)
        pygame.draw.circle(screen, (0, 255, 255), center_coordinates, 100, 2)


def draw_cross():
    for i in range(0, len(move_X) - 1):
        # print("move_cell[i] ", move_cell[i])
        corner_coordinates = cross_coord[move_cell[i]]
        # print(corner_coordinates[0])
        pygame.draw.line(screen, (255, 0, 255), corner_coordinates[0], corner_coordinates[1], 2)
        pygame.draw.line(screen, (255, 0, 255), corner_coordinates[2], corner_coordinates[3], 2)


def draw_button(replay_hover):
    # pygame.draw.ellipse(surface, color, bounding rectangle, thickness)
    pygame.draw.ellipse(screen, (255, 127, 80), (900, 207, 160, 60), 0)
    pygame.draw.ellipse(screen, (255, 165, 0), (900, 200, 160, 60), 0)
    if replay_hover:
        screen.blit(replay_button2, (925, 215))
    else:
        screen.blit(replay_button, (925, 215))

def check_replay():
    global X_replay, Y_replay, replay_hover

    if X_replay > 900 and X_replay < (900 + 160):
        if Y_replay > (200 - 60) and Y_replay < (200 + 60):
            replay_hover = True
            # print(X_replay, Y_replay)

        else:
            replay_hover = False
    else:
        replay_hover = False

def init_dict():
    global circle_center, cross_coord

    srl = 1
    for i in range(0, rows):
        for j in range(0, cols):
            cell_no[i][j] = cell_no[i][j] + str(srl)
            srl += 1
    print(cell_no)

    circle_center = {"C1": (100, 100),
                     "C2": (300, 100),
                     "C3": (500, 100),
                     "C4": (100, 300),
                     "C5": (300, 300),
                     "C6": (500, 300),
                     "C7": (100, 500),
                     "C8": (300, 500),
                     "C9": (500, 500)}

    # dictionary for drawing cross
    cross_coord = {"C1": ((0, 0), (200, 200), (200, 0), (0, 200)),
                   "C2": ((200, 0), (400, 200), (400, 0), (200, 200)),
                   "C3": ((400, 0), (600, 200), (600, 0), (400, 200)),
                   "C4": ((0, 200), (200, 400), (200, 200), (0, 400)),
                   "C5": ((200, 200), (400, 400), (400, 200), (200, 400)),
                   "C6": ((400, 200), (600, 400), (600, 200), (400, 400)),
                   "C7": ((0, 400), (200, 600), (200, 400), (0, 600)),
                   "C8": ((200, 400), (400, 600), (400, 400), (200, 600)),
                   "C9": ((400, 400), (600, 600), (600, 400), (400, 600))}

def score_board():
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(860, 300, 250, 60),  2)
    screen.blit(score_hdr, (900, 315))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(860, 360, 150, 60), 2)
    screen.blit(player_X, (870, 380))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(1010, 360, 100, 60), 2)
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(860, 420, 150, 60), 2)
    screen.blit(player_O, (870, 440))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(1010, 420, 100, 60), 2)
    # winning_msg = font.render(winner, True, (255, 255, 0))
    screen.blit(font.render(str(score_O), True, (255, 255, 0)), (1030, 440))
    screen.blit(font.render(str(score_X), True, (255, 255, 0)), (1030, 380))

# driver code
import pygame
import pyautogui

pygame.init()

page_width, page_depth = pyautogui.size()
page_depth = int(page_depth * .95)

# screen = pygame.display.set_mode((600, 600))
screen = pygame.display.set_mode((page_width, page_depth))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.Font('freesansbold.ttf', 32)
winner = ""
replay_button = font.render("Replay", True, (255, 255, 255))
replay_button2 = font.render("Replay", True, (255, 0, 0))
score_hdr = font.render("Score Card", True, (255, 255, 0))
player_X = font.render("Player-X", True, (255, 255, 0))
player_O = font.render("Player-O", True, (255, 255, 0))


running = True
pos = [0, 0]
X_click = 0
Y_click = 0
cell = ""
move_X = []
move_Y = []
move_state = []
move_cell = []
state = "X"
rows, cols = (3, 3)
matrix = [["" for i in range(cols)] for j in range(rows)]
cell_no = [["C" for i in range(cols)] for j in range(rows)]
row_index = -1
column_index = -1
winA, winB = [], []
# print(matrix)
X_replay, Y_replay = 0, 0
replay_hover = False
replay_click = False
score_X, score_O = 0, 0

# dictionary for drawing circle
circle_center, cross_coord = {}, {}
init_dict()
print("circle_center_init", circle_center)

# print(cross_coord["C1"])

game_over = False

while running:
    screen.fill((0, 0, 0))
    winning_msg = font.render(winner, True, (255, 255, 0))
    screen.blit(winning_msg, (775, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            X_replay, Y_replay = pygame.mouse.get_pos()
            check_replay()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            X_click = pos[0]
            Y_click = pos[1]

            cell = click_cell()
            print(cell)
            if game_over == False:

                if cell != "":
                    if cell not in move_cell:
                        move_cell.append(cell)
                        move_X.append(pos[0])
                        move_Y.append(pos[1])
                        move_state.append(state)
                        matrix[row_index][column_index] = state
                        game_over = CheckGameStatus()
                        if state == "X":
                            state = "O"
                        elif state == "O":
                            state = "X"



    draw_game_outline()
    
 
    draw_state()

    if game_over:
        pygame.draw.line(screen, (255, 255, 0), winA, winB, 5)

    draw_button(replay_hover)

    score_board()
    
    # IsGameOver()
    
    pygame.display.flip()

pygame.display.update()