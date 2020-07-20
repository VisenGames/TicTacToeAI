# from Moduals.position import Position
# from Moduals.cells import Cell


def check_win(position):
    xcount = 0
    ocount = 0
    for g in range(3):
        for i in position.cells:
            if i.x == g and i.val == "X":
                xcount += 1
            elif i.x == g and i.val == "O":
                ocount += 1
        if xcount == 3:
            return -1
        elif ocount == 3:
            return 1
        xcount = 0
        ocount = 0
    xcount = 0
    ocount = 0
    for g in range(3):
        for i in position.cells:
            if i.y == g and i.val == "X":
                xcount += 1
            elif i.y == g and i.val == "O":
                ocount += 1
        if xcount == 3:
            return -1
        elif ocount == 3:
            return 1
        xcount = 0
        ocount = 0
    xcount = 0
    ocount = 0
    for g in range(3):
        for i in position.cells:
            if i.y == g and i.x == g and i.val == "X":
                xcount += 1
            elif i.y == g and i.x == g and i.val == "O":
                ocount += 1
    if xcount == 3:
        return -1
    elif ocount == 3:
        return 1
    xcount = 0
    ocount = 0
    for g in range(3):
        for i in position.cells:
            if i.y == g and i.x == 2 - g and i.val == "X":
                xcount += 1
            elif i.y == g and i.x == 2 - g and i.val == "O":
                ocount += 1
    if xcount == 3:
        return -1
    elif ocount == 3:
        return 1
    xcount = 0
    ocount = 0
    return 0


def main():
    cells = []
    for i in range(3):
        for g in range(3):
            if g == 0:
                cells.append(Cell("O", g, i))
            else:
                cells.append(Cell(0, g, i))
    postion = Position(cells)
    print(check_win(postion))
    cells = []
    cells.append(Cell(0, 0, 0))
    cells.append(Cell(0, 1, 0))
    cells.append(Cell("O", 2, 0))
    cells.append(Cell(0, 0, 1))
    cells.append(Cell("X", 1, 1))
    cells.append(Cell("O", 2, 1))
    cells.append(Cell("X", 0, 2))
    cells.append(Cell(0, 1, 2))
    cells.append(Cell("O", 2, 2))
    position = Position(cells)
    print(check_win(position))


if __name__ == "__main__":
    main()
