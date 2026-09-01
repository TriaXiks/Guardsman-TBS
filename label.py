import pygame as pg
from settings import *
from textwrap import wrap

class Label:
    def __init__(self, sc):
        pg.font.init()
        self.sc = sc
        self.font = pg.font.Font(None, 35)

    def draw_text(self, x, y, text):
        lines = wrap(text, 50)

        y_diff = 0
        for line in lines:
            rend_line = self.font.render(line, True, WHITE)
            self.sc.blit(rend_line, (x, y+y_diff))
            y_diff = y_diff + 25