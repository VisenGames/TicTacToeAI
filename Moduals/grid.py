import pygame
import os
import time

WINDOWS_LOCATION = '0,0'
WIDTH = 900
HEIGHT = 900

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

CELL_SIZE = 300
GRID_COORD_MARGIN_SIZE = 0


class Grid():
    def __init__(self, surface, cellSize, axisLabels):
        self.surface = surface
        self.colNb = surface.get_width() // cellSize
        self.lineNb = surface.get_height() // cellSize
        self.cellSize = cellSize
        self.axisLabels = axisLabels
        self.grid = [[0 for i in range(self.colNb)] for j in range(self.lineNb)]
        self.font = pygame.font.SysFont('arial', 12, False)

    def drawUseLine(self):
        for li in range(self.lineNb):
            liCoord = GRID_COORD_MARGIN_SIZE + li * CELL_SIZE
            if self.axisLabels:
                if li < 10:
                    ident = '   '
                else:
                    ident = '  '
                text = self.font.render(ident + str(li), 1, (0, 0, 0))
                self.surface.blit(text, (0, liCoord))
            pygame.draw.line(self.surface, BLACK, (GRID_COORD_MARGIN_SIZE, liCoord),
                             (self.surface.get_width(), liCoord))
        for co in range(self.colNb):
            colCoord = GRID_COORD_MARGIN_SIZE + co * CELL_SIZE
            if self.axisLabels:
                if co < 10:
                    ident = '  '
                else:
                    ident = ' '
                text = self.font.render(ident + str(co), 1, (0, 0, 0))
                self.surface.blit(text, (colCoord, 1))
            pygame.draw.line(self.surface, BLACK, (colCoord, GRID_COORD_MARGIN_SIZE),
                             (colCoord, self.surface.get_height()))
