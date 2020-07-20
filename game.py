from Moduals.position import Position
from Moduals.cells import Cell
from Moduals.checkwin import check_win
import pygame
from Moduals import grid
import time
import random


def render_cells(cells):
    for i in cells:
        pygame.draw.rect(win, (255, 255, 255), (i.x * 300, i.y * 300, 300, 300))
        font = pygame.font.Font('freesansbold.ttf', 32)
        black = (0, 0, 0)
        if i.val == 0:
            texttren = ""
        else:
            texttren = str(i.val)
        text = font.render(texttren, True, black)
        textrect = text.get_rect()
        textrect.center = ((i.x * 300) + 150, (i.y * 300) + 150)
        # print("Render num: ", self.num)
        win.blit(text, textrect)


def find_pos(xp, yp, size):
    while True:
        if xp % size != 0:
            xp = xp - 1
        else:
            break
    while True:
        if yp % size != 0:
            yp = yp - 1
        else:
            break
    return xp, yp


def mousepress(x, y):
    global gamepos
    global turn
    cells = gamepos.cells
    madeamove = False
    for i in cells:
        if i.x == x and i.y == y and i.val == 0:
            i.val = "X"
            madeamove = True
    if madeamove is True:
        gamepos = Position(cells, turn * -1, 1)
        turn = turn * -1
    if gamepos.value == -1:
        print("Evaluation: X Is Winning")
    elif gamepos.value == 1:
        print("Evaluation: O Is Winning")
    else:
        print("Evaluation: Its a draw.")

pygame.init()
win = pygame.display.set_mode((900, 900))
pygame.font.init()
random = random.randint(0, 2)
if random is 1:
    turn = 1
else:
    turn = -1
pygame.display.set_caption("TicTacToe")
run = True
game = False
size = 300
grid = grid.Grid(surface=win, cellSize=300, axisLabels=0)
pygame.draw.rect(win, (255, 255, 255), (0, 0, 900, 900))
draw = False
cells = []
for i in range(3):
    for g in range(3):
        cells.append(Cell(0, g, i))
gamepos = Position(cells, turn, 0)
if turn == 1:
    cells[0].val = "O"
    turn = -1
while run:
    ev = pygame.event.get()
    x, y = pygame.mouse.get_pos()
    x, y = find_pos(x, y, size)
    x = int(x / 300)
    y = int(y / 300)
    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if turn == -1:
                mousepress(x, y)
    render_cells(gamepos.cells)
    grid.drawUseLine()
    pygame.display.update()
    draw = True
    if check_win(gamepos) == 1:
        run = False
        game = False
        draw = False
    elif check_win(gamepos) == -1:
        run = False
        game = True
        draw = False
    else:
        for i in gamepos.cells:
            if i.val == 0:
                draw = False
    if draw:
        run = False
        game = False
    if turn == 1 and run is True:
        gamepos = gamepos.bestpos
        turn = turn * -1

time.sleep(2)
pygame.draw.rect(win, (255, 255, 255), (0, 0, 1000, 1000))
font = pygame.font.Font('freesansbold.ttf', 32)
black = (0, 0, 0)
if game is False:
    if draw is False:
        text = font.render("Izgubio si", True, black)
    else:
        text = font.render("Izjednaceno", True, black)
else:
    text = font.render("Pobjedio Si", True, black)
textrect = text.get_rect()
textrect.center = (500, 500)
win.blit(text, textrect)
while True:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

