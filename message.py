import pygame as pg
from settings import *
from textwrap import wrap

class Messages:
    def __init__(self, sc):
        pg.font.init()
        self.sc = sc
        self.font = pg.font.Font(None, 40)
        self.msg_queue = []

    def add_to_queue(self, text):
        self.msg_queue.append(text)

    def draw_msg(self, events):
        if self.msg_queue:
            pg.draw.rect(self.sc, WHITE, (5, HEIGHT//3*2, WIDTH-10, HEIGHT//3-5))
            pg.draw.rect(self.sc, BLACK, (5, HEIGHT//3*2, WIDTH-10, HEIGHT//3-5), 4)

            lines = wrap(self.msg_queue[0], 50)

            y_diff = 0

            for line in lines:
                rendered_line = self.font.render(line, True, BLACK)
                self.sc.blit(rendered_line, (15, HEIGHT//3*2+10+y_diff))
                y_diff = y_diff + 30

            for event in events:
                if event.type == pg.MOUSEBUTTONUP and pg.rect.Rect(5, HEIGHT//3*2, WIDTH-10, HEIGHT//3-5).collidepoint(pg.mouse.get_pos()):
                    self.msg_queue.pop(0)