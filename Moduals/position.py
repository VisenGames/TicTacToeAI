from Moduals.checkwin import check_win
from Moduals.cells import Cell


class Position:
    def __init__(self, cells, turn, calc):
        self.cells = cells
        self.turn = turn
        self.value = "?"
        self.q = []
        self.bestpos = "?"
        self.bestmove = "?"
        if calc is 1:
            self.get_value()

    def get_value(self):
        self.value = check_win(self)
        if self.value == 0:
            for i in self.cells:
                if i.val == 0:
                    self.q.append(i)
        if len(self.q) is not 0:
            posvalchart = []
            for i in self.q:
                cells = []
                for g in self.cells:
                    if g.val == 0 and g.x == i.x and g.y == i.y:
                        if self.turn == 1:
                            cells.append(Cell("O", g.x, g.y))
                        elif self.turn == -1:
                            cells.append(Cell("X", g.x, g.y))
                    else:
                        cells.append(g)
                posvalchart.append(Position(cells, self.turn * -1, 1))

            posvalchartvalues = []
            for i in posvalchart:
                posvalchartvalues.append(i.value)
           # print(posvalchartvalues)
            if self.turn == 1:
                finalval = max(posvalchartvalues)
                for i in posvalchart:
                    if i.value == finalval:
                        self.bestpos = i
            elif self.turn == -1:
                finalval = min(posvalchartvalues)
                for i in posvalchart:
                    if i.value == finalval:
                        self.bestpos = i
            for i in self.cells:
                for g in self.bestpos.cells:
                    if i.x == g.x and i.y == g.y and i.val != g.val:
                        self.bestmove = g

            self.value = finalval


def main():
    cells = []
    cells.append(Cell("O", 0, 0))
    cells.append(Cell(0, 1, 0))
    cells.append(Cell("X", 2, 0))
    cells.append(Cell(0, 0, 1))
    cells.append(Cell("O", 1, 1))
    cells.append(Cell("O", 2, 1))
    cells.append(Cell("X", 0, 2))
    cells.append(Cell(0, 1, 2))
    cells.append(Cell("X", 2, 2))
    position = Position(cells, -1, 1)
    print(position.value)
    print(position.bestmove)
    print(f"Best move is {position.bestmove.val} {position.bestmove.x} {position.bestmove.y}")


if __name__ == "__main__":
    main()
